import os
os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/run-darkos.py &>/dev/null")   
os.system("wget https://raw.githubusercontent.com/ahmad1abbadi/darkos/main/run-update &>/dev/null")
os.system("chmod +x darkos")
os.system("mv darkos darkos.py $PREFIX/bin/")
