from payobj import console
from payobj import payrok
from payobj import payid
from payobj import payenc
from payobj import payload
from payobj import paycolor as colors

class Help:
    dictData = {
        "help": "Show this message",
        "make": "Make payload: make type=path/to/pay",
        "encode": "Just use for Powershell payloads: make=pw/3/tcp LHOST 1.1.1.1 LPORT 1234 encode",
        "whoami": "Show your hex id",
        "set": "Set and Save the ngrok auth token",
        "tun": "Make tunnel with ngrok: tun http 5566 (all of options is optional)",
        "isexists": "Like search command in msfconsole, use for payloads",
        "paths": "Give the Paths for make payload",
        "gettun": "Get Online And Active NGROK Tunnels",
        "dl-ngrok": "Download the Ngrok File, Payzer scan your os system and download the same type of system",
        "exit": "Exit and finish the program"
    }

class PayPaths:
    pths = [
        "/pw/1", 
        "/pw/2",
        "/pw/3",
        "/pw/4",
        "/bash/tcp",
        "/bash/udp",
        "/bash/dev196",
        "/bash/readline",
        "/bash/bash5",
        "/bash/5",
        "/bash/curl",
        "/nc/regular",
        "/nc/exe",
        "/nc/exec",
        "/nc/busybox",
        "/nc/backdoor",
        "/nc/udp",
        "/rc",
        "/c/src",
        "/c/win32src",
        "/csh/tcp",
        "/csh/bash",
        "/ruby/regular",
        "/ruby/nosh",
        "/nodejs/tcp",
        "/nodejs/nc",
        "/nodejs/socket",
        "/lua/socket",
        "/lua/socket/v1",
        "/lua/socket/v2",
        "/go/socket",
        "/crystal/socket"
    ]

class Log:
    def err(msg):
        print(f"{colors.colors.white}[{colors.colors.red}ERROR{colors.colors.white}] {msg}")

class Payzer(object):

    def start():
        console.Console.printBanner()
        console.Console.starterPrint()
        console.Console.loadingAnimation(f"{colors.colors.white}[{colors.colors.yellow}UPDATES{colors.colors.white}] Drink a Coffee ...")
        hexId = payid.PayID.makePrivateUID()
        print()

        while 1:
            data = console.Console.streamPrompt()
            user: str = data['user']
            text: list = data['splited']

            if user == "help":
                print()
                console.Console.promptMessage(Help.dictData)
            
            elif user.startswith("make"):
                print()
                iscall = False
                txtdata = {}
                nums = 0

                for txt in text:
                    nums += 1
                    if str(txt).startswith("type="):
                        iscall = True
                        txtdata['index'] = nums
                        txtdata['data'] = txt.split("=")[1]
                    else:pass

                if iscall == False:
                    Log.err("Use 'type' to give payload path")
                else:
                    paypath = str(txtdata['data'])
                    if paypath == "" or paypath == " ":
                        Log.err("Cannot get the path of paypath")
                    
                    else:
                        otherData = text
                        if paypath == "/pw/1":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    if "encode" == otherData[-1]:
                                        LHOST = otherData[otherData.index("LHOST")+1]
                                        LPORT = otherData[otherData.index("LPORT")+1]
                                        print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                        print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                        dt = payload.Powershell().makePrepare(LHOST, LPORT)
                                        print(colors.colors.ORANGE, payenc.PayloadEncryptor.changer(str(dt['data'])))
                                        if dt['is_copy'] == True:
                                            print(colors.colors.green, "Saved in clipboard")
                                    else:
                                        LHOST = otherData[otherData.index("LHOST")+1]
                                        LPORT = otherData[otherData.index("LPORT")+1]
                                        print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                        print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                        dt = payload.Powershell().makePrepare(LHOST, LPORT)
                                        print(colors.colors.ORANGE, dt['data'])
                                        if dt['is_copy'] == True:
                                            print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")
                        
                        elif paypath == "/pw/2":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    if "encode" == otherData[-1]:
                                        LHOST = otherData[otherData.index("LHOST")+1]
                                        LPORT = otherData[otherData.index("LPORT")+1]
                                        print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                        print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                        dt = payload.Powershell(2).makePrepare(LHOST, LPORT)
                                        print(colors.colors.ORANGE, payenc.PayloadEncryptor.changer(str(dt['data'])))
                                        if dt['is_copy'] == True:
                                            print(colors.colors.green, "Saved in clipboard")
                                    else:
                                        LHOST = otherData[otherData.index("LHOST")+1]
                                        LPORT = otherData[otherData.index("LPORT")+1]
                                        print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                        print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                        dt = payload.Powershell(2).makePrepare(LHOST, LPORT)
                                        print(colors.colors.ORANGE, dt['data'])
                                        if dt['is_copy'] == True:
                                            print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")
                        
                        elif paypath == "/pw/3":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    if "encode" == otherData[-1]:
                                        LHOST = otherData[otherData.index("LHOST")+1]
                                        LPORT = otherData[otherData.index("LPORT")+1]
                                        print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                        print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                        dt = payload.Powershell(3).makePrepare(LHOST, LPORT)
                                        print(colors.colors.ORANGE, payenc.PayloadEncryptor.changer(str(dt['data'])))
                                        if dt['is_copy'] == True:
                                            print(colors.colors.green, "Saved in clipboard")
                                    else:
                                        LHOST = otherData[otherData.index("LHOST")+1]
                                        LPORT = otherData[otherData.index("LPORT")+1]
                                        print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                        print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                        dt = payload.Powershell(3).makePrepare(LHOST, LPORT)
                                        print(colors.colors.ORANGE, dt['data'])
                                        if dt['is_copy'] == True:
                                            print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/pw/4":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    if "encode" == otherData[-1]:
                                        LHOST = otherData[otherData.index("LHOST")+1]
                                        LPORT = otherData[otherData.index("LPORT")+1]
                                        print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                        print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                        dt = payload.Powershell(4).makePrepare(LHOST, LPORT)
                                        print(colors.colors.ORANGE, payenc.PayloadEncryptor.changer(str(dt['data'])))
                                        if dt['is_copy'] == True:
                                            print(colors.colors.green, "Saved in clipboard")
                                    else:
                                        LHOST = otherData[otherData.index("LHOST")+1]
                                        LPORT = otherData[otherData.index("LPORT")+1]
                                        print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                        print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                        dt = payload.Powershell(4).makePrepare(LHOST, LPORT)
                                        print(colors.colors.ORANGE, dt['data'])
                                        if dt['is_copy'] == True:
                                            print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/bash/tcp":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Bash.tcp(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/bash/udp":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Bash.udp(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/bash/dev196":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Bash.dev196(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/bash/readline":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Bash.readline(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/bash/bash5" or paypath == "bash/5":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Bash.bash5(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/bash/curl":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Bash.curl(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/nc/regular":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.NetCat.regular(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/nc/exe":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.NetCat.exe(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/nc/busybox":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.NetCat.busyBox(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/nc/backdoor":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.NetCat.backdoor(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/nc/exec":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.NetCat.executer(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/nc/udp":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.NetCat.udp(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/rc":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.RustCat.makePay(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")
                        
                        elif paypath == "/c/src":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.C.source(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")
                        
                        elif paypath == "/c/win32src":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.C.windowsSource(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/csh/tcp":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.CSharp.tcp(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/csh/bash":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.CSharp.bash(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")
                        
                        elif paypath == "/ruby/regular":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Ruby.regular(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/ruby/nosh":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Ruby.noSh(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/nodejs/nc":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.NodeJS.netCatStealer(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/nodejs/socket":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.NodeJS.socketWorker(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/lua/socket" or paypath == "/lua/socket/v1":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Lua.socketWorker(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/lua/socket/v2":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Lua.socketWorkerV2(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/go/socket":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.GoLang.socketWorker(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")

                        elif paypath == "/crystal/socket":
                            if "LHOST" in otherData:
                                if "LPORT" in otherData:
                                    LHOST = otherData[otherData.index("LHOST")+1]
                                    LPORT = otherData[otherData.index("LPORT")+1]
                                    print(f"{colors.colors.cyan}LHOST{colors.colors.red} => {colors.colors.white}{LHOST}")
                                    print(f"{colors.colors.cyan}LPORT{colors.colors.red} => {colors.colors.white}{LPORT}")
                                    dt = payload.Crystal.socketWorker(LHOST, LPORT)
                                    print(colors.colors.ORANGE, dt['data'])
                                    if dt['is_copy'] == True:
                                        print(colors.colors.green, "Saved in clipboard")
                                else:Log.err("Please set port with LPORT: LPORT 1234")
                            else:Log.err("Please set host with LHOST: LHOST 1.1.1.1")
                        
                        else:Log.err(f"The path '{paypath}' Does not exists, please use 'isexists' command")

            elif user == "whoami":
                print()
                print(colors.colors.white, "[",colors.colors.IMPORTANT,colors.colors.white, "] ",hexId)

            elif user.startswith("isexists"):
                print()
                path = user.replace("isexists ", "")
                if path == "isexists":Log.err(f"Please set the payload path infront of isexists")
                else:
                    print(f"{colors.colors.white}Search for '{colors.colors.Backpink}{path}{colors.colors.white}'")
                    if path in PayPaths.pths:
                        print(f"{colors.colors.white}The '{colors.colors.Backpink}{path}{colors.colors.white}' Does {colors.colors.green}Exists")
                    else:print(f"{colors.colors.red}Cannot find {colors.colors.white}'{colors.colors.Backpink}{path}{colors.colors.white}'")

            elif user.startswith("set"):
                tk = user.replace("set ", "")
                if tk == "set":Log.err(f"Please set the auth token infront of set")
                else:
                    payrok.PayRok.setToken(tk)
                    print(f"{colors.colors.white}The token {colors.colors.green}'{tk}'{colors.colors.white} was save")
            
            elif user.startswith("tun"):
                app = payrok.PayRok

                ishttp = False
                ishttps = False
                isport = False

                if "port" in text:
                    isport = True
                
                if "http" in text:
                    ishttp = True

                if "https" in text:
                    ishttps = True

                if ishttps == True and ishttp == True:Log.err("Cannot selecte the both method")

                if ishttp == True:
                    if isport == True:
                        try:
                            app.stableConnection("http", int(text[text.index("port")+1]))
                        except Exception as ER:Log.err(ER)
                    else:
                        try:
                            app.stableConnection("http")
                        except Exception as ER:Log.err(ER)
                elif ishttps == True:
                    if isport == True:
                        try:
                            app.stableConnection("https", int(text[text.index("port")+1]))
                        except Exception as ER:Log.err(ER)
                    else:
                        try:
                            app.stableConnection("https")
                        except Exception as ER:Log.err(ER)
                else:Log.err("No Method selected")

            elif user == "gettun":print(payrok.PayRok.getTunnels())

            elif user == "dl-ngrok":payrok.PayRok.dls()

            elif user == "paths":print(json.dumps(PayPaths.pths, indent=4))

            elif user == "ls":import os;os.system("ls")

            elif user == "cls" or user == "clear":import os;os.system("cls || clear")

            elif user == "exit":exit()
try:
    Payzer.start()
except KeyboardInterrupt:
    exit()
