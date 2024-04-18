#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2020/8/17 17:55
# @Author  : system
# @File    : app.py


import allure

class App:
    '''
    test
    '''

    @allure.step('移动位置')
    def _app_move_appId(self, item_fixture, appId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/move/{appId}'
        response = item_fixture.request('put', resource)
        return response

    @allure.step('修改')
    def _app_modify_appId(self, item_fixture, appId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/modify/{appId}'
        response = item_fixture.request('put', resource)
        return response

    @allure.step('删除')
    def _app_delete_app_appId(self, item_fixture, appId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/delete-app/{appId}'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('新建')
    def _app_create(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/create'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('应用列表')
    def _app_list(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/list'
        response = item_fixture.request('get', resource)
        return response


