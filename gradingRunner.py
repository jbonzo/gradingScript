g = __import__("gradingScript")
import os
import platform

def runner():
    isWindows = platform.system() == "Windows"

    hwNum = str(raw_input("What homework number is this?"))
    fileList = g.navigateAndStore("hw0" + hwNum + ".py")
    counter = 0
    clear = lambda : (os.system("cls") if isWindows else os.system("clear"))

    for filePath in fileList:
        done = False
        lastName = filePath.split("/")[5]
        prompt = "Do you want to grade " + lastName[:len(lastName) - 34] + "?"
        donePrompt = "Are you done grading this homework?"
        print lastName[:len(lastName) - 34]
        if str(raw_input(prompt)) == "y":
            while not done:
                g.callFunctions(filePath)
                if str(raw_input(donePrompt)) == "y":
                    done = True
                clear()

        counter = counter + 1
        clear()

    

runner()