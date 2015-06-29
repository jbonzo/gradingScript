"""
	1. Navigate through folders and place script inside
		Use os.listdir() and loop through my students
	2. Call functions from files in script
		Use sys.path.append(path)
	3. Read output.txt files and ensure they are similar to test case files
	4. Record how many are right vs wrong
	5. print score
"""

import sys
import os

path = "C:\Users/rbarillas3\Desktop\RabbitHole".replace("\\", "/")
sys.path.append(path)

from sandbox import test

print len(sys.path)

print test()
