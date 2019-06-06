# -*- coding: utf-8 -*-

__author__ = 'Jace Xu'

from .autoit import AUTO_IT
from .autoit import api
from .autoit import AutoItError
from ctypes.wintypes import *
from ctypes import create_unicode_buffer, byref
from .autoit import properties


@api.check(2, "activate window failed, maybe the window doesn't exist")
def win_activate(title, **kwargs):
    """
    Activates (gives focus to) a window.
    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinActivate(LPCWSTR(title), LPCWSTR(text))
    return ret


@api.check(2, "activate window failed, maybe the window doesn't exist")
def win_activate_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinActivateByHandle(HWND(handle))
    return ret


def win_active(title, **kwargs):
    """

    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinActive(LPCWSTR(title), LPCWSTR(text))
    return ret


def win_active_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinActiveByHandle(HWND(handle))
    return ret


@api.check(2, "close this window failed, maybe the window doesn't exist")
def win_close(title, **kwargs):
    """

    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinClose(LPCWSTR(title), LPCWSTR(text))
    return ret


@api.check(2, "close window failed, maybe the window does not exist")
def win_close_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinCloseByHandle(HWND(handle))
    return ret


def win_exists(title, **kwargs):
    """
    Checks to see if a specified window exists.
    :param title: The title of the window to check.
    :param text: The text of the window to check.
    :return: Returns 1 if the window exists, otherwise returns 0.
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinExists(LPCWSTR(title), LPCWSTR(text))
    return ret


def win_exists_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinExistsByHandle(HWND(handle))
    return ret


@api.check(1, "get the coordinates of the caret failed")
def win_get_caret_pos():
    """
    Returns the coordinates of the caret in the foreground window
    :return:
    """
    p = POINT()
    AUTO_IT.AU3_WinGetCaretPos(byref(p))
    return p.x, p.y


def win_get_class_list(title, buf_size=200, **kwargs):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    text = kwargs.get("text", "")
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


def win_get_client_size(title, **kwargs):
    """

    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
    rect = RECT()

    ret = AUTO_IT.AU3_WinGetClientSize(LPCWSTR(title), LPCWSTR(text),
                                       byref(rect))
    if ret == 1:
        raise AutoItError(
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
        raise AutoItError("get the size of client failed")
    return rect.right, rect.bottom


@api.check(3, "No window match the criteria")
def win_get_handle(title, **kwargs):
    """

    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinGetHandle(LPCWSTR(title), LPCWSTR(text))
    return ret


@api.check(1, "No window match the criteria")
def win_get_handle_as_text(title, buf_size=16, **kwargs):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    text = kwargs.get("text", "")
    rec_text = create_unicode_buffer(buf_size)
    AUTO_IT.AU3_WinGetHandleAsText(LPCWSTR(title), LPCWSTR(text),
                                   rec_text, INT(buf_size))
    msg = rec_text.value
    return msg


def win_get_pos(title, **kwargs):
    """

    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
    rect = RECT()
    res = AUTO_IT.AU3_WinGetPos(LPCWSTR(title), LPCWSTR(text), byref(rect))
    if res == 1:
        raise AutoItError("No window match the criteria")
    return rect.left, rect.top, rect.right, rect.bottom


def win_get_pos_by_handle(handle):
    """

    :param handle:
    :return:
    """
    rect = RECT()
    res = AUTO_IT.AU3_WinGetPosByHandle(HWND(handle), byref(rect))
    if res == 1:
        raise AutoItError("No window match the handle: %s" % str(handle))
    return rect.left, rect.top, rect.right, rect.bottom


@api.check(2, "No window match the criteria", unexpected_ret=(-1,))
def win_get_process(title, **kwargs):
    """

    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
    res = AUTO_IT.AU3_WinGetProcess(LPCWSTR(title), LPCWSTR(text))
    return res


@api.check(2, "No window match the criteria", unexpected_ret=(-1,))
def win_get_process_by_handle(handle):
    """

    :param handle:
    :return:
    """
    res = AUTO_IT.AU3_WinGetProcessByHandle(HWND(handle))
    return res


@api.check(2, "No window match the criteria")
def win_get_state(title, **kwargs):
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
    text = kwargs.get("text", "")
    res = AUTO_IT.AU3_WinGetState(LPCWSTR(title), LPCWSTR(text))
    return res


@api.check(2, "No window match the criteria")
def win_get_state_by_handle(handle):
    """

    :param handle:
    :return:
    """
    res = AUTO_IT.AU3_WinGetStateByHandle(HWND(handle))
    return res


def win_get_text(title, buf_size=256, **kwargs):
    """

    :param title:
    :param text:
    :param buf_size:
    :return:
    """
    text = kwargs.get("text", "")
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


def win_get_title(title, buf_size=256, **kwargs):
    """

    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
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


@api.check(2, "No window match the criteria")
def win_kill(title, **kwargs):
    """

    :param title:
    :param text:
    :return:
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinKill(LPCWSTR(title), LPCWSTR(text))
    return ret


@api.check(2, "No window match the criteria")
def win_kill_by_handle(handle):
    """

    :param handle:
    :return:
    """
    ret = AUTO_IT.AU3_WinKillByHandle(HWND(handle))
    return ret


@api.check(2, "the menu item could not be found")
def win_menu_select_item(title, *items, **kwargs):
    """
    Usage:
        win_menu_select_item("[CLASS:Notepad]", "", u"文件(&F)", u"退出(&X)")
    :param title:
    :param text:
    :param items:
    :return:
    """
    text = kwargs.get("text", "")
    if not (0 < len(items) < 8):
        raise ValueError("accepted none item or number of items exceed eight")
    f_items = [LPCWSTR(item) for item in items]
    for i in range(8 - len(f_items)):
        f_items.append(LPCWSTR(""))

    ret = AUTO_IT.AU3_WinMenuSelectItem(LPCWSTR(title), LPCWSTR(text),
                                        *f_items)
    return ret


@api.check(2, "the menu item could not be found")
def win_menu_select_item_by_handle(handle, *items):
    """

    :param handle:
    :param items:
    :return:
    """
    if not (0 < len(items) < 8):
        raise ValueError("accepted none item or number of items exceed eight")
    f_items = [LPCWSTR(item) for item in items]
    for i in range(8 - len(f_items)):
        f_items.append(LPCWSTR(""))

    ret = AUTO_IT.AU3_WinMenuSelectItemByHandle(HWND(handle), *f_items)
    return ret


def win_minimize_all():
    """

    :return:
    """
    AUTO_IT.AU3_WinMinimizeAll()


def win_minimize_all_undo():
    """

    :return:
    """
    AUTO_IT.AU3_WinMinimizeAllUndo()


@api.check(2, "No window match the criteria")
def win_move(title, x, y, width=-1, height=-1, **kwargs):
    """

    :param title:
    :param text:
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinMove(LPCWSTR(title), LPCWSTR(text), INT(x), INT(y),
                              INT(width), INT(height))
    return ret


@api.check(2, "No window match the criteria")
def win_move_by_handle(handle, x, y, width=-1, height=-1):
    """

    :param handle:
    :param x:
    :param y:
    :param width:
    :param height:
    :return:
    """
    ret = AUTO_IT.AU3_WinMoveByHandle(HWND(handle), INT(x), INT(y), INT(width),
                                      INT(height))
    return ret


@api.check(2, "No window match the criteria")
def win_set_on_top(title, flag=1, **kwargs):
    """

    :param title:
    :param flag: 1=set on top flag, 0 = remove on top flag
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_WinSetOnTop(LPCWSTR(title), LPCWSTR(text), INT(flag))
    return ret


@api.check(2, "No window match the criteria")
def win_set_on_top_by_handle(handle, flag=1):
    """

    :param handle:
    :param flag:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetOnTopByHandle(HWND(handle), INT(flag))
    return ret


@api.check(2, "No window match the criteria")
def win_set_state(title, flag=properties.SW_SHOW, **kwargs):
    """

    :param title:
    :param flag: The "show" flag of the executed program:
        SW_HIDE = Hide window
        SW_SHOW = Shows a previously hidden window
        SW_MINIMIZE = Minimize window
        SW_MAXIMIZE = Maximize window
        SW_RESTORE = Undoes a window minimization or maximization
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_WinSetState(LPCWSTR(title), LPCWSTR(text), INT(flag))
    return ret


@api.check(2, "No window match the criteria")
def win_set_state_by_handle(handle, flag=properties.SW_SHOW):
    """

    :param handle:
    :param flag:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetStateByHandle(HWND(handle), INT(flag))
    return ret


@api.check(2, "No window match the criteria")
def win_set_title(title, new_title, **kwargs):
    """

    :param title:
    :param new_title:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinSetTitle(LPCWSTR(title), LPCWSTR(text),
                                  LPCWSTR(new_title))
    return ret


@api.check(2, "No window match the criteria")
def win_set_title_by_handle(handle, new_title):
    """

    :param handle:
    :param new_title:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetTitleByHandle(HWND(handle), LPCWSTR(new_title))
    return ret


@api.check(2, "No window match the criteria")
def win_set_trans(title, trans, **kwargs):
    """
    Sets the transparency of a window.
    :param title:
    :param trans: A number in the range 0 - 255. The larger the number,
        the more transparent the window will become.
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_WinSetTrans(LPCWSTR(title), LPCWSTR(text), INT(trans))
    return ret


@api.check(2, "No window match the criteria")
def win_set_trans_by_handle(handle, trans):
    """

    :param handle:
    :param trans:
    :return:
    """
    ret = AUTO_IT.AU3_WinSetTransByHandle(HWND(handle), INT(trans))
    return ret


@api.check(2, "timeout on wait for window exists")
def win_wait(title, timeout=0, **kwargs):
    """

    :param title:
    :param timeout:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_WinWait(LPCWSTR(title), LPCWSTR(text), INT(timeout))
    return ret


@api.check(2, "timeout on wait for window exists")
def win_wait_by_handle(handle, timeout):
    """

    :param handle:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitByHandle(HWND(handle), INT(timeout))
    return ret


@api.check(2, "timeout on wait for activate window")
def win_wait_active(title, timeout=0, **kwargs):
    """

    :param title:
    :param timeout:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_WinWaitActive(LPCWSTR(title), LPCWSTR(text),
                                    INT(timeout))
    return ret


@api.check(2, "timeout on wait for activate window")
def win_wait_active_by_handle(handle, timeout):
    """

    :param handle:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitActiveByHandle(HWND(handle), INT(timeout))
    return ret


@api.check(2, "timeout on wait for close window")
def win_wait_close(title, timeout=0, **kwargs):
    """

    :param title:
    :param timeout:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")
    ret = AUTO_IT.AU3_WinWaitClose(LPCWSTR(title), LPCWSTR(text), INT(timeout))
    return ret


@api.check(2, "timeout on wait for close window")
def win_wait_close_by_handle(handle, timeout):
    """

    :param handle:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitCloseByHandle(HWND(handle), INT(timeout))
    return ret


@api.check(2, "timeout on wait for deactivate window")
def win_wait_not_active(title, timeout=0, **kwargs):
    """

    :param title:
    :param timeout:
    :param kwargs:
    :return:
    """
    text = kwargs.get("text", "")

    ret = AUTO_IT.AU3_WinWaitNotActive(LPCWSTR(title), LPCWSTR(text),
                                       INT(timeout))
    return ret


@api.check(2, "timeout on wait for deactivate window")
def win_wait_not_active_by_handle(handle, timeout):
    """

    :param handle:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_WinWaitNotActiveByHandle(HWND(handle), INT(timeout))
    return ret
