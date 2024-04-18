#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @TIME    : 2020/8/17 17:55
# @Author  : system
# @File    : business_data.py


import allure

class BusinessData:
    '''
    test
    '''

    @allure.step('权限码列表，返回当前用户有权限列表')
    def _business_data_permission_list(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/business/data/permission-list'
        response = item_fixture.request('post', resource)
        return response

    @allure.step('用户列表，根据项目id/标段id')
    def _business_data_user_list_projectId(self, item_fixture, projectId, sectionId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/business/data/user-list/{projectId}'
        response = item_fixture.request('get', resource)
        return response

    @allure.step('标段列表，仅返回有权限列表')
    def _business_data_section_list_projectId(self, item_fixture, projectId):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/business/data/section-list/{projectId}'
        response = item_fixture.request('get', resource)
        return response

    @allure.step('项目列表，仅返回有权限列表')
    def _business_data_project_list(self, item_fixture):
        '''
        
        :param item_fixture: item fixture,
        '''
        resource = f'/business/data/project-list'
        response = item_fixture.request('get', resource)
        return response


