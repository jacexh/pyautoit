# -*- coding: utf-8 -*-

__author__ = 'Jace Xu'

from autoit import AUTO_IT
from autoit import get_error
from autoit import WindowError
from ctypes.wintypes import *
from ctypes import create_unicode_buffer, byref


def win_activate(title, text=""):
    """
    Activates (gives focus to) a window.
    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinActivate(LPCWSTR(title), LPCWSTR(text))
    if ret == 0:
        raise WindowError(
            "activate window failed, maybe the window does not exist")
    return ret


def win_activate_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinActivateByHandle(HWND(handle))
    if ret == 0:
        raise WindowError(
            "activate window by handle failed, maybe the window "
            "does not exist")
    return ret


def win_active(title, text=""):
    """

    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinActive(LPCWSTR(title), LPCWSTR(text))
    return ret


def win_active_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinActiveByHandle(HWND(handle))
    return ret


def win_close(title, text=""):
    """

    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinClose(LPCWSTR(title), LPCWSTR(text))
    if ret == 0:
        raise WindowError(
            "close this window failed, maybe the window does not exist")
    return ret


def win_close_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinCloseByHandle(HWND(handle))
    if ret == 0:
        raise WindowError(
            "close window failed, maybe the window does not exist"
        )
    return ret


def win_exists(title, text=""):
    """
    Checks to see if a specified window exists.
    :param title: The title of the window to check.
    :param text: The text of the window to check.
    :return: Returns 1 if the window exists, otherwise returns 0.
    """
    ret = AUTO_IT.AU3_WinExists(LPCWSTR(title), LPCWSTR(text))
    return ret


def win_exists_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinExistsByHandle(HWND(handle))
    return ret


def win_get_caret_pos():
    """
    Returns the coordinates of the caret in the foreground window
    :return:
    """
    p = POINT()
    AUTO_IT.AU3_WinGetCaretPos(byref(p))
    if get_error() == 1:
        raise WindowError("get the coordinates of the caret failed")
    return p.x, p.y


def win_get_class_list(title, text="", buf_size=200):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    rec_text = create_unicode_buffer(buf_size)  # ...
    AUTO_IT.AU3_WinGetClassList(LPCWSTR(title), LPCWSTR(text),
                                rec_text, INT(buf_size))

    msg = rec_text.value.rstrip()
    return msg


def win_get_class_list_by_handle(handle, buf_size=200):
    """

    :param handle:
    :param buf_size:
    :return:
    """

    rec_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetClassListByHandle(HWND(handle), rec_text, INT(buf_size))

    msg = rec_text.value.rstrip()
    return msg


def win_get_client_size(title, text=""):
    """

    :param title:
    :param text:
    :return:
    """
    rect = RECT()

    ret = AUTO_IT.AU3_WinGetClientSize(LPCWSTR(title), LPCWSTR(text),
                                       byref(rect))
    if ret == 1:
        raise WindowError(
            "get the size of client failed")
    return rect.right, rect.bottom


def win_get_client_size_by_handle(handle):
    """

    :param handle:
    :return:
    """
    rect = RECT()
    ret = AUTO_IT.AU3_WinGetClientSizeByHandle(HWND(handle), byref(rect))
    if ret == 1:
        raise WindowError("get the size of client failed")
    return rect.right, rect.bottom


def win_get_handle(title, text=""):
    """

    :param title:
    :param text:
    :return:
    """
    ret = AUTO_IT.AU3_WinGetHandle(LPCWSTR(title), LPCWSTR(text))
    if ret == 0 and get_error() == 1:
        raise WindowError("No window match the criteria")
    return ret


def win_get_handle_as_text(title, text="", buf_size=16):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    rec_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetHandleAsText(LPCWSTR(title), LPCWSTR(text),
                                   rec_text, INT(buf_size))
    if get_error() == 1:
        raise WindowError("No window match the criteria")
    msg = rec_text.value
    return msg


def win_get_pos(title, text=""):
    """

    :param title:
    :param text:
    :return:
    """
    rect = RECT()
    res = AUTO_IT.AU3_WinGetPos(LPCWSTR(title), LPCWSTR(text), byref(rect))
    if res == 1:
        raise WindowError("No window match the criteria")
    return rect.left, rect.top, rect.right, rect.bottom


def win_get_pos_by_handle(handle):
    """

    :param handle:
    :return:
    """
    rect = RECT()
    res = AUTO_IT.AU3_WinGetPosByHandle(HWND(handle), byref(rect))
    if res == 1:
        raise WindowError("No window match the handle: %s" % str(handle))
    return rect.left, rect.top, rect.right, rect.bottom


def win_get_process(title, text=""):
    """

    :param title:
    :param text:
    :return:
    """
    res = AUTO_IT.AU3_WinGetProcess(LPCWSTR(title), LPCWSTR(text))
    if res == -1:
        raise WindowError(
            "No window match the criteria: \n    Title: %s\n    Text: %s" %
            (str(title), str(text)))
    return res


def win_get_process_by_handle(handle):
    """

    :param handle:
    :return:
    """
    res = AUTO_IT.AU3_WinGetProcessByHandle(HWND(handle))
    if res == -1:
        raise WindowError(
            "No window match the criteria:\n    Handle: %s" % str(handle))
    return res


def win_get_state(title, text=""):
    """
    Retrieves the state of a given window.
    :param title:
    :param text:
    :return:
    1 = Window exists
    2 = Window is visible
    4 = Windows is enabled
    8 = Window is active
    16 = Window is minimized
    32 = Windows is maximized
    """
    res = AUTO_IT.AU3_WinGetState(LPCWSTR(title), LPCWSTR(text))
    if res == 0:
        raise WindowError(
            "No window match the criteria: \n    Title: %s\n    Text: %s" %
            (str(title), str(text)))
    return res


def win_get_state_by_handle(handle):
    """

    :param handle:
    :return:
    """
    res = AUTO_IT.AU3_WinGetStateByHandle(HWND(handle))
    if res == 0:
        raise WindowError(
            "No window match the criteria:\n    Handle: %s" % str(handle))
    return res


def win_get_text(title, text="", buf_size=256):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    ret_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetText(LPCWSTR(title), LPCWSTR(text), ret_text,
                           INT(buf_size))
    val = ret_text.value.rstrip()
    return val


def win_get_text_by_handle(handle, buf_size=256):
    """

    :param handle:
    :return:
    """
    ret_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetTextByHandle(HWND(handle), ret_text, INT(buf_size))
    return ret_text.value.rstrip()


def win_get_title(title, text="", buf_size=256):
    """

    :param title:
    :param text:
    :return:
    """
    ret_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetTitle(LPCWSTR(title), LPCWSTR(text), ret_text,
                            INT(buf_size))
    val = ret_text.value.rstrip()
    return val


def win_get_title_by_handle(handle, buf_size=256):
    """

    :param handle:
    :param buf_size:
    :return:
    """
    ret_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetTitleByHandle(HWND(handle), ret_text, INT(buf_size))
    val = ret_text.value.rstrip()
    return val
