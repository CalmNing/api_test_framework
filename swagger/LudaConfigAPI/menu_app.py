#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2020/8/17 17:55
# @Author  : system
# @File    : menu_app.py


import allure

class MenuApp:
    '''
    test
    '''

    @allure.step('重命名')
    def _app_menu_rename_menuId(self, item_fixture, menuId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/menu/rename/{menuId}'
        response = item_fixture.request('put', resource)
        return response

    @allure.step('移动')
    def _app_menu_move_menuId(self, item_fixture, menuId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/menu/move/{menuId}'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('删除')
    def _app_menu_delete_menuId(self, item_fixture, menuId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/menu/delete/{menuId}'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('新建')
    def _app_menu_create(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/menu/create'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('列表')
    def _app_menu_list_appId(self, item_fixture, appId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/menu/list/{appId}'
        response = item_fixture.request('get', resource)
        return response


