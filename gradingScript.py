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
import filecmp

#################### Set Up ####################

currentPathList = [
	"D:/Users/Ricky/Desktop/Coding/Projects/gradingScript/",
	"C:/Users/Ricky/Desktop/coding/Projects/gradingScript"
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
		"D:/Users/Ricky/Desktop/Classes/CS 1315 TA/text/"
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
	newCode = "import os\ndef getMediaPath():\n\ttextPathList = [\n\t\t"
	newCode = newCode + "\"C:/Users/Ricky/Downloads/Bulk Download/Media Sources/text/\",\n\t\t"
	newCode = newCode + "\"D:/Users/Ricky/Desktop/Classes/CS 1315 TA/text/\",\n\t]"
	newCode = newCode + "\n\n\tfor path in textPathList:\n\t\tif os.path.exists(path):\n\t\t\t"
	newCode = newCode + "return path\n\n"
	return newCode

def setMediaPath2(filePath):
	fileName = "hw06.py" if os.path.exists(filePath + "hw06.py") else "HW06.py"

	testFile = open(filePath + fileName, "r+")
	code = testFile.read().replace(getNewCode(), "")
	code = getNewCode() + code
	testFile.close()

	testFile = open(filePath + fileName, "w+")
	testFile.write(code)
	testFile.close()

def callFunctions(filePath):
	sys.path.append(filePath)
	#print "    " + str(filePath)
	#print "    " + str(os.listdir(filePath))
	try:
		from hw06 import evenOdd
	except ImportError, e:
		from HW06 import evenOdd
	else:
		evenOdd("words.txt")
		sys.path.remove(filePath)

def fileCheck(file1, file2):
	return filecmp.cmp(file1, file2)

def runner():
	fileList = navigateAndStore()

	for filePath in fileList:
		setMediaPath2(filePath)
		callFunctions(filePath)
		break


print fileCheck(getMediaPath() + "evenOddTest.txt", getMediaPath() + "evenOdd.txt")
#runner()

#print getNewCode()
#print open(currentPath + "gradingScript.py", "r").read()

"""
	For some reason in the Note: Suppress Return commit it prints none
	Learn how to suppress unwanted return statements
"""

"""
	change reference of:
		from HW01 import *
	to:
		form HWa import *
	Make HWa point to an item from a list of references
"""