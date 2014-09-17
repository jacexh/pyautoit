# -*- coding: utf-8 -*-

__author__ = 'Jace Xu'
__version__ = "0.1"

from .autoit import options, properties, error

from .process import run
from .process import run_wait
from .process import process_close
from .process import process_exists
from .process import process_set_priority
from .process import process_wait
from .process import process_wait_close
from .process import run_as
from .process import run_as_wait
from .process import shutdown

from .win import win_activate
from .win import win_activate_by_handle
from .win import win_active
from .win import win_active_by_handle
from .win import win_close
from .win import win_close_by_handle
from .win import win_exists
from .win import win_exists_by_handle
from .win import win_get_caret_pos
from .win import win_get_class_list
from .win import win_get_class_list_by_handle
from .win import win_get_client_size
from .win import win_get_client_size_by_handle
from .win import win_get_handle
from .win import win_get_handle_as_text
from .win import win_get_pos
from .win import win_get_pos_by_handle
from .win import win_get_process
from .win import win_get_process_by_handle
from .win import win_get_state
from .win import win_get_state_by_handle
from .win import win_get_text
from .win import win_get_text_by_handle
from .win import win_get_title
from .win import win_get_title_by_handle
from .win import win_kill
from .win import win_kill_by_handle
from .win import win_menu_select_item
from .win import win_menu_select_item_by_handle
from .win import win_minimize_all
from .win import win_minimize_all_undo
from .win import win_move
from .win import win_move_by_handle
from .win import win_set_on_top
from .win import win_set_on_top_by_handle
from .win import win_set_state
from .win import win_set_state_by_handle
from .win import win_set_title
from .win import win_set_title_by_handle
from .win import win_set_trans
from .win import win_set_trans_by_handle
from .win import win_wait
from .win import win_wait_by_handle
from .win import win_wait_active
from .win import win_wait_active_by_handle
from .win import win_wait_close
from .win import win_wait_close_by_handle
from .win import win_wait_not_active
from .win import win_wait_not_active_by_handle