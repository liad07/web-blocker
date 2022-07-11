import webbrowser
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
file = open("C:\Windows\System32\drivers\etc\hosts", "r", encoding="utf8")
file1 = open("hosts", "w", encoding="utf8")
x=file.read()
for i in range (len(file.read().split("\n"))):
    file1.write(x+"\n")
    web=input(bcolors.OKBLUE+"enter url \n" + bcolors.ENDC)
    webr="127.0.0.1"
    file1.write(webr+" "+web)
file1.close()
print(bcolors.OKBLUE+"copy the hosts file to the folder has open now" + bcolors.ENDC)
webbrowser.open("C:\Windows\System32\drivers\etc")