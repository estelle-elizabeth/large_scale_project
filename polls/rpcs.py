from grpc_django.interfaces import rpc
from .views import Getorder, ListUsers


rpcs = [
    rpc(name='Getorder', view=Getorder),
    rpc(name='ListUsers', view=ListUsers)
]
