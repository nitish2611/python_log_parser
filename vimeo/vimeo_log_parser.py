"""
Date: 01/11/2020
Author: nitish.seshachala@gmail.com
Goal: Log parser to calculate % 5XX errors for each domain in a specific window

Usage:
    python vimeo_log_parser.py 1493969101.638 1493969101.667 log_sample.txt /var/log/a.txt b.txt c.txt 

Note: 
	1. specify full path for the file or the script will only look in the working directory
	2. Each input is seperated by a space the order is Start Time, End Time, List of files
	3. If the number of parameters is less than 3 the program will output an error message to provide required parameters.
	4. If there is an invalid file , the program will handle invalid file or path exception : <file/path name>

"""

#!/usr/bin/python
import sys
import os.path
from os import path

domainErrors = {"total5xxCount":0}  #Initial counter for 5xx errors

def main():
	if (len(sys.argv)-1 < 3):
		print ("insuffecient input parameters")
	else:
		#if (isinstance(sys.argv[1],float) and isinstance(sys.argv[2],float)):
		for file in range(3,len(sys.argv)):
			if path.exists((sys.argv)[file]):
				calc5xxRespPercentage((sys.argv)[1],(sys.argv)[2],(sys.argv)[file])
			else:
				print ("invalid file or path : "+str((sys.argv)[file]))
		print ("Between time "+str((sys.argv)[1])+" and time "+str((sys.argv)[2])+" :")
		if (len(domainErrors)==1) :
			print ("No 5xx errors were logged")
		else:
			for k,v in domainErrors.items():
				if k != "total5xxCount":
					print (str(k)+" returned "+str((100*v)/domainErrors["total5xxCount"]) +"% 5xx errors")
		#else:
			#print ("Invalid input parameters")



def calc5xxRespPercentage(startTime,EndTime,fileName):
	with open(fileName, "r") as read_file:
		for line in read_file:
			split_line_list = line.split('|')
			if (float(startTime) <= float(split_line_list[0].strip()) < float(EndTime)):
				if (500 <= int(split_line_list[4].strip()) < 600):
					domainErrors["total5xxCount"]+=1
					if (split_line_list[2].strip()) not in domainErrors.keys():
						domainErrors[split_line_list[2].strip()] = 1
					else:
						domainErrors[split_line_list[2].strip()]+=1
					
if __name__ == '__main__':
	
	main()
