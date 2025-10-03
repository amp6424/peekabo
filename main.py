# importing modules
from modules import os_info

# detecting the os type
ostype = os_info.detect_os()
print(f"You are a {ostype}'s User!")

# get system information
os_info.os_info()


'''
# running fucntions based on os
if ostype == "Windows":
    # code for windows
    pass
elif ostype == "Linux":
    # code for linux
    pass
elif ostype == "Darwin":
    # code for mac
    pass
'''