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
import json

InputFile = "README.md"

##The regular expression to check each line is
## \*\s\[.*\]\(https?://(www.)?.*\)\s-\s[[[\w|\s|\-|\*|\,\.]*]*\.\n

# Read every line and extract name, url and locations
def decompose_entry(line):
	# Not pretty but does the job
	result1 = re.split("(\*\s)",line)

	company_name = str(re.findall("\[.*\]",result1[2]))
	company_name = company_name.replace("[","").replace("]","")
	company_name = company_name.replace("'","")
	company_name = str(company_name)

	result2 = re.split("\[.*\]",result1[2])
	
	url = re.findall("https?://.*\/",str(result2[1]))
	url = str(url[0])

	result3 = re.split("\(https?://(www.)?.*\)\s-\s",result2[1])

	locations = result3[2]
	locations = locations.replace(".","").replace("*","").rstrip().split(",")

	return url, {"name":company_name, "locations":locations}

def check_entry(line):
	#print line
	regex_patter = re.compile("\*\s\[.*\]\(https?://(www.)?.*\/\)\s-\s[[[\w|\s|\-|\*|\,\.]*]*\.\n")
	if regex_patter.match(line) != None:
		return True
	else:
		print "This line has not a correct syntax, please check: ", line
		return False


def main():
	print "Starting mdtojson"

	output_dict = {}

	print "Checking if README.md exists"
	if(os.path.isfile(InputFile)):

		print "Readme.md exists"
		print "Processing...please wait"
		ifile = open(InputFile,'r')

		for line in ifile:
			if (line.startswith("*")):
				if check_entry(line):
					key, value = decompose_entry(line)
					#print key
					#print value['name']
					output_dict[key] = value


		#print output_dict

		# TODO: Check return values of write!
		with open('vfx-facilities.json', 'w') as ofile:
			json.dump(output_dict, ofile)

		print "Done!"

	else:
		print "README.md does not exists"
		print "Shutting down...bye..bye..."

if __name__=="__main__":
	main()