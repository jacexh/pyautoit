#pragma once

///////////////////////////////////////////////////////////////////////////////
//
// AutoItX v3
//
// Copyright (C)1999-2013:
//		- Jonathan Bennett <jon at autoitscript dot com>
//		- See "AUTHORS.txt" for contributors.
//
// This file is part of AutoItX.  Use of this file and the AutoItX DLL is subject
// to the terms of the AutoItX license details of which can be found in the helpfile.
//
// When using the AutoItX3.dll as a standard DLL this file contains the definitions,
// and function declarations required to use the DLL and AutoItX3_DLL.lib file.
//
///////////////////////////////////////////////////////////////////////////////


#ifdef __cplusplus
	#define AU3_API extern "C"
#else
	#define AU3_API
#endif


// Definitions
#define AU3_INTDEFAULT			(-2147483647)	// "Default" value for _some_ int parameters (largest negative number)

//
// nBufSize
// When used for specifying the size of a resulting string buffer this is the number of CHARACTERS
// in that buffer, including the null terminator.  For example:
//
// WCHAR szBuffer[10];
// AU3_ClipGet(szBuffer, 10);
//
// The resulting string will be truncated at 9 characters with the the terminating null in the 10th.
//


///////////////////////////////////////////////////////////////////////////////
// Exported functions
///////////////////////////////////////////////////////////////////////////////

#include <windows.h>

AU3_API void WINAPI AU3_Init(void);
AU3_API int AU3_error(void);

AU3_API int WINAPI AU3_AutoItSetOption(LPCWSTR szOption, int nValue);

AU3_API void WINAPI AU3_ClipGet(LPWSTR szClip, int nBufSize);
AU3_API void WINAPI AU3_ClipPut(LPCWSTR szClip);
AU3_API int WINAPI AU3_ControlClick(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szButton, int nNumClicks, int nX = AU3_INTDEFAULT, int nY = AU3_INTDEFAULT);
AU3_API int WINAPI AU3_ControlClickByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szButton, int nNumClicks, int nX = AU3_INTDEFAULT, int nY = AU3_INTDEFAULT);
AU3_API void WINAPI AU3_ControlCommand(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szCommand, LPCWSTR szExtra, LPWSTR szResult, int nBufSize);
AU3_API void WINAPI AU3_ControlCommandByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra, LPWSTR szResult, int nBufSize);
AU3_API void WINAPI AU3_ControlListView(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPWSTR szResult, int nBufSize);
AU3_API void WINAPI AU3_ControlListViewByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPWSTR szResult, int nBufSize);
AU3_API int WINAPI AU3_ControlDisable(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl);
AU3_API int WINAPI AU3_ControlDisableByHandle(HWND hWnd, HWND hCtrl);
AU3_API int WINAPI AU3_ControlEnable(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl);
AU3_API int WINAPI AU3_ControlEnableByHandle(HWND hWnd, HWND hCtrl);
AU3_API int WINAPI AU3_ControlFocus(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl);
AU3_API int WINAPI AU3_ControlFocusByHandle(HWND hWnd, HWND hCtrl);
AU3_API void WINAPI AU3_ControlGetFocus(LPCWSTR szTitle, LPCWSTR szText, LPWSTR szControlWithFocus, int nBufSize);
AU3_API void WINAPI AU3_ControlGetFocusByHandle(HWND hWnd, LPWSTR szControlWithFocus, int nBufSize);
AU3_API HWND WINAPI AU3_ControlGetHandle(HWND hWnd, LPCWSTR szControl);
AU3_API void WINAPI AU3_ControlGetHandleAsText(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPCWSTR szControl, LPWSTR szRetText, int nBufSize);
AU3_API int WINAPI AU3_ControlGetPos(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPRECT lpRect);
AU3_API int WINAPI AU3_ControlGetPosByHandle(HWND hWnd, HWND hCtrl, LPRECT lpRect);
AU3_API void WINAPI AU3_ControlGetText(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPWSTR szControlText, int nBufSize);
AU3_API void WINAPI AU3_ControlGetTextByHandle(HWND hWnd, HWND hCtrl, LPWSTR szControlText, int nBufSize);
AU3_API int WINAPI AU3_ControlHide(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl);
AU3_API int WINAPI AU3_ControlHideByHandle(HWND hWnd, HWND hCtrl);
AU3_API int WINAPI AU3_ControlMove(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, int nX, int nY, int nWidth = -1, int nHeight = -1);
AU3_API int WINAPI AU3_ControlMoveByHandle(HWND hWnd, HWND hCtrl, int nX, int nY, int nWidth = -1, int nHeight = -1);
AU3_API int WINAPI AU3_ControlSend(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szSendText, int nMode = 0);
AU3_API int WINAPI AU3_ControlSendByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szSendText, int nMode = 0);
AU3_API int WINAPI AU3_ControlSetText(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szControlText);
AU3_API int WINAPI AU3_ControlSetTextByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szControlText);
AU3_API int WINAPI AU3_ControlShow(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl);
AU3_API int WINAPI AU3_ControlShowByHandle(HWND hWnd, HWND hCtrl);
AU3_API void WINAPI AU3_ControlTreeView(LPCWSTR szTitle, LPCWSTR szText, LPCWSTR szControl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPWSTR szResult, int nBufSize);
AU3_API void WINAPI AU3_ControlTreeViewByHandle(HWND hWnd, HWND hCtrl, LPCWSTR szCommand, LPCWSTR szExtra1, LPCWSTR szExtra2, LPWSTR szResult, int nBufSize);

AU3_API void WINAPI AU3_DriveMapAdd(LPCWSTR szDevice, LPCWSTR szShare, int nFlags, /*[in,defaultvalue("")]*/LPCWSTR szUser, /*[in,defaultvalue("")]*/LPCWSTR szPwd, LPWSTR szResult, int nBufSize);
AU3_API int WINAPI AU3_DriveMapDel(LPCWSTR szDevice);
AU3_API void WINAPI AU3_DriveMapGet(LPCWSTR szDevice, LPWSTR szMapping, int nBufSize);

AU3_API int WINAPI AU3_IsAdmin(void);

AU3_API int WINAPI AU3_MouseClick(/*[in,defaultvalue("LEFT")]*/LPCWSTR szButton, int nX = AU3_INTDEFAULT, int nY = AU3_INTDEFAULT, int nClicks = 1, int nSpeed = -1);
AU3_API int WINAPI AU3_MouseClickDrag(LPCWSTR szButton, int nX1, int nY1, int nX2, int nY2, int nSpeed = -1);
AU3_API void WINAPI AU3_MouseDown(/*[in,defaultvalue("LEFT")]*/LPCWSTR szButton);
AU3_API int WINAPI AU3_MouseGetCursor(void);
AU3_API void WINAPI AU3_MouseGetPos(LPPOINT lpPoint);
AU3_API int WINAPI AU3_MouseMove(int nX, int nY, int nSpeed = -1);
AU3_API void WINAPI AU3_MouseUp(/*[in,defaultvalue("LEFT")]*/LPCWSTR szButton);
AU3_API void WINAPI AU3_MouseWheel(LPCWSTR szDirection, int nClicks);

AU3_API int WINAPI AU3_Opt(LPCWSTR szOption, int nValue);

AU3_API unsigned int WINAPI AU3_PixelChecksum(LPRECT lpRect, int nStep = 1);
AU3_API int WINAPI AU3_PixelGetColor(int nX, int nY);
AU3_API void WINAPI AU3_PixelSearch(LPRECT lpRect, int nCol, /*default 0*/int nVar, /*default 1*/int nStep, LPPOINT pPointResult);
AU3_API int WINAPI AU3_ProcessClose(LPCWSTR szProcess);
AU3_API int WINAPI AU3_ProcessExists(LPCWSTR szProcess);
AU3_API int WINAPI AU3_ProcessSetPriority(LPCWSTR szProcess, int nPriority);
AU3_API int WINAPI AU3_ProcessWait(LPCWSTR szProcess, int nTimeout = 0);
AU3_API int WINAPI AU3_ProcessWaitClose(LPCWSTR szProcess, int nTimeout = 0);

AU3_API int WINAPI AU3_Run(LPCWSTR szProgram, /*[in,defaultvalue("")]*/LPCWSTR szDir, int nShowFlag = SW_SHOWNORMAL);
AU3_API int WINAPI AU3_RunWait(LPCWSTR szProgram, /*[in,defaultvalue("")]*/LPCWSTR szDir, int nShowFlag = SW_SHOWNORMAL);
AU3_API int WINAPI AU3_RunAs(LPCWSTR szUser, LPCWSTR szDomain, LPCWSTR szPassword, int nLogonFlag, LPCWSTR szProgram, /*[in,defaultvalue("")]*/LPCWSTR szDir, int nShowFlag = SW_SHOWNORMAL);
AU3_API int WINAPI AU3_RunAsWait(LPCWSTR szUser, LPCWSTR szDomain, LPCWSTR szPassword, int nLogonFlag, LPCWSTR szProgram, /*[in,defaultvalue("")]*/LPCWSTR szDir, int nShowFlag = SW_SHOWNORMAL);

AU3_API void WINAPI AU3_Send(LPCWSTR szSendText, int nMode = 0);
AU3_API int WINAPI AU3_Shutdown(int nFlags);
AU3_API void WINAPI AU3_Sleep(int nMilliseconds);
AU3_API int WINAPI AU3_StatusbarGetText(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, /*[in,defaultvalue(1)]*/int nPart, LPWSTR szStatusText, int nBufSize);
AU3_API int WINAPI AU3_StatusbarGetTextByHandle(HWND hWnd, /*[in,defaultvalue(1)]*/int nPart, LPWSTR szStatusText, int nBufSize);

AU3_API void WINAPI AU3_ToolTip(LPCWSTR szTip, int nX = AU3_INTDEFAULT, int nY = AU3_INTDEFAULT);

AU3_API int WINAPI AU3_WinActivate(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText);
AU3_API int WINAPI AU3_WinActivateByHandle(HWND hWnd);
AU3_API int WINAPI AU3_WinActive(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText);
AU3_API int WINAPI AU3_WinActiveByHandle(HWND hWnd);
AU3_API int WINAPI AU3_WinClose(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText);
AU3_API int WINAPI AU3_WinCloseByHandle(HWND hWnd);
AU3_API int WINAPI AU3_WinExists(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText);
AU3_API int WINAPI AU3_WinExistsByHandle(HWND hWnd);
AU3_API int WINAPI AU3_WinGetCaretPos(LPPOINT lpPoint);
AU3_API void WINAPI AU3_WinGetClassList(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPWSTR szRetText, int nBufSize);
AU3_API void WINAPI AU3_WinGetClassListByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
AU3_API int WINAPI AU3_WinGetClientSize(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPRECT lpRect);
AU3_API int WINAPI AU3_WinGetClientSizeByHandle(HWND hWnd, LPRECT lpRect);
AU3_API HWND WINAPI AU3_WinGetHandle(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText);
AU3_API void WINAPI AU3_WinGetHandleAsText(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPWSTR szRetText, int nBufSize);
AU3_API int WINAPI AU3_WinGetPos(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPRECT lpRect);
AU3_API int WINAPI AU3_WinGetPosByHandle(HWND hWnd, LPRECT lpRect);
AU3_API DWORD WINAPI AU3_WinGetProcess(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText);
AU3_API DWORD WINAPI AU3_WinGetProcessByHandle(HWND hWnd);
AU3_API int WINAPI AU3_WinGetState(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText);
AU3_API int WINAPI AU3_WinGetStateByHandle(HWND hWnd);
AU3_API void WINAPI AU3_WinGetText(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPWSTR szRetText, int nBufSize);
AU3_API void WINAPI AU3_WinGetTextByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
AU3_API void WINAPI AU3_WinGetTitle(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPWSTR szRetText, int nBufSize);
AU3_API void WINAPI AU3_WinGetTitleByHandle(HWND hWnd, LPWSTR szRetText, int nBufSize);
AU3_API int WINAPI AU3_WinKill(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText);
AU3_API int WINAPI AU3_WinKillByHandle(HWND hWnd);
AU3_API int WINAPI AU3_WinMenuSelectItem(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, LPCWSTR szItem1, LPCWSTR szItem2, LPCWSTR szItem3, LPCWSTR szItem4, LPCWSTR szItem5, LPCWSTR szItem6, LPCWSTR szItem7, LPCWSTR szItem8);
AU3_API int WINAPI AU3_WinMenuSelectItemByHandle(HWND hWnd, LPCWSTR szItem1, LPCWSTR szItem2, LPCWSTR szItem3, LPCWSTR szItem4, LPCWSTR szItem5, LPCWSTR szItem6, LPCWSTR szItem7, LPCWSTR szItem8);
AU3_API void WINAPI AU3_WinMinimizeAll();
AU3_API void WINAPI AU3_WinMinimizeAllUndo();
AU3_API int WINAPI AU3_WinMove(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, int nX, int nY, int nWidth = -1, int nHeight = -1);
AU3_API int WINAPI AU3_WinMoveByHandle(HWND hWnd, int nX, int nY, int nWidth = -1, int nHeight = -1);
AU3_API int WINAPI AU3_WinSetOnTop(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, int nFlag);
AU3_API int WINAPI AU3_WinSetOnTopByHandle(HWND hWnd, int nFlag);
AU3_API int WINAPI AU3_WinSetState(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, int nFlags);
AU3_API int WINAPI AU3_WinSetStateByHandle(HWND hWnd, int nFlags);
AU3_API int WINAPI AU3_WinSetTitle(LPCWSTR szTitle,/*[in,defaultvalue("")]*/ LPCWSTR szText, LPCWSTR szNewTitle);
AU3_API int WINAPI AU3_WinSetTitleByHandle(HWND hWnd, LPCWSTR szNewTitle);
AU3_API int WINAPI AU3_WinSetTrans(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, int nTrans);
AU3_API int WINAPI AU3_WinSetTransByHandle(HWND hWnd, int nTrans);
AU3_API int WINAPI AU3_WinWait(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, int nTimeout = 0);
AU3_API int WINAPI AU3_WinWaitByHandle(HWND hWnd, int nTimeout);
AU3_API int WINAPI AU3_WinWaitActive(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, int nTimeout = 0);
AU3_API int WINAPI AU3_WinWaitActiveByHandle(HWND hWnd, int nTimeout);
AU3_API int WINAPI AU3_WinWaitClose(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, int nTimeout = 0);
AU3_API int WINAPI AU3_WinWaitCloseByHandle(HWND hWnd, int nTimeout);
AU3_API int WINAPI AU3_WinWaitNotActive(LPCWSTR szTitle, /*[in,defaultvalue("")]*/LPCWSTR szText, int nTimeout);
AU3_API int WINAPI AU3_WinWaitNotActiveByHandle(HWND hWnd, int nTimeout = 0);

///////////////////////////////////////////////////////////////////////////////
