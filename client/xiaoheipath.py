# -*- coding: utf-8-*-
import os
# Dingdang main directory
APP_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))

DATA_PATH = os.path.join(APP_PATH, "static")
LIB_PATH = os.path.join(APP_PATH, "client")
LOGIN_PATH = os.path.join(APP_PATH, "login")
TEMP_PATH = os.path.join(APP_PATH, "temp")
PLUGIN_PATH = os.path.join(LIB_PATH, "plugins")

CONFIG_PATH = os.path.expanduser(
    os.getenv('XIAOHEI_CONFIG', '~/.xiaohei')
)
CONTRIB_PATH = os.path.expanduser(
    os.getenv('XIAOHEI_CONFIG', '~/.xiaohei/contrib')
)
CUSTOM_PATH = os.path.expanduser(
    os.getenv('XIAOHEI_CONFIG', '~/.xiaohei/custom')
)


def config(*fname):
    return os.path.join(CONFIG_PATH, *fname)


def data(*fname):
    return os.path.join(DATA_PATH, *fname)
