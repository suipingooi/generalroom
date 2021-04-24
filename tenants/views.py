from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm, ViewRequestForm
from django.contrib import messages
# Create your views here.

# CRUD tenant-client / CRM


def add_client(request):
    if request.method == 'POST':
        view_request_form = ViewRequestForm(request.POST)
        client_form = ClientForm(request.POST)
        if client_form.is_valid() and view_request_form.is_valid():
            client_form.save()
            view_request_form.save()
            messages.success(request, 'Details Submitted')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'tenants/client_add-template.html', {
                'c_form': client_form,
                'vr_form': view_request_form
            })
    else:
        client_form = ClientForm()
        return render(request, 'tenants/client_add-template.html', {
            'c_form': client_form,
            'vr_form': view_request_form
        })


def client_list(request):
    tenant = Client.objects.all().order_by('-id')
    return render(request, 'tenants/client_list-template.html', {
        'tenant': tenant
    })


def edit_client(request, client_id):
    client_to_edit = get_object_or_404(Client, pk=client_id)
    if request.method == "POST":
        client_form = ClientForm(request.POST, instance=client_to_edit)
        if client_form.is_valid():
            client_form.save()
            messages.success(request, 'Client Details Updated')
            return redirect(reverse(client_list))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'tenants/client_update-template.html', {
                'form': client_form,
                'tenant': client_to_edit
            })
    else:
        messages.info(request, 'EDIT action will overwrite data')
        client_form = ClientForm(instance=client_to_edit)
        return render(request, 'tenants/client_update-template.html', {
            'form': client_form,
            'tenant': client_to_edit
        })
    return render(request, 'tenants/client_list-template.html', {
        'tenant': client_to_edit
    })


def delete_client(request, client_id):
    client_to_del = get_object_or_404(Client, pk=client_id)
    if request.method == "POST":
        client_to_del.delete()
        messages.success(request, 'Client Data Deleted')
        return redirect(client_list)
    else:
        messages.warning(request, 'DELETE action cannot be undone')
        return render(request, 'tenants/client_delete-template.html', {
            'tenant': client_to_del
        })
