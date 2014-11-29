#############################################################################
#############################################################################
## Project     : vfx-facilities - List of vfx facilities
## File        : mdtojson.py
## Contributors: Jathavan Sriram - vfx.engineering
##
## Summary     : This small script converts the README.md with all entries
##				 into a json to be used with watable or another json table
##				 generator for the website.
##
## 
## Note        : Keep in mind the README.md needs specific formatting! 
##
#############################################################################
#############################################################################
import argparse
import os.path
import re

InputFile = "README.md"

##The regular expression to check each line is
## \*\s\[.*\]\(https?://(www.)?.*\)\s-\s[[[\w|\s|\-|\*|\,\.]*]*\.\n

def decompose_entry(line):
	tmp_dict = {}
	result1 = re.split("(\*\s)",line)
	print result1




	return tmp_dict

def check_entry(line):
	#print line
	regex_patter = re.compile("\*\s\[.*\]\(https?://(www.)?.*\)\s-\s[[[\w|\s|\-|\*|\,\.]*]*\.\n")
	if regex_patter.match(line) != None:
		return True
	else:
		print "This line has not a correct syntax: ", line
		return False


def main():
	print "Starting mdtojson"

	output_dict = {}
	fac_list = []

	print "Checking if README.md exits"
	if(os.path.isfile(InputFile)):

		print "File exists"
		ifile = open(InputFile,'r')

		for line in ifile:
			if (line.startswith("*")):
				if check_entry(line):
					fac_list.append(decompose_entry(line))

		#print fac_list

	else:
		print "README.md does not exists"
		print "Shutting down...bye..bye..."

if __name__=="__main__":
	main()