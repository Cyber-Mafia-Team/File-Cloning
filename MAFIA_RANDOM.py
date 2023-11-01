import os,platform
os.system('git pull')
Ruhull=platform.architecture()[0]
if Ruhull=="32bit":__import__("RUHUL32")
elif Ruhull=="64bit":__import__("RUHUL64")