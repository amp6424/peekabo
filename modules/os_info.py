import platform

def detect_os() -> str:
    # this identifies the operating system that we are using
    ostype = platform.uname().system
    return ostype

def os_info() -> None:
    # keys array
    info = ["system", "node", "release", "version", "root", "machine"]
    # printing the system information
    print("\nSYSTEM INFORMATION:")
    print("====================")
    # getting the sys info and printing it likewise
    for i, details in enumerate(platform.uname()):
        print(f"{info[i]}: {details}")
    print("")
        
