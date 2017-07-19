#!/usr/bin/env python3

import io
import os
import argparse
import sys
import time

import logging

PWD = os.path.dirname(__file__)

#Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
LOG_FILE = os.path.join(PWD,"gVizAPI.log")
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
	format = LOG_FORMAT,
	filemode = "a")

#root logger
logger = logging.getLogger()





# Imports the Google Cloud client library
from google.cloud import vision

# def defaultActionPrint():
# 	print("Invalid argument, to see usage python main.py -h")

def getLabels(filename):
	"""
	Creates vision API client using from google.cloud import vision

	Parameters
	==========
	filename: str : looks like resouces/cat.jpg

	Returns
	========
	labels: list : list of labels identified in filename
	"""

	logger.info("getLabels({0})".format(filename))
	
	# Instantiates a client
	vision_client = vision.Client()

	# The name of the image file to annotate
	file_name = os.path.join(os.path.dirname(__file__),filename)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    image = vision_client.image(content=image_file.read())

	# Performs label detection on the image file
	labels = image.detect_labels()

	logger.info("labels for {0} ".format(str([label.description for label in labels])))

	return labels

def main():
	logger.info("main() Executed with logger.level="+str(logger.level))
	filename = sys.argv[1]
	print("getting labels for "+filename)

	labels = getLabels(filename)

	print('Labels:')
	for label in labels:
	    print(label.description)


	print(filename)
	print(PWD)
	print("executed")



# parser = argparse.ArgumentParser()
# parser.add_argument('--labels', help='labels takes the name of an image stored in resources, ex. cat.jpg'
# 	, action='store_const'
# 	, default=defaultActionPrint
# 	, const=getLabels)
# args = parser.parse_args()

# calling main() function on script excecution


if __name__ == '__main__':
    main()