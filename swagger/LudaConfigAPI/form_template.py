#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2020/8/17 17:55
# @Author  : system
# @File    : form_template.py


import allure

class FormTemplate:
    '''
    test
    '''

    @allure.step('更新表单&amp;菜单名称')
    def _form_template_rename_formId(self, item_fixture, formId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/template/rename/{formId}'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('获取表单列表')
    def _form_template_list_appId(self, item_fixture, appId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/template/list/{appId}'
        response = item_fixture.request('get', resource)
        return response

    @allure.step('获取字段列表')
    def _form_template_fields_formId(self, item_fixture, formId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/template/fields/{formId}'
        response = item_fixture.request('get', resource)
        return response

    @allure.step('获取表单详情')
    def _form_template_detail_formId(self, item_fixture, formId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/template/detail/{formId}'
        response = item_fixture.request('get', resource)
        return response

    @allure.step('获取表单详情，通过菜单id')
    def _form_template_detail_bindType_bindId(self, item_fixture, bindType, bindId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/template/detail/{bindType}/{bindId}'
        response = item_fixture.request('get', resource)
        return response


