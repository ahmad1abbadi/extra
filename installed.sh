#!/bin/bash
clear
echo "installing packages please wait"
echo ""
apt-get update &>/dev/null
apt-get -y --with-new-pkgs -o Dpkg::Options::="--force-confdef" upgrade &>/dev/null
apt install python --no-install-recommends -y &>/dev/null
echo "be patient"
curl -o run-insta.py https://raw.githubusercontent.com/ahmad1abbadi/test2/main/run-insta.py && python3 run-insta.py
    exit
fi
