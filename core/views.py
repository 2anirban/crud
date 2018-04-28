from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Client
from .forms import ClientForm
from django.contrib.auth.decorators import login_required

def test_function(request):
    return HttpResponse("HelloWorld")


def list_clients(request):
    clients=Client.objects.all
    return render(request,"create.html",{"clients":clients})


def new_clients(request):
    form=ClientForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(list_clients)


    return render(request,'form.html',{'form':form})

@login_required
def update_client(request,id):
    client=get_object_or_404(Client,pk=id)

    form = ClientForm(request.POST or None,instance=client)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request, 'form.html', {'form': form})

@login_required
def delete_client(request,id):
    client=get_object_or_404(Client,pk=id)

    if request.method=="POST":
        client.delete()
        return redirect(list_clients)

    return render(request, 'confirm.html', {'client': client})