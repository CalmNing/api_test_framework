#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2020/8/17 17:55
# @Author  : system
# @File    : file.py


import allure

class File:
    '''
    test
    '''

    @allure.step('申请上传地址')
    def _file_upload_url(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/file/upload-url'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('申请预览地址')
    def _file_preview_url(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/file/preview-url'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('申请下载地址')
    def _file_download_url(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/file/download-url'
        response = item_fixture.request('post', resource)
        return response


