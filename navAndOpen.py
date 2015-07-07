g = __import__("gradingScript")
import os

def runner():
    fileList = g.navigateAndStore("index.html")
    for filePath in fileList:
        lastName = filePath.split("/")[5]
        if str(raw_input("Do you want to grade " + lastName[:len(lastName) - 34] + "?")) == "y":
            os.startfile(filePath + "index.html")
        raw_input("Press Enter to continue to next student")

runner()