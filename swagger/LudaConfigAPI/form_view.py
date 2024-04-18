#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2020/8/17 17:55
# @Author  : system
# @File    : form_view.py


import allure

class FormView:
    '''
    test
    '''

    @allure.step('保存表单视图')
    def _form_view_saveOrUpdate(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/view/saveOrUpdate'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('查询表单视图，通过id')
    def _form_view_viewId(self, item_fixture, viewId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/view/{viewId}'
        response = item_fixture.request('get', resource)
        return response

    @allure.step('查询表单视图，指定类型视图')
    def _form_view_formId_type(self, item_fixture, formId, type):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/view/{formId}/{type}'
        response = item_fixture.request('get', resource)
        return response

    @allure.step('表单视图列表')
    def _form_view_list_formId(self, item_fixture, formId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/view/list/{formId}'
        response = item_fixture.request('get', resource)
        return response

    @allure.step('删除表单视图，通过id')
    def _form_view_delete_viewId(self, item_fixture, viewId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/form/view/delete/{viewId}'
        response = item_fixture.request('delete', resource)
        return response


