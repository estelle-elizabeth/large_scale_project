from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import user,truck,user_truck
from grpc_django.views import RetrieveGRPCView, ServerStreamGRPCView
from polls.order_pb2 import GetRequest as get



def index(request):
    data = truck.objects.all()
    list = {"truck_list": data}
    update = user_truck.objects.all()
    list2 = {"update_list": update}
    print(list2)
    return render(request, "polls/index.html", {"truck_list": data,"update_list": update})

def user(request, question_id):
    return HttpResponse("you're looking at order %s." % question_id)

def order(request):
    truck = request.POST.get('value')
    print(request)
    print(truck)
    print("am i getting anything?")
    return render(request, "polls/order_confirmed.html")

def update(request, question_id):
    print("IS THIS GOOD?")
    print(question_id)
    return HttpResponse('this is to update status')

def status(request, question_id):
    print(question_id)
    return HttpResponse('this is to get status')

class Getorder(RetrieveGRPCView):
    """
    RPC to view a single order by ID
    """
    queryset = user_truck.objects.all()
    response_proto = get


class ListUsers(ServerStreamGRPCView):
    """
    RPC to list all users
    """
    queryset = user_truck.objects.all()
    response_proto = get
