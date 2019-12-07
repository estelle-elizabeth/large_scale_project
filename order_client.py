from __future__ import print_function
import logging

import grpc
import sys


import order_pb2_grpc
import order_pb2

#!/usr/bin/env python






def run():
	task = sys.argv[1]
	order = int(sys.argv[2])
	channel = grpc.insecure_channel('localhost:50051')
	stub = order_pb2_grpc.OrderStub(channel)
	if task == 'get':
		response = stub.GetState(order_pb2.GetRequest(orderID=order))
		print(response.answer)

	
	elif task == 'set':
		response = stub.SetState(order_pb2.SetRequest(orderID=order))
		print(response.answer)
	

if __name__ == '__main__':
	logging.basicConfig()
	run()