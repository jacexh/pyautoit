# -*- coding: utf-8 -*-

__author__ = 'Jace Xu'

from autoit import INTDEFAULT, AUTO_IT, ControlError, WindowError
from autoit import commands, error
from ctypes.wintypes import *
import ctypes


def control_click(title, control, **kwargs):
    """

    :param title:
    :param text:
    :param control:
    :param button:
    :param clicks:
    :param x:
    :param y:
    :return:
    """
    text = kwargs.get("text", "")
    button = kwargs.get("button", "left")
    clicks = kwargs.get("clicks", 1)
    x = kwargs.get("x", INTDEFAULT)
    y = kwargs.get("y", INTDEFAULT)

    ret = AUTO_IT.AU3_ControlClick(LPCWSTR(title), LPCWSTR(text),
                                   LPCWSTR(control), LPCWSTR(button),
                                   INT(clicks), INT(x), INT(y))
    if ret == 0:
        raise ControlError("send click message failed")
    return ret


def control_click_by_handle(hwnd, h_ctrl, **kwargs):
    """

    :param handle:
    :param kwargs:
    :return:
    """
    button = kwargs.get("button", "left")
    clicks = kwargs.get("clicks", 1)
    x = kwargs.get("x", INTDEFAULT)
    y = kwargs.get("y", INTDEFAULT)

    ret = AUTO_IT.AU3_ControlClickByHandle(HWND(hwnd), HWND(h_ctrl),
                                           LPCWSTR(button), INT(clicks),
                                           INT(x), INT(y))

    if ret == 0:
        raise ControlError("send click message failed")
    return ret


def control_command(title, control, command, buf_size=256, **kwargs):
    """

    :param title:
    :param control:
    :param command:
    :param extra:
    :param buf_size:
    :return:
    """
    text = kwargs.get("text", "")
    extra = kwargs.get("extra", "")
    result = ctypes.create_unicode_buffer(buf_size)
    AUTO_IT.AU3_ControlCommand(LPCWSTR(title), LPCWSTR(text), LPCWSTR(control),
                               LPCWSTR(command), LPCWSTR(extra),
                               result, INT(buf_size))

    if error() == 1:
        raise ControlError("an error occurred, may no window "
                           "match the criteria")
    return result.value.rstrip()


def control_command_by_handle(hwnd, h_ctrl, command, buf_size=256, **kwargs):
    """

    :param hwnd:
    :param h_ctrl:
    :param command:
    :param kwargs:
    :return:
    """
    extra = kwargs.get("extra", "")
    result = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_ControlCommandByHandle(
        HWND(hwnd), HWND(h_ctrl), LPCWSTR(command), LPCWSTR(extra), result,
        INT(buf_size))

    if error() == 1:
        raise ControlError("an error occurred when send command: %s"
                           % commands)
    return result.value.rstrip()


def control_list_view(title, control, command, **kwargs):
    """

    :param title:
    :param control:
    :param command:
    :param args:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")
    buf_size = kwargs.get("buf_size", 256)
    result = ctypes.create_unicode_buffer(buf_size)
    extra1 = kwargs.get("extras1", "")
    extra2 = kwargs.get("extras2", "")

    AUTO_IT.AU3_ControlListView(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(command),
        LPCWSTR(extra1), LPCWSTR(extra2), result, INT(buf_size)
    )

    if error() == 1:
        raise ControlError("Window/Control could not be found")
    return result.value.rstrip()


def control_list_view_by_handle(hwnd, h_ctrl, command, **kwargs):
    """

    :param hwnd:
    :param h_ctrl:
    :param command:
    :param kwargs:
    :return:
    """
    extra1 = kwargs.get("extra1", "")
    extra2 = kwargs.get("extra2", "")
    buf_size = kwargs.get("buf_size", 256)
    result = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_ControlListViewByHandle(
        HWND(hwnd), HWND(h_ctrl), LPCWSTR(command),
        LPCWSTR(extra1), LPCWSTR(extra2), result, INT(buf_size)
    )

    if error() == 1:
        raise ControlError("Window/Control could not be found")
    return result.value.rstrip()


def control_disable(title, control, **kwargs):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_ControlDisable(LPCWSTR(title), LPCWSTR(text),
                                     LPCWSTR(control))
    if ret == 0:
        raise ControlError("disable control failed, "
                           "window/control could not be found")
    return ret


def control_disable_by_handle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlDisableByHandle(HWND(hwnd), HWND(h_ctrl))
    if ret == 0:
        raise ControlError("disable control failed, "
                           "window/control could not be found")
    return ret


def control_enable(title, control, **kwargs):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_ControlEnable(LPCWSTR(title), LPCWSTR(text),
                                    LPCWSTR(control))
    if ret == 0:
        raise ControlError("enable control failed, "
                           "window/control could not be found")
    return ret


def control_enable_by_handle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlEnableByHandle(HWND(hwnd), HWND(h_ctrl))
    if ret == 0:
        raise ControlError("enable control failed, "
                           "window/control could not be found")
    return ret


def control_focus(title, control, **kwargs):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_ControlFocus(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control))
    if ret == 0:
        raise ControlError("set input focus to the given control failed")
    return ret


def control_focus_by_handle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlFocusByHandle(HWND(hwnd), HWND(h_ctrl))
    if ret == 0:
        raise ControlError("set input focus to the given control failed")
    return ret


def control_get_focus(title, **kwargs):
    """

    :param title:
    :param kwargs:
    :return:
    """
    buf_size = kwargs.get("buf_size", 256)
    text = kwargs.get("text", "")
    ctrl_with_focus = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_ControlGetFocus(
        LPCWSTR(title), LPCWSTR(text), ctrl_with_focus, INT(buf_size))

    if error() == 1:
        raise WindowError("the specified window could not be found")
    return ctrl_with_focus.value.rstrip()


def control_get_focus_by_handle(hwnd, buf_size=256):
    """

    :param hwnd:
    :param buf_size:
    :return:
    """
    ctrl_with_focus = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_ControlGetFocusByHandle(HWND(hwnd), ctrl_with_focus,
                                        INT(buf_size))

    if error() == 1:
        raise WindowError("the specified window could not be found")
    return ctrl_with_focus.value.rstrip()


def control_get_handle(hwnd, control):
    """

    :param hwnd:
    :param control:
    :return:
    """
    ret = AUTO_IT.AU3_ControlGetHandle(HWND(hwnd), LPCWSTR(control))

    if error() == 1:
        raise ControlError("No window/control match the criteria")
    return ret


def control_get_handle_as_text(title, control, **kwargs):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")
    buf_size = kwargs.get("buf_size", 32)
    ret_text = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_ControlGetHandleAsText(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control),
        ret_text, INT(buf_size)
    )

    if error() == 1:
        raise ControlError("No window/control match the criteria")
    return ret_text.value.rstrip()


def control_get_pos(title, control, text=""):
    """

    :param title:
    :param control:
    :param text:
    :return:
    """
    rect = RECT()

    AUTO_IT.AU3_ControlGetPos(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control),
        ctypes.byref(rect)
    )

    if error() == 1:
        raise ControlError("No window/control match the criteria")
    return rect.left, rect.top, rect.right, rect.bottom


def control_get_pos_by_handle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    rect = RECT()

    AUTO_IT.AU3_ControlGetPosByHandle(HWND(hwnd), HWND(h_ctrl),
                                      ctypes.byref(rect))

    if error() == 1:
        raise ControlError("No window/control match the criteria")
    return rect.left, rect.top, rect.right, rect.bottom


def control_get_text(title, control, **kwargs):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")
    buf_size = kwargs.get("buf_size", 256)
    ctrl_text = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_ControlGetText(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control),
        ctrl_text, INT(buf_size)
    )

    if error() == 1:
        raise ControlError("No window/control match the criteria")
    return ctrl_text.value.rstrip()


def control_get_text_by_handle(hwnd, h_ctrl, **kwargs):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    buf_size = kwargs.get("buf_size", 256)
    ctrl_text = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_ControlGetTextByHandle(
        HWND(hwnd), HWND(h_ctrl), ctrl_text, INT(buf_size)
    )

    if error() == 1:
        raise ControlError("No window/control match the criteria")
    return ctrl_text.value.rstrip()


def control_hide(title, control, **kwargs):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_ControlHide(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control))
    if ret == 0:
        raise ControlError("hide control failed, "
                           "window/control could not be found")
    return ret


def control_hide_by_handle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlHideByHandle(HWND(hwnd), HWND(h_ctrl))
    if ret == 0:
        raise ControlError("hide control failed, "
                           "window/control could not be found")
    return ret


def control_move(title, control, x, y, width=-1, height=-1, **kwargs):
    """

    :param title:
    :param control:
    :param x:
    :param y:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_ControlMove(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control),
        INT(x), INT(y), INT(width), INT(height)
    )

    if ret == 0:
        raise ControlError("No window/control match the criteria")
    return ret


def control_move_by_handle(hwnd, h_ctrl, x, y, width=-1, height=-1):
    """

    :param hwnd:
    :param h_ctrl:
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    ret = AUTO_IT.AU3_ControlMoveByHandle(
        HWND(hwnd), HWND(h_ctrl), INT(x), INT(y), INT(width), INT(height)
    )
    if ret == 0:
        raise ControlError("No window/control match the criteria")
    return ret


def control_send(title, control, send_text, mode=0, **kwargs):
    """

    :param title:
    :param control:
    :param send_text:
    :param mode:
    flag = 0 (default), Text contains special characters like + to indicate
        SHIFT and {LEFT} to indicate left arrow.
    flag = 1, keys are sent raw.
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_ControlSend(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control),
        LPCWSTR(send_text), INT(mode)
    )

    if ret == 0:
        raise ControlError("no window/control match the criteria")
    return ret


def control_send_by_handle(hwnd, h_ctrl, send_text, mode=0):
    """

    :param hwnd:
    :param h_ctrl:
    :param send_text:
    :param mode:
    :return:
    """

    ret = AUTO_IT.AU3_ControlSendByHandle(
        HWND(hwnd), HWND(h_ctrl), LPCWSTR(send_text), INT(mode)
    )

    if ret == 0:
        raise ControlError("no window/control match the criteria")
    return ret


def control_set_text(title, control, control_text, **kwargs):
    """

    :param title:
    :param control:
    :param control_text:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_ControlSetText(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(control_text)
    )

    if ret == 0:
        raise ControlError("no window/control match the criteria")
    return ret


def control_set_text_by_handle(hwnd, h_ctrl, control_text):
    """

    :param hwnd:
    :param h_ctrl:
    :param control_text:
    :return:
    """
    ret = AUTO_IT.AU3_ControlSetTextByHandle(
        HWND(hwnd), HWND(h_ctrl), LPCWSTR(control_text)
    )
    if ret == 0:
        raise ControlError("no window/control match the criteria")
    return ret


def control_show(title, control, **kwargs):
    """

    :param title:
    :param control:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_ControlShow(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control))
    if ret == 0:
        raise ControlError("show control failed, "
                           "window/control could not be found")
    return ret


def control_show_by_handle(hwnd, h_ctrl):
    """

    :param hwnd:
    :param h_ctrl:
    :return:
    """
    ret = AUTO_IT.AU3_ControlShowByHandle(HWND(hwnd), HWND(h_ctrl))
    if ret == 0:
        raise ControlError("show control failed, "
                           "window/control could not be found")
    return ret


def control_tree_view(title, control, command, **kwargs):
    """

    :param title:
    :param control:
    :param command:
    :param args:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")
    buf_size = kwargs.get("buf_size", 256)
    result = ctypes.create_unicode_buffer(buf_size)
    extra1 = kwargs.get("extras1", "")
    extra2 = kwargs.get("extras2", "")

    AUTO_IT.AU3_ControlTreeView(
        LPCWSTR(title), LPCWSTR(text), LPCWSTR(control), LPCWSTR(command),
        LPCWSTR(extra1), LPCWSTR(extra2), result, INT(buf_size)
    )

    if error() == 1:
        raise ControlError("Window/Control could not be found")
    return result.value.rstrip()


def control_tree_view_by_handle(hwnd, h_ctrl, command, **kwargs):
    """

    :param hwnd:
    :param h_ctrl:
    :param command:
    :param kwargs:
    :return:
    """
    extra1 = kwargs.get("extra1", "")
    extra2 = kwargs.get("extra2", "")
    buf_size = kwargs.get("buf_size", 256)
    result = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_ControlTreeViewByHandle(
        HWND(hwnd), HWND(h_ctrl), LPCWSTR(command),
        LPCWSTR(extra1), LPCWSTR(extra2), result, INT(buf_size)
    )
    if error() == 1:
        raise ControlError("Window/Control could not be found")
    return result.value.rstrip()


def statusbar_get_text(title, text="", part=1, buf_size=256):
    """

    :param title:
    :param text:
    :param part: The "part" number of the status bar to read - the default
        is 1. 1 is the first possible part and usually the one that contains
        the useful messages like "Ready" "Loading...", etc.
    :param buf_size:
    :return:
    """
    sb_text = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_StatusbarGetText(
        LPCWSTR(title), LPCWSTR(text), INT(part), sb_text, INT(buf_size)
    )

    if error() == 1:
        raise ControlError("no text could be read")
    return sb_text.value.rstrip()


def statusbar_get_text_by_handle(hwnd, part=1, buf_size=256):
    """

    :param hwnd:
    :param part:
    :param buf_size:
    :return:
    """
    statusbar_text = ctypes.create_unicode_buffer(buf_size)

    AUTO_IT.AU3_StatusbarGetTextByHandle(
        HWND(hwnd), INT(part), statusbar_text, INT(buf_size)
    )

    if error() == 1:
        raise ControlError("no text could be read")
    return statusbar_text.value.rstrip()