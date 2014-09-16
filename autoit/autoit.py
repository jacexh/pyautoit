# -*- coding: utf-8 -*-

__author__ = 'Jace Xu'

import ctypes
import os
import platform
from ctypes.wintypes import *

dll = "AutoItX3.dll"
bit, _ = platform.architecture()

if "(x86)" in os.environ['PROGRAMFILES'] and bit == "64bit":
    # if 64bit version of python within 64bit version of Windows,
    # load AutoItX3_x64.dll
    dll = "AutoItX3_x64.dll"

dll_path = os.path.join(os.path.dirname(__file__), "lib", dll)

if not os.path.exists(dll_path):
    raise IOError("Cannot load AutoItX from path: %s" % dll_path)

AUTO_IT = ctypes.windll.LoadLibrary(dll_path)


class ProcessError(Exception):
    pass


class TimeoutError(Exception):
    pass


class OptionError(Exception):
    pass


class WindowError(Exception):
    pass


def get_error():
    return AUTO_IT.AU3_error()


def auto_it_set_option(option, param):
    """
    Changes the operation of various AutoIt functions/parameters
    :param option: The option to change
    :param param: The parameter (varies by option).
    :return:
    """
    pre_value = AUTO_IT.AU3_AutoItSetOption(LPCWSTR(option), INT(param))
    return pre_value


class Properties(object):
    """
    Below is an list of all the properties available in AutoItX.
    """
    SW_HIDE = 0
    SW_MAXIMIZE = 3
    SW_MINIMIZE = 6
    SW_RESTORE = 9
    SW_SHOW = 5
    SW_SHOWDEFAULT = 10
    SW_SHOWMAXIMIZED = 3
    SW_SHOWMINIMIZED = 2
    SW_SHOWMINNOACTIVE = 7
    SW_SHOWNA = 8
    SW_SHOWNOACTIVATE = 4
    SW_SHOWNORMAL = 1


class _Options(object):

    def __init__(self):
        self._caret_coord_mode = 1
        self._mouse_click_delay = 10
        self._mouse_click_down_delay = 10
        self._mouse_click_drag_delay = 250
        self._mouse_coord_mode = 1
        self._pixel_coord_mode = 1
        self._send_attach_mode = 0
        self._send_capslock_mode = 1
        self._send_key_delay = 5
        self._send_key_down_delay = 10
        self._win_detect_hidden_text = 0
        self._win_search_children = 0
        self._win_text_match_mode = 1
        self._win_title_match_mode = 1
        self._win_wait_delay = 250

    @property
    def caret_coord_mode(self):
        return self._caret_coord_mode

    @caret_coord_mode.setter
    def caret_coord_mode(self, value):
        auto_it_set_option("CaretCoordMode", value)
        self._caret_coord_mode = value

    @property
    def mouse_click_delay(self):
        return self._mouse_click_delay

    @mouse_click_delay.setter
    def mouse_click_delay(self, value):
        auto_it_set_option("MouseClickDelay", value)
        self._mouse_click_delay = value

    @property
    def mouse_click_down_delay(self):
        return self._mouse_click_down_delay

    @mouse_click_down_delay.setter
    def mouse_click_down_delay(self, value):
        auto_it_set_option("MouseClickDownDelay", value)
        self._mouse_click_down_delay = value

    @property
    def mouse_click_drag_delay(self):
        return self._mouse_click_drag_delay

    @mouse_click_drag_delay.setter
    def mouse_click_drag_delay(self, value):
        auto_it_set_option("MouseClickDragDelay", value)
        self._mouse_click_drag_delay = value

    @property
    def mouse_coord_mode(self):
        return self._mouse_coord_mode

    @mouse_coord_mode.setter
    def mouse_coord_mode(self, value):
        auto_it_set_option("MouseCoordMode", value)
        self._mouse_coord_mode = value

    @property
    def pixel_coord_mode(self):
        return self._pixel_coord_mode

    @pixel_coord_mode.setter
    def pixel_coord_mode(self, value):
        auto_it_set_option("PixelCoordMode", value)
        self._pixel_coord_mode = value

    @property
    def send_attach_mode(self):
        return self._send_attach_mode

    @send_attach_mode.setter
    def send_attach_mode(self, value):
        auto_it_set_option("SendAttachMode", INT(value))
        self._send_attach_mode = value

    @property
    def send_capslock_mode(self):
        return self._send_capslock_mode

    @send_capslock_mode.setter
    def send_capslock_mode(self, value):
        auto_it_set_option("SendCapslockMode", value)
        self._send_capslock_mode = value

    @property
    def send_key_delay(self):
        return self._send_key_delay

    @send_key_delay.setter
    def send_key_delay(self, value):
        auto_it_set_option("SendKeyDelay", value)
        self._send_key_delay = value

    @property
    def send_key_down_delay(self):
        return self._send_key_down_delay

    @send_key_down_delay.setter
    def send_key_down_delay(self, value):
        auto_it_set_option("SendKeyDownDelay", value)
        self._send_key_down_delay = value

    @property
    def win_detect_hidden_text(self):
        return self._win_detect_hidden_text

    @win_detect_hidden_text.setter
    def win_detect_hidden_text(self, value):
        auto_it_set_option("WinDetectHiddenText", value)
        self._win_detect_hidden_text = value

    @property
    def win_search_children(self):
        return self._win_search_children

    @win_search_children.setter
    def win_search_children(self, value):
        auto_it_set_option("WinSearchChildren", value)
        self._win_search_children = value

    @property
    def win_text_match_mode(self):
        return self._win_text_match_mode

    @win_text_match_mode.setter
    def win_text_match_mode(self, value):
        auto_it_set_option("WinTextMatchMode", value)
        self._win_text_match_mode = value

    @property
    def win_title_match_mode(self):
        return self._win_title_match_mode

    @win_title_match_mode.setter
    def win_title_match_mode(self, value):
        auto_it_set_option("WinTitleMatchMode", value)
        self._win_title_match_mode = value

    @property
    def win_wait_delay(self):
        return self._win_wait_delay

    @win_wait_delay.setter
    def win_wait_delay(self, value):
        auto_it_set_option("WinWaitDelay", value)
        self._win_wait_delay = value

Options = _Options()
