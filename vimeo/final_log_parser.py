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
	if (len(sys.argv)-1 < 3):	#Check for required arguments
		print ("Insufficient input parameters")
		print("USAGE : python log_parser.py <STARTTIME> <ENDTIME> </PATH/TO/LOGFILE/>")
		
	else:
		for file in range(3,len(sys.argv)):	#Check for log file path
			if path.exists((sys.argv)[file]):
				calc5xxRespPercentage((sys.argv)[1],(sys.argv)[1],(sys.argv)[file])
			else:	
				print ("Invalid filename or path not found : "+str((sys.argv)[file]))
				print("USAGE : python log_parser.py <STARTTIME> <ENDTIME> </PATH/TO/LOGFILE/>")
			

def calc5xxRespPercentage(startTime,EndTime,fileName):
	print ("Between time "+str((sys.argv)[1])+" and time "+str((sys.argv)[2])+" :")
	
	with open(fileName, "r") as read_file:
		for line in read_file:
			split_line_list = line.split('|')
			logtime = float(split_line_list[0])
			starttime = float(sys.argv[1])
			endtime = float(sys.argv[2])
			if (starttime <= logtime < endtime):
				if (500 <= int(split_line_list[4].strip()) < 600):
					domainErrors["total5xxCount"]+=1
					if (split_line_list[2].strip() not in domainErrors.keys()):
						domainErrors[split_line_list[2].strip()] = 1
					else:
						domainErrors[split_line_list[2].strip()]+=1
	if (len(domainErrors)==1):
		print("No 5xx errors were logged")
	else:
		for domain,count in domainErrors.items():
			if domain != "total5xxCount":
				print (str(domain)+" returned "+str((100*count)/domainErrors["total5xxCount"]) +"% 5xx errors")
	
					
if __name__ == '__main__':
	
	main()
