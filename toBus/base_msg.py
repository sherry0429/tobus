# -*- coding: utf-8 -*-

"""
Copyright (C) 2017 tianyou pan <sherry0429 at SOAPython>
"""


class BaseMessage(object):

    msg_id = None
    direction = list()
    # notice direction and publish modules only exists one,
    # if both of them is not None, toBus will use publish_modules
    publish_module_type = None
    before = None  # string
    content = None
    return_code = None

