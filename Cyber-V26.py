import os,platform
os.system('git pull')
Cyber=platform.architecture()[0]
if Cyber=="32bit":__import__("cd")
elif Cyber=="64bit":__import__("ab")