# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""


class SERVICETESTHandler(object):

    def __init__(self):
        pass

    def file_change_callback(self, file_list, service_instance):
        print file_list
        return

    def after_watch_callback(self, file_list, service_instance):
        print file_list
        return

    def before_watch_callback(self, service_instance):
        pass

