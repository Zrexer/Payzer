import payobj.paycolor
import time
import os 

os.system("")

activated = True

class Console(object):

    def endPointAnimation(itemsList: list, firstMessage: str, endMessage: str, endData = "", sleepedTime = 0.8):
        while activated:
            for item in itemsList:
                print(f"\r{firstMessage}{item}", flush=False, end="")
                time.sleep(sleepedTime)

            print(f"\r{endMessage}{endData}\t", flush=False, end="")
            break

    def loadingAnimation(message: str = ""):
        itemsParty = ['/', "|", '\\', "_", "-", "_", "<", "=", ">", "\t"]
        while activated:
            for items in itemsParty:
                print(f"\r{message} {items}", flush=False, end="")
                time.sleep(0.5)

            break
        print()
    
    def promptMessage(comdis: dict, infronter: int = 15):
        print("\r  {:<{}}{}".format("Commands", infronter, "Discription"))
        print("\r  {:<{}}{}".format("--------", infronter, "-----------"))
        for command, dis in comdis.items():
            print(
                "\r  {:<{}}{}".format(command, infronter, dis)
            )


    def printBanner():
        padding = '  '
        
        # Define ASCII art patterns for each letter
        P = [[' ', '┌', '─', '┐'], [' ', '│', '├', '┤'], [' ', '|', ' ', ' '],[' ', '└', '─', '┘']]
        A = [[' ', '┌', '─', '┐'], [' ', '├', '─', '┤'], [' ', '┴', ' ', '┴']]
        Y = [[' ', '┐', ' ', '┌'], [' ', '┌', '|', '┐'], [' ', ' ', '|', ' ']]
        Z = [['  ', '─', '─', '┐'], [' ', ' ', ' ', '/'], [' ', ' ', '/', ' '], [' ', '└', '─', '┘']]
        E = [['', '┌', '─', '┐'], [' ', '├', '┤', ' '], [' ', '└', '─', '┘']]
        R = [[' ', '|', "──", '┌'], [' ', '|', ' ', ' '], [' ', '|', " ", ' ']]
        
        banner = [P, A, Y, Z, E, R]
        final = []
        print('\r')
        init_color = 36
        txt_color = init_color
        cl = 0
        
        for charset in range(0, 3):
            for pos in range(0, len(banner)):
                for i in range(0, len(banner[pos][charset])):
                    clr = f'\033[38;5;{txt_color}m'
                    char = f'{clr}{banner[pos][charset][i]}'
                    final.append(char)
                    cl += 1
                    txt_color = txt_color + 36 if cl <= 3 else txt_color
                
                cl = 0
                txt_color = init_color
            
            init_color += 31
            
            if charset < 2:
                final.append('\n   ')
        
        print(f"   {''.join(final)}")
        print(f'{payobj.paycolor.colors.END}{padding}                           by Zrexer\n')

    def starterPrint():
        print(f"{payobj.paycolor.colors.white}[{payobj.paycolor.colors.META}INFO{payobj.paycolor.colors.white}] Created and Published by {payobj.paycolor.colors.ORANGE}Zrexer")
        print(f"{payobj.paycolor.colors.white}[{payobj.paycolor.colors.META}INFO{payobj.paycolor.colors.white}] https://github.com/Zrexer")

    def streamPrompt():
        user = str(input(f"{payobj.paycolor.colors.white}{payobj.paycolor.colors.underline}Payzer{payobj.paycolor.colors.white} > "))
        return {"user": user, "splited": user.split()}
