import order_pb2_grpc
import order_pb2
import redis


from concurrent import futures
import logging

import grpc

r = redis.Redis(
    host = "localhost",
    port = 6379,
    password = "")

class Order(order_pb2_grpc.OrderServicer):

	def GetState(self, request, context):
		order = str(request.orderID)

		state = r.get(order)

		return order_pb2.GetReply(answer = state)
			


	def SetState(self, request, context):
		order = str(request.orderID)
		state = request.state

		r.set(order, state)

		return order_pb2.SetReply(answer = order + " has been " + state)




def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServicer_to_server(Order(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()