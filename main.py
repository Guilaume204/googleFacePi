
import io
import os

import argparse
import sys


# Imports the Google Cloud client library
from google.cloud import vision


# def defaultActionPrint():
# 	print("Invalid argument, to see usage python main.py -h")

def getLabels(filename):
	
	# Instantiates a client
	vision_client = vision.Client()

	# The name of the image file to annotate
	file_name = os.path.join(os.path.dirname(__file__),'resources/'+filename)

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    image = vision_client.image(content=image_file.read())

	# Performs label detection on the image file
	labels = image.detect_labels()

	return labels

def main():

	filename = sys.argv[1]
	print("getting labels for "+filename)

	labels = getLabels(filename)

	print('Labels:')
	for label in labels:
	    print(label.description)



# parser = argparse.ArgumentParser()
# parser.add_argument('--labels', help='labels takes the name of an image stored in resources, ex. cat.jpg'
# 	, action='store_const'
# 	, default=defaultActionPrint
# 	, const=getLabels)
# args = parser.parse_args()

#calling main() function on script excecution
if __name__ == '__main__':
    main()