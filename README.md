# Crypto_project
 

## Containerizing an Asymmetric Key-Gen App 


## Problem Statement
This project is mainly based on creating an asymmetric key-gen app using python programming language. Then using flask to create an API for it and containerizing it using Docker.
## Brief description
The project is mainly intended to create a Highly Advance Security (HAS) platform that uses asymmetric keys to  encrypt data.
These keys are generated using the RSA algorithm. It is provided as a module in Python from pycrypto. We use the Crypto.PublicKey class to achieve this.
The algorithm can be used for both confidentiality (encryption) and authentication (digital signature).
Here, we are creating a key-gen app which generates new public and private keys to encode our messages everytime we put up a request.

## Proposed Solution
Using the above mentioned class, we generate an API using the flask module in Python
We create a flask API and deploy the module using the WSGI server Gunicorn. This helps us in scaling the application in a robust way and since it uses threading and workers to allocate the processes, we can increase the efficiency of the API manifold.
This entire system is then containerized using Docker. 
To achieve this, we build a Dockerfile, which basically imports a pre-built Linux based Python3.6 docker image. 
Upon building this image, we then copy necessary files into the app folder.
Then we install all the required packages required to run the app.
Then we expose the port in which we would want to access the api.
Then we start the gunicorn server inside the docker system.
Now, we can open a new terminal or browser and check for the output.
For ease of use, the host:port numbers has been set to 0.0.0.0:80. So, we can use the command - 
“curl -X GET --url http://0.0.0.0:80”

## Block diagram

## Instructions
Run commands -
 “docker pull chiru1995/crypto_project”
“docker run -p 80:80 chiru1995/crypto_project”
“curl -X GET --url http://0.0.0.0:80” (This command to be run in a different terminal to get the output)
## Sample Test Results

![Alt text](https://github.com/chiranthancv95/Crypto_project/blob/main/app%20running.png?raw=true "App running in Docker")
			Figure a - App running in Docker

			FIgure b - An image of the output
## Future Scope
Possible improvements for this project are to use better and latest algorithms for generating key-gen more efficiently.
We can use django to create an api which has better features and services compared to flask and flask_restful modules
We can use better deployment servers for higher efficiency in running the applications for better handling and robustness.
We can set the number of worker threads based on the instance on which we would deploy the app on.  
