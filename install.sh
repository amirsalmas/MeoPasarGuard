#!/bin/bash
echo "در حال نصب پنل میو پاسارگارد..."
apt-get update
apt-get install -y git python3 python3-pip
git clone https://github.com/amirsalmas/MeoPasarGuard.git /opt/MeoPasarGuard
cd /opt/MeoPasarGuard
pip install -r requirements.txt
nohup python3 main.py > panel.log 2>&1 &
echo "نصب تمام شد! پنل روی پورت 8080 بالا اومد."
