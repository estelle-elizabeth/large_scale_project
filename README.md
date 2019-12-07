# Large Scale Project


# Group Members:
		Estelle Ocran
		Won Jong Yang 
		Jack Xu


# Instructions on how to initialize server:



#Instructions to get Redis Running
- run this command from your command line
- pip install redis
- install the appropriate redis package for your operating system from the redis website
- run the redis-server exe from the redis package folder you downloaded

# Instructions on how to build and run GRPC code.

- Language of choice - Python for both server and client
-There are two RPC calls; SetState (to set the state of the order) and GetState (to get the state of the order)


#How to invoke protoc in order to generate the stubs
- run these commands from within the folder the protoc is located
- python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./order.proto


# How to run the GRPC server (on localhost)
- python order_server.py
-run this on another terminal (not the same as the one the client is running on)

# How to invoke GRPC client tool
- python order_client.py <get|set> orderID
- eg. python order_client.py get "1234"
- eg. python order_client.py set "1234"

- Voila! You should have a response now :).




