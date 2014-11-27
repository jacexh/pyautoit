# -*- coding: utf-8 -*-

__author__ = 'Jace Xu'

from .autoit import AUTO_IT
from .autoit import api, error
from .autoit import Properties
from .autoit import AutoItError
from ctypes.wintypes import *


@api.check(1, "run program failed")
def run(filename, work_dir="", show_flag=Properties.SW_SHOWNORMAL):
    """

    :param filename:
    :param work_dir:
    :param show_flag:
    :return:
    """
    ret = AUTO_IT.AU3_Run(LPCWSTR(filename), LPCWSTR(work_dir),
                          INT(show_flag))
    return ret


@api.check(1, "run program failed")
def run_wait(filename, work_dir="", show_flag=Properties.SW_SHOWNORMAL):
    """

    :param filename:
    :param work_dir:
    :param show_flag:
    :return:
    """
    ret = AUTO_IT.AU3_RunWait(LPCWSTR(filename), LPCWSTR(work_dir),
                              INT(show_flag))
    return ret


def process_close(process):
    """
    Terminates a named process.
    """
    ret = AUTO_IT.AU3_ProcessClose(LPCWSTR(process))
    return ret


def process_exists(process):
    """

    :param process:
    :return:
    """
    ret = AUTO_IT.AU3_ProcessExists(LPCWSTR(process))
    return ret


def process_set_priority(process, priority):
    """
    Changes the priority of a process
    :param process: The name or PID of the process to check.
    :param priority:A flag which determines what priority to set
        0 - Idle/Low
        1 - Below Normal (Not supported on Windows 95/98/ME)
        2 - Normal
        3 - Above Normal (Not supported on Windows 95/98/ME)
        4 - High
        5 - Realtime (Use with caution, may make the system unstable)
    :return:
    """
    ret = AUTO_IT.AU3_ProcessSetPriority(LPCWSTR(process), INT(priority))
    if ret == 0:
        if error() == 1:
            raise AutoItError("set priority failed")
        elif error() == 2:
            raise AutoItError("unsupported priority class be used")
    return ret


@api.check(2, "the process wait timed out")
def process_wait(process, timeout=0):
    """
    Pauses script execution until a given process exists.
    :param process:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_ProcessWait(LPCWSTR(process), INT(timeout))
    return ret


@api.check(2, "the process wait close timed out")
def process_wait_close(process, timeout=0):
    """
    Pauses script execution until a given process does not exist.
    :param process:
    :param timeout:
    :return:
    """
    ret = AUTO_IT.AU3_ProcessWaitClose(LPCWSTR(process), INT(timeout))
    return ret


@api.check(1, "run an external program failed")
def run_as(user, domain, password, filename, logon_flag=1, work_dir="",
           show_flag=Properties.SW_SHOWNORMAL):
    """
    Runs an external program.
    :param user: username The user name to use.
    :param domain: The domain name to use.
    :param password: The password to use.
    :param logon_flag: 0 = do not load the user profile, 1 = (default) load
        the user profile, 2 = use for net credentials only
    :param filename: The name of the executable (EXE, BAT, COM, or PIF) to run.
    :param work_dir: The working directory.
    :param show_flag: The "show" flag of the executed program:
        SW_HIDE = Hidden window
        SW_MINIMIZE = Minimized window
        SW_MAXIMIZE = Maximized window
    :return:
    """
    ret = AUTO_IT.AU3_RunAs(
        LPCWSTR(user), LPCWSTR(domain), LPCWSTR(password), INT(logon_flag),
        LPCWSTR(filename), LPCWSTR(work_dir), INT(show_flag)
    )
    return ret


@api.check(1, "run an external program failed")
def run_as_wait(user, domain, password, filename, logon_flag=1, work_dir="",
                show_flag=Properties.SW_SHOWNORMAL):
    """
    Runs an external program.
    :param user: username The user name to use.
    :param domain: The domain name to use.
    :param password: The password to use.
    :param logon_flag: 0 = do not load the user profile, 1 = (default) load
        the user profile, 2 = use for net credentials only
    :param filename: The name of the executable (EXE, BAT, COM, or PIF) to run.
    :param work_dir: The working directory.
    :param show_flag: The "show" flag of the executed program:
        SW_HIDE = Hidden window
        SW_MINIMIZE = Minimized window
        SW_MAXIMIZE = Maximized window
    :return:
    """
    ret = AUTO_IT.AU3_RunAsWait(
        LPCWSTR(user), LPCWSTR(domain), LPCWSTR(password), INT(logon_flag),
        LPCWSTR(filename), LPCWSTR(work_dir), INT(show_flag)
    )
    return ret


@api.check(2, "set shutdown failed")
def shutdown(code):
    """

    :param code: The shutdown code is a combination of the following values:
        0 = Logoff
        1 = Shutdown
        2 = Reboot
        4 = Force
        8 = Power down
    :return:
    """
    ret = AUTO_IT.AU3_Shutdown(INT(code))
    return ret