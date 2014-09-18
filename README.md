PyAutoIt
========

Python binding for AutoItX3.dll

### Installing

If you have pip on your system, you can simply install or upgrade PyAutoIt:

```python
pip install -U pyautoit
```

Alternately, you can download the source distribution from PyPI, unarchive it, and run:

```python
python setup.py install
```

### Example

- open notepad
- type some string into notepad, eg: **"hello world"**
- close notepad without saving

```python
import autoit

autoit.run("notepad.exe")
autoit.win_wait_active("[CLASS:Notepad]", 3)
autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
autoit.win_close("[CLASS:Notepad]")
autoit.control_click("[Class:#32770]", "Button2")
```
