# googleFacePi

This project is set up using https://cloud.google.com/vision/docs/face-tutorial\
To learn more about gcloud command-line commands, see the gcloud Tool Guide @ https://cloud.google.com/sdk/gcloud.

This program uses the python library 'argparse' to aid with command line argument management, documentation can be found @ https://docs.python.org/3.3/library/argparse.html


## Instalation Requirements

Install the Google Client Library
run this a few times if you get any errors

	pip install --upgrade google-cloud-vision 

The following example shows how to use the client library. To run it on your local workstation you must first install the Google Cloud SDK from https://cloud.google.com/sdk/docs/. To check if your pc is 32bit or 64bit run (OSX or Linux)

	uname -m

authenticate by running the following command:

	gcloud auth application-default login

Install Python.
API reference.

Install pillow.
	
	pip install pillow