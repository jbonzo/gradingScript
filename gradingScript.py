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
from time import sleep

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

hwPy = ""

answers = []

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

def findFile(path, desiredFile):
	#if the current directory is empty return none
	if len(os.listdir(path)) <= 0:
		return (False, "")
	items = os.listdir(path)
	newPath = path + "/" + items[0]
	#if the file is there return the path of its directory
	#if it doesnt exist and we can go deeper then go deeper
	#else return none
	if desiredFile in items:
		return (True, path)
	elif os.path.isdir(newPath):
		return findFile(newPath, desiredFile)
	else:
		return (False, "")

def findFileExt(path, desiredExtension):
	#if the current directory is empty return none
	if len(os.listdir(path)) <= 0:
		return (False, "", )
	items = os.listdir(path)
	newPath = path + "/" + items[0]

	#if the file is there return the path of its directory
	#if it doesnt exist and we can go deeper then go deeper
	#else return none
	#Ternary  = "desired outcome" if condition else "other outcome"
	for item in items:
		if desiredExtension in item:
			return (True, item, path)
	if os.path.isdir(newPath):
		return findFileExt(newPath, desiredExtension)
	else:
		return (False, "", )

def getMediaPath():
	textPathList = [
		"C:/Users/Ricky/Downloads/Bulk Download/Media Sources/text/",
		"D:/Users/Ricky/Desktop/Classes/CS 1315 TA/text/",
		"C:/Users/rbarillas3/Downloads/Bulk Download/Media Sources/text/"
	]

	for path in textPathList:
		if os.path.exists(path):
			return path


def navigateAndStore(desiredFile):
	counter = 0
	studentFilePaths = []
	global hwPy
	hwPy = desiredFile
	#cycle through every student
	for student in students:
		#makes a path based on current student
		path = bulkDownload + student
		#lastName = student.split(",")[0].strip()
		if desiredFile[0] == ".":
			if findFileExt(path, desiredFile)[0]:
				counter = counter + 1
				studentFilePaths.append(findFileExt(path, desiredFile))
		else:
			if findFile(path, desiredFile)[0]:
				counter = counter + 1
				#string type for homework file path
				studentFilePaths.append(findFile(path, desiredFile)[1] + "/")
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
	fileName = hwPy if os.path.exists(filePath + hwPy) else hwPy

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

def checkAnswer(x):
	print x == answers[0]
	if not x == answers[0]:
		print x
		#openHw()
	del answers[0]

def problem6(filePath):
	output = ""
	inputLines = open(filePath + hwPy, "rt").readlines()
	print

	printBool = False
	for line in inputLines:
		if line == "# Big O\n" or line == "# problem6\n":
			print line
			printBool = True
		elif printBool:
			print line

def debugApostropheProblem(filePath):
	returnBool = False
	string = ""
	with open(filePath + hwPy) as fp:
		for i, line in enumerate(fp):
			#print line
			#raw_input()
			if "\x92" in line or "\xe2" in line:
				returnBool = True
				print
				print "Yes it was the apostrope problem\nNow we try to fix it"
				sleep(5)
				line = line.replace("\x92", " ")
				line = line.replace("\xe2", " ")
			string = string + line
		fp.close()
		fp = open(filePath + hwPy, "w")
		fp.write(string)
		fp.close
		return returnBool

def callFunctions(filePath):
	sys.path.append(filePath)
	global openHw
	openHw = lambda : os.startfile(filePath + hwPy)
	global answers
	answers = [14,14910,"a*b*c","s*m*a*s*h*m*o*u*t*h","(abd)","(1623)",4,7]

	try:
		hw = __import__(hwPy[:len(hwPy) - 3])
		openHw()
		reload(hw)
	except ImportError, e:
		openHw()
		hw = __import__(hwPy[:len(hwPy) - 3])
		reload(hw)
	except SyntaxError, e:
		print "Their code had a SyntaxError..."
		sleep(1)
		print "We are going to see if it's that apostrophe problem"
		sleep(1)
		if not debugApostropheProblem(filePath):
			print "hm it wasnt that"
			sleep(3)
			print e
			openHw()
		else:
			return

	try:
		print

		print "pyramid Test 1:",
		checkAnswer(hw.pyramid(3))

		print "pyramid Test 2:",
		checkAnswer(hw.pyramid(35))

		print "allStar Test 1:",
		checkAnswer(hw.allStar("abc"))

		print "allStar Test 2:",
		checkAnswer(hw.allStar("smashmouth"))

		print "parenBit Test 1:",
		checkAnswer(hw.parenBit("askdfjnskdfnas(abd)asdfkjns"))

		print "parenBit Test 2:",
		checkAnswer(hw.parenBit("askdfjnsk45cgdfnas(1623)asdfc4q3r4r"))

		print "xCounter Test 1:",
		checkAnswer(hw.xCounter("kajsdnfkjadsnxkjansdxkjansdfxkjandx", 0))

		print "xCounter Test 2:",
		checkAnswer(hw.xCounter("jaskdfjnxkajndxkajndxkajndxkajdnxkajndxklajndx", 0))

		print "\ncodingSong:",
		hw.codingSong(3)

		#problem6(filePath)
		print "Big O"
		sleep(3)
		#openHw()
		sys.path.remove(filePath)
	except AttributeError, e:
		print "AttributeError"
		print e
		sleep(3)
		openHw()
	except TypeError, e:
		print "TypeError"
		print e
	except NameError, e:
		print "NameError"
		print e
	except IndexError, e:
		print "IndexError"
		print e
	except Exception, e:
		raise e
		print
		raw_input("Oh no their code messed up...")
		openHw()

def scriptRunner():
	fileList = navigateAndStore("hw.py")
	counter = 0
	clear = lambda : os.system("cls")
	done = False
	for filePath in fileList:
		lastName = filePath.split("/")[5]
		prompt = "Do you want to grade " + lastName[:len(lastName) - 34] + "?"
		print lastName[:len(lastName) - 34]
		if str(raw_input(prompt)) == "y":
			setMediaPath2(filePath, True)
			while not done:
				callFunctions(filePath)

			setMediaPath2(filePath, False)
		counter = counter + 1
		clear()

#navigateAndStore("hw08.py")
#scriptRunner()

#print getNewCode()
#print open(currentPath + "gradingScript.py", "r").read()

#for item, key in sys.modules.iteritems():
	#	print item, key
	#	raw_input()


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
	Merge findFile and findFileExt for eloquence
"""

"""
	Make this file a library
"""

"""
	Maybe make gradingScript a class and call functions from it to make it more dynamic
"""

"""
	Dynamic grading. For the first several students I input
	my comments like normal but I will never repeat my self.
	The script will know that some error equals an equivalent comment
	and it will autofill the comment for me.
"""

"""
	Import JES's library.... duh
"""