#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2020/8/17 17:55
# @Author  : system
# @File    : group_app.py


import allure

class GroupApp:
    '''
    test
    '''

    @allure.step('保存分组（支持新增、删除、更新、应用排序）')
    def _app_group_save(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/group/save'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('分组列表')
    def _app_group_list(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/app/group/list'
        response = item_fixture.request('get', resource)
        return response


