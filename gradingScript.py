"""
	1. Navigate through folders
		Use os.listdir() and loop through my students
		Use recursion?
	2. Call functions from files in script
		Use sys.path.append(path)
	2a. Account for getMediaPath()
	3. Read output.txt files and ensure they are similar to test case files
	4. Record how many are right vs wrong
	5. print score
"""

import sys
import os

bulkDownload = "C:\Users/rbarillas3\Downloads\Bulk Download/".replace("\\", "/")
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
	if "hw01.py" in items or "HW01.py" in items:
		return (True, path)
	elif os.path.isdir(newPath):
		return findPYFile(newPath)
	else:
		return (False, "")

def navigate():
	#cycle through every student
	for student in students:
		#makes a path based on current student
		path = bulkDownload + student
		lastName = student.split(",")[0]
		if findPYFile(path)[0]:
			sys.path.append(findPYFile(path)[1])
			try:
				from hw01 import speak
			except Exception, e:
				from HW01 import speak
			speak()
			sys.path.remove(findPYFile(path)[1])
		#print "%s contains the homework file: %s \n" % (lastName, findPYFile(path))

navigate()