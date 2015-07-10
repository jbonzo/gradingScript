g = __import__("gradingScript")
import os

def runner():
    htmlList = g.navigateAndStore(".html")
    cssList = g.navigateAndStore(".css")
    try:
        for html, css in zip(htmlList, cssList):
            lastName = html[2].split("/")[5]
            if str(raw_input("Do you want to grade " + lastName[:len(lastName) - 34] + "?")) == "y":
                os.startfile(html[2] + "/" + html[1])
                #os.startfile(html[2] + "/" + html[1])
                #os.startfile(css[2] + "/" + css[1])
            raw_input("Press Enter to continue to next student")
    except ValueError, e:
        raise e

runner()