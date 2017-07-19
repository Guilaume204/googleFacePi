
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--foo', help='foo help')
# args = parser.parse_args()

# def defaultActionPrint():
# 	print("Invalid argument, to see usage python main.py -h")
# In [133]: def act2():
#      ...:     print('act2')
#      ...:     
# In [134]: parser=argparse.ArgumentParser()
# In [135]: parser.add_argument('-a',action='store_const',default=act1,const=act2);


import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

def getLabels():
	# Instantiates a client
	vision_client = vision.Client()

	# The name of the image file to annotate
	file_name = os.path.join(os.path.dirname(__file__),'resources/car_me_and_a_naartjie.jpg')

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    image = vision_client.image(content=image_file.read())

	# Performs label detection on the image file
	labels = image.detect_labels()

	return labels



def main():
	print("getting labels")
	labels = getLabels()

	print('Labels:')
	for label in labels:
	    print(label.description)

#calling main() function on script excecution
if __name__ == '__main__':
    main()