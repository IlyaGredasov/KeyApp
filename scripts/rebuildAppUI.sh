#!/bin/bash

pyuic5 -x .\design\main_window.ui -o .\src\main_window.py
pyuic5 -x .\design\alert.ui -o .\src\alert.py
pyuic5 -x .\design\password_query.ui -o .\src\password_query.py
pyuic5 -x .\design\delete_dialog.ui -o .\src\delete_dialog.py