#!/usr/bin/env python3
import io
import os
import argparse
import sys
import logging

from google.cloud import vision # Imports the Google Cloud client library

#Set constants
PWD = os.path.dirname(__file__)

#Create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
LOG_FILE = os.path.join(PWD,"gVizAPI.log")
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG,
	format = LOG_FORMAT,
	filemode = "a")

#root logger
logger = logging.getLogger()

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
		
	vision_client = vision.Client() # Instantiates a client
	file_name = os.path.join(os.path.dirname(__file__),filename)# The name of the image file to annotate

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    image = vision_client.image(content=image_file.read())

	# Performs label detection on the image file
	labels = image.detect_labels()

	#log results as free google vision cloud API only has 1000 image request/month
	logger.info("labels for {0} ".format(str([label.description for label in labels])))
	return labels

def main():
	"""
	main function called using if __name__ == '__main__':, 'nuff said.
	"""
	logger.info("main() Executed with logger.level="+str(logger.level))
	filename = sys.argv[1]
	print("getting labels for "+filename)

	labels = getLabels(filename)

	print('Labels:')
	for label in labels:
	    print(label.description)

# next on the agenda...

# def defaultActionPrint():
# 	print("Invalid argument, to see usage python main.py -h")

# parser = argparse.ArgumentParser()
# parser.add_argument('--labels', help='labels takes the name of an image stored in resources, ex. cat.jpg'
# 	, action='store_const'
# 	, default=defaultActionPrint
# 	, const=getLabels)
# args = parser.parse_args()

# calling main() function on script excecution

if __name__ == '__main__':
    main()