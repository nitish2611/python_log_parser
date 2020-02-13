#Python log parser

Simple python script to calculate percentage of HTTP 5xx errors for each domain in the log file, for a given timeframe.

##Invocation of script

```python log_parser.py <STARTTIME> <ENDTIME> </PATH/TO/LOGFILE/>```

Run ```python log_parser.py 1493969101.638 1493969101.668 log_sample.txt```

Output: 
Between time 1493969101.638 and time 1493969101.668 :
player.vimeo.com returned 66.66666666666667% 5xx errors
vimeo.com returned 33.333333333333336% 5xx errors


##Assumptions
   1: Python 3 is already installed on the machine. This script is python 3 compatible.
   2: Specify full path for the file or the script will only look in the working directory.
   3: If the number of input parameters is less than 3, the script will display the right usage and exits.
   4: Script checks for valid file path/name, the program will print an error message as invalid file or path 
   

##Additional
  1: vimeo/manifests/init.pp can be utilized to add to configuration management-puppet.

