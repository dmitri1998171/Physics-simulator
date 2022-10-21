import os
import time
os.system('pip install pipreqs')
time.sleep(1)
os.system('pipreqs ./')
time.sleep(1)
os.system('pip install -r requirements.txt')
print('success')
