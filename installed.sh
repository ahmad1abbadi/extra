#!/bin/bash
clear
echo "installing packages please wait"
echo ""
apt-get update &>/dev/null
apt-get -y --with-new-pkgs -o Dpkg::Options::="--force-confdef" upgrade &>/dev/null
apt install python --no-install-recommends -y &>/dev/null
echo "be patient"
curl -o installglibc.py https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/installglibc.py && python3 installglibc.py
    exit
fi
