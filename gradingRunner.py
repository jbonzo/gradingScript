g = __import__("gradingScript")
import os

def runner():
    fileList = g.navigateAndStore("hw08.py")
    counter = 0
    clear = lambda : os.system("cls")

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

        counter = counter + 1
        clear()

runner()