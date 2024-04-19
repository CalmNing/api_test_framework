#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2024/4/16 13:11
# @Author  : anning
# @File    : resolution.py
import json
import os
from functools import reduce
from pathlib import Path

import chevron
import jsonpath
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
                        requestBody = method_v.get('requestBody', None)
                        function_data = {
                            'function_name': uri.replace('/', '_').replace('-', '_')
                            .replace('{', '').replace('}', ''),
                            "function_description": '',
                            'uri': uri,
                            "summary": summary,
                            'method': method,
                            'path': [],
                            'requestBody': jsonpath.jsonpath(requestBody, '$.content.application/json.schema.$ref')
                        }
                        for parameter in parameters:
                            for key, value in parameter.items():
                                if key == 'name' and value != "access-token":
                                    function_data.get("path").append(value)
                        class_data.get('interfaces').append(function_data)
            # 获取所有接口的uri 并且用 / 分割成列表
            uri_list = []
            for interface in class_data.get('interfaces'):
                uri_list.append(interface.get('uri').split('/'))
            # 对多个接口uri取交集 拿到公共的部分 用来生成 类名称 和 文件名称
            sets = [set(lst) for lst in uri_list]
            intersection = reduce(lambda x, y: x & y, sets)
            result = list(intersection)
            # 类名称首字符大写
            class_data['class_name'] = ''.join([element.capitalize() for element in result if element])
            # 文件名称用下划线分割
            class_data['file_name'] = '_'.join([element for element in result if element])
            class_list.append(class_data)
        return class_list

    def clen_data_body(self):
        response = self.get_swagger_api_docs_response()
        schemas = jsonpath.jsonpath(response, '$.components.schemas')
        schema_list = []
        for schema in schemas:
            dict_a = {}
            for model, model_v in schema.items():
                dict_a[model] = {}
                fields = jsonpath.jsonpath(model_v, f'$.properties')
                for field in fields:
                    for k, v in field.items():
                        k_d = {k: v.get('type')}
                        dict_a[model].update(k_d)
            schema_list.append(dict_a)
        return schema_list

    def analysis_components_schemas(self, ref):
        # 递归生成嵌套的请求body
        schema = ref.split('/')[-1]
        schema_d = self.get_swagger_api_docs_response().get('components').get('schemas').get(schema).get('properties')
        body = {}
        for k, v in schema_d.items():
            if v.get('type') == 'array' and v.get('items').get('$ref'):
                k_d = {k: [self.analysis_components_schemas(v.get('items').get('$ref'))]}
                body.update(k_d)
            elif v.get('type') == 'array':
                k_d = {k: []}
                body.update(k_d)
            else:
                k_d = {k: v.get('type')}
                body.update(k_d)
        return body



    def generate_body(self):
        data = self.clen_data()
        for c in data:
            for interface in c.get('interfaces'):
                if interface.get('requestBody'):
                    interface['body'] = self.analysis_components_schemas(interface.get('requestBody')[0])
        return data

    def main(self):
        """
        生成接口文件
        :return:
        """
        for class_l in self.generate_body():
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
    print(json.dumps(sw.main()))
