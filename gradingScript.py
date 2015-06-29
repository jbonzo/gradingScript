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
	#if os.listdir(path) contains a .py file then return true
	#else dig deeper

	items = os.listdir(path)
	if "hw04.py" in items or "HW04.py" in items:
		return True
	elif len(items) > 0:
		return findPYFile(path + "/" + items[0])
	else:
		return False

#for item in os.listdir(path):
#	print item
#	break

#sys.path.append(path)

#from sandbox import test

#print len(sys.path)

#print test()

def navigate():
	for student in students:
		path = bulkDownload + student
		lastName = student.split(",")[0]
		if not findPYFile(path):
			print "%s contains the homework file: %s \n" % (lastName, findPYFile(path))

navigate()