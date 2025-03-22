#!/bin/bash

sudo apt install libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxkbcommon-x11-0
sudo apt install python3.12 python3.12-venv python3.12-dev
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

pyinstaller --onefile --name=KeyApp \
  --add-data="./src/Alert.py:." \
  --add-data="./src/DeleteDialog.py:." \
  --add-data="./src/PasswordQuery.py:." \
  --add-data="./src/WebApi.py:." \
  --add-data="./design/alert.png:." \
  --collect-submodules PyQt5 \
  --collect-submodules requests \
  --collect-binaries python3.12 \
  ./src/MainWindow.py

deactivate
