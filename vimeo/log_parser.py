"""
Date: 01/13/2020
Author: nitish.seshachala@gmail.com
Goal: Log parser to calculate % 5XX errors for each domain in a specific window

"""

#!/usr/bin/python
import sys
import os.path
from os import path

domainErrors = {"total5xxCount":0}  #Initial counter for 5xx errors

def logParser():

```
Validates input parameters and calls calc5xxRespPercentage()
input: <STARTTIME> <ENDTIME> </PATH/TO/LOGFILE/>
```
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

```
Calculates HTTP 5xx errors broken down by domain, for a given timeframe.
 
```
	with open(fileName, "r") as read_file:
		print ("Between time "+str((sys.argv)[1])+" and time "+str((sys.argv)[2])+" in file "+fileName+":")
		for line in read_file:
			split_line_list = [line.strip() for line in line.split('|')]
			if (len(split_line_list) != 1): 
				logtime = float(split_line_list[0])
				starttime = float(sys.argv[1])
				endtime = float(sys.argv[2])
				if (starttime <= logtime < endtime):				#Count number of 5xx
					if (500 <= int(split_line_list[4].strip()) < 600):
						domainErrors["total5xxCount"]+=1
						if (split_line_list[2].strip() not in domainErrors.keys()): #Append to existing domain or create new domain key
							domainErrors[split_line_list[2].strip()] = 1
						else:
							domainErrors[split_line_list[2].strip()]+=1
	if (len(domainErrors)==1):
		print("No 5xx errors were logged")
	else:
		for domain,count in domainErrors.items():
			if domain != "total5xxCount":
				print (str(domain)+" returned "+str((100*count)/domainErrors["total5xxCount"]) +"% 5xx errors") #Calculate percentage
	
					
if __name__ == '__main__':
	
	logParser()
