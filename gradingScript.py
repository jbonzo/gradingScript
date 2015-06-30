"""
	1. Navigate through folders
		Use os.listdir() and loop through my students
		Use recursion?
	2. Call functions from files in script
		Use sys.path.append(path)
	2a. Account for getMediaPath()
		In order to account for getMediaPath() we must edit their code
	3. Read output.txt files and ensure they are similar to test case files
	4. Record how many are right vs wrong
	5. print score
"""

import sys
import os


bulkPathList = [
	"C:/Users/rbarillas3/Downloads/Bulk Download/",
	"D:/Users/Ricky/Downloads/Bulk Download/",
	"C:/Users/Ricky/Downloads/Bulk Download/"
]

bulkDownload = ""
textPath = "C:/Users/Ricky/Downloads/Bulk Download/Media Sources/text/"
#to make it compatible with any developing computer
for bulkPath in bulkPathList:
	if os.path.exists(bulkPath):
		bulkDownload = bulkPath

#List of student directories
students = os.listdir(bulkDownload)




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
	return textPath

def navigate():
	counter = 0
	#cycle through every student
	for student in students:
		#makes a path based on current student
		path = bulkDownload + student
		lastName = student.split(",")[0].strip()
		if findPYFile(path)[0]:
			counter = counter + 1
			#string type for homework file path
			return findPYFile(path)[1]

def callFunctions(filePath):
	sys.path.append(filePath)
	try:
		from hw06 import evenOdd
	except Exception, e:
		from HW06 import evenOdd

	evenOdd(textPath + "words.txt")
	sys.path.remove(filePath)
	open()


callFunctions(navigate())


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