#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2024/4/16 13:11
# @Author  : anning
# @File    : resolution.py
import os
from functools import reduce
from pathlib import Path

import chevron
import requests


class SwaggerJSONResolution:
    def __init__(self, url):
        self.url = url

    def get_swagger_api_docs_response(self):
        # 获取接口详情
        response = requests.get(self.url).json()
        return response

    def get_info_title(self):
        """
        获取swagger title 用来生成文件夹
        :return:
        """
        title = self.get_swagger_api_docs_response().get('info').get('title').split(' ')
        return ''.join(title)

    def get_paths(self):
        # 提取 paths
        response = self.get_swagger_api_docs_response()
        paths = response.get('paths')
        return paths

    def get_interface_tags(self) -> set:
        # 提取 tags， 作用用tag分组，相同tag的接口 生成到同一个 py文件中
        tags = []
        for uri, uri_v in self.get_paths().items():
            for method, method_v in uri_v.items():
                tags.append(method_v.get('tags')[0])
        return set(tags)

    def clen_data(self):
        """
        清洗数据
        :return:
        """
        class_list = []
        for file_name in self.get_interface_tags():
            class_data = {
                'file_name': file_name,
                'class_name': '',
                "class_description": 'test',
                'interfaces': []
            }
            for uri, uri_v in self.get_paths().items():
                for method, method_v in uri_v.items():
                    if method_v.get('tags')[0] == file_name:
                        summary = method_v.get('summary', None)
                        parameters = method_v.get('parameters', None)
                        function_data = {
                            'function_name': uri.replace('/', '_').replace('-', '_')
                            .replace('{', '').replace('}', ''),
                            "function_description": '',
                            'uri': uri,
                            "summary": summary,
                            'method': method,
                            'path': []
                        }
                        for parameter in parameters:
                            for key, value in parameter.items():
                                if key == 'name' and value != "access-token":
                                    function_data.get("path").append(value)
                        class_data.get('interfaces').append(function_data)
            uri_list = []
            for interface in class_data.get('interfaces'):
                uri_list.append(interface.get('uri').split('/'))
            sets = [set(lst) for lst in uri_list]
            intersection = reduce(lambda x, y: x & y, sets)
            result = list(intersection)
            class_data['class_name'] = ''.join([element.capitalize() for element in result if element])
            class_data['file_name'] = '_'.join([element for element in result if element])
            class_list.append(class_data)
        return class_list

    def main(self):
        """
        生成接口文件
        :return:
        """
        for class_l in self.clen_data():
            with open('./interface.mustache', 'r') as mustache:
                interfaces = chevron.render(mustache, class_l)
                path = Path.cwd()
                if not os.path.exists(f'swagger/{sw.get_info_title()}'):
                    os.makedirs(f'swagger/{sw.get_info_title()}')
                case_demo_default = path / f'swagger/{sw.get_info_title()}' / f"{class_l.get('file_name')}.py"
                with open(case_demo_default, 'w', encoding='utf-8') as f:
                    f.write(interfaces)

if __name__ == '__main__':
    sw = SwaggerJSONResolution('http://192.168.13.178:19983/luda-config/v3/api-docs')
    class_list = sw.main()
