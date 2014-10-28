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

InputFile = "README.md"

def main():
	print "Starting mdtojson"

	print "Checking if README.md exits"
	if(os.path.isfile(InputFile)):
		print "File exists"
		fac_json = {}
		ifile = open(InputFile,'r')
		for line in ifile:
			if (line.startswith("*")):
				entry = line.split('[') ### Work with regex....anything does not work!
				print entry

	else:
		print "README.md does not exists"
		print "Shutting down...bye..bye..."

if __name__=="__main__":
	main()