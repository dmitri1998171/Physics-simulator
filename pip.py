import os 
os.system('pip install pipreqs')
os.system('pipreqs ./src')
os.system('pip install -r requirements.txt')
print('succses')