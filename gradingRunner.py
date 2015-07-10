g = __import__("gradingScript")
import os

def runner():
    fileList = navigateAndStore("hw.py")
    counter = 0
    clear = lambda : os.system("cls")
    done = False
    for filePath in fileList:
        lastName = filePath.split("/")[5]
        prompt = "Do you want to grade " + lastName[:len(lastName) - 34] + "?"
        donePrompt = "Are you done grading this homework?"
        print lastName[:len(lastName) - 34]
        if str(raw_input(prompt)) == "y":
            setMediaPath2(filePath, True)
            while not done:
                callFunctions(filePath)
                if str(raw_input(donePrompt)) == "y":
                    done = True
            setMediaPath2(filePath, False)
        counter = counter + 1
        clear()
