"""
	1. Navigate through folders
		Use os.listdir() and loop through my students
		Use recursion?
	2. Call functions from files in script
		Use sys.path.append(path)
	2a. Account for getMediaPath()
		Use I/O to place getMediaPath() in each file
	3. Read output.txt files and ensure they are similar to test case files
		Read file cmp docs
	4. Record how many are right vs wrong
	5. Print score
"""

import sys
import os

#################### Set Up ####################


currentPathList = [
	"D:/Users/Ricky/Desktop/Coding/Projects/gradingScript/",
	"C:/Users/Ricky/Desktop/coding/Projects/gradingScript/",
	"C:/Users/rbarillas3/Documents/GitHub/gradingScript/"
]
currentPath = ""

bulkPathList = [
	"C:/Users/rbarillas3/Downloads/Bulk Download/",
	"D:/Users/Ricky/Downloads/Bulk Download/",
	"C:/Users/Ricky/Downloads/Bulk Download/"
]
bulkDownload = ""



#to make it compatible with any developing computer
for bulkPath in bulkPathList:
	if os.path.exists(bulkPath):
		bulkDownload = bulkPath

for path in currentPathList:
	if os.path.exists(path):
		currentPath = path

#List of student directories
students = os.listdir(bulkDownload)


#################### Function Definitions ####################

def findPYFile(path):
	#if the current directory is empty return none
	if len(os.listdir(path)) <= 0:
		return (False, "")
	items = os.listdir(path)
	newPath = path + "/" + items[0]

	#if the file is there return the path of its directory
	#if it doesnt exist and we can go deeper then go deeper
	#else return none
	if "hw06.py" in items or "HW06.py" in items:
		return (True, path)
	elif os.path.isdir(newPath):
		return findPYFile(newPath)
	else:
		return (False, "")

def getMediaPath():
	textPathList = [
		"C:/Users/Ricky/Downloads/Bulk Download/Media Sources/text/",
		"D:/Users/Ricky/Desktop/Classes/CS 1315 TA/text/",
		"C:/Users/rbarillas3/Downloads/Bulk Download/Media Sources/text/"
	]

	for path in textPathList:
		if os.path.exists(path):
			return path


def navigateAndStore():
	counter = 0
	studentFilePaths = []

	#cycle through every student
	for student in students:
		#makes a path based on current student
		path = bulkDownload + student
		lastName = student.split(",")[0].strip()
		if findPYFile(path)[0]:
			counter = counter + 1
			#string type for homework file path
			studentFilePaths.append(findPYFile(path)[1] + "/")
	return studentFilePaths

def getNewCode():
	codeSource = open("gradingScript.py", "rt")
	newCode = "import os\n"
	sentinal = ""
	while not sentinal == "def getMediaPath():\n":
		sentinal = codeSource.readline()

	newCode = newCode + sentinal
	sentinal = codeSource.readline()

	while not sentinal == "\t\t\treturn path\n":
		newCode = newCode + sentinal
		sentinal = codeSource.readline()
	return newCode + sentinal

def setMediaPath2(filePath, addCode):
	fileName = "hw06.py" if os.path.exists(filePath + "hw06.py") else "HW06.py"

	testFile = open(filePath + fileName, "r+")
	code = testFile.read().replace(getNewCode(), "")
	#print code[:50] + "\n"
	if addCode:
		code = getNewCode() + code
		#print code[:50] + "GETTTT\n"
	testFile.close()
	testFile = open(filePath + fileName, "w")
	testFile.write(code)
	testFile.close()



def callFunctions(filePath):
	sys.path.append(filePath)

	try:
		hw06 = __import__("hw06")
		os.startfile(filePath + "hw06.py")
		reload(hw06)
	except ImportError, e:
		os.startfile(filePath + "HW06.py")
		hw06 = __import__("HW06")
		reload(HW06)

	#for item, key in sys.modules.iteritems():
	#	print item, key
	#	raw_input()

	print "\nrandomOrder:"
	try:
		hw06.randomOrder("words.txt")
	except IOError, e:
		hw06.randomOrder(getMediaPath() + "words.txt")

	raw_input("\nPress Enter to continue")

	print "\noneLine.txt exists:",
	try:
		hw06.oneLine("words.txt")
	except IOError, e:
		hw06.oneLine(getMediaPath() + "words.txt")
	if os.path.exists(getMediaPath() + "oneLine.txt"):
		os.startfile(getMediaPath() + "oneLine.txt")
		print  "True"
	else:
		print "False"

	raw_input("\nPress Enter to continue")

	print "\nunderAverage:"
	try:
		hw06.underAverage("words2.txt")
	except IOError, e:
		hw06.underAverage(getMediaPath() + "words2.txt")

	raw_input("\nPress Enter to continue")

	print "\nevenOdd.txt exists:",
	try:
		hw06.evenOdd("words.txt")
	except IOError, e:
		hw06.evenOdd(getMediaPath() + "words.txt")
	if os.path.exists(getMediaPath() + "evenOdd.txt"):
		os.startfile(getMediaPath() + "evenOdd.txt")
		print "True"
	else:
		print "False"

	raw_input("\nPress Enter to continue")

	print "\nnicCage.txt exists:",
	try:
		hw06.nicIsBack("words.txt")
	except IOError, e:
		hw06.nicIsBack(getMediaPath() + "words.txt")
	if os.path.exists(getMediaPath() + "nicCage.txt"):
		os.startfile(getMediaPath() + "nicCage.txt")
		print "True"
	else:
		print "False"

	sys.path.remove(filePath)
	raw_input("\nPress Enter to go on to the next student")
	if os.path.exists(getMediaPath() + "oneLine.txt"):
		try:
			os.remove(getMediaPath() + "oneLine.txt")
		except WindowsError, e:
			print "Won't remove file"
	if os.path.exists(getMediaPath() + "evenOdd.txt"):
		os.remove(getMediaPath() + "evenOdd.txt")
	if os.path.exists(getMediaPath() + "nicCage.txt"):
		os.remove(getMediaPath() + "nicCage.txt")

def grade():
	pointsOff = 0
	os.startfile(getMediaPath() + "nicCage.txt", "r")
	open(getMediaPath() + "oneLine.txt", "r")


def runner():
	fileList = navigateAndStore()
	counter = 0
	clear = lambda : os.system("cls")
	for filePath in fileList:
		lastName = filePath.split("/")[5]
		print lastName[:len(lastName) - 34]
		if str(raw_input("Do you want to grade " + lastName[:len(lastName) - 34] + "?")) == "y":
			setMediaPath2(filePath, True)
			callFunctions(filePath)
			setMediaPath2(filePath, False)
		counter = counter + 1
		clear()
		#grade()


runner()

#print getNewCode()
#print open(currentPath + "gradingScript.py", "r").read()

"""
	DEBUG:
		Cleaned up Exceptions.. Kinda (commit):
			Doesn't reset the command prompt and calls from former students
			To re-enact do daniel seal then reba sellers
		FIXED:
			used __import__("module") and reload(module)
"""

"""
	For some reason in the Note: Suppress Return commit it prints none
	Learn how to suppress unwanted return statements
"""

"""
	change reference of:
		from HW01 import *
	to:
		from HWa import *
	Make HWa point to an item from a list of references


	var = __import__("x")
	module x contains function test()
	var.test() doesnt throw errer
"""

"""
	Dynamic grading. For the first several students I input
	my comments like normal but I will never repeat my self.
	The script will know that some error equals an equivalent comment
	and it will autofill the comment for me.
"""