from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import ClientRequest
from .forms import ClientRequestForm
from django.contrib import messages

# Create your views here.

# CRUD tenant-client / CRM


def add_client(request):
    if request.method == 'POST':
        clientrequest_form = ClientRequestForm(request.POST)
        if clientrequest_form.is_valid():
            clientrequest_form.save()
            messages.success(
                request, 'Details Submitted, A confirmation call will follow within 24hrs')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'tenants/client_add-template.html', {
                'cr_form': clientrequest_form,
            })
    else:
        clientrequest_form = ClientRequestForm()
        return render(request, 'tenants/client_add-template.html', {
            'cr_form': clientrequest_form,
        })


def client_list(request):
    tenant = ClientRequest.objects.all()
    return render(request, 'tenants/client_list-template.html', {
        'tenant': tenant,
    })


def edit_client(request, request_id):
    client_to_edit = get_object_or_404(ClientRequest, pk=request_id)
    if request.method == "POST":
        clientrequest_form = ClientRequestForm(
            request.POST, instance=client_to_edit)
        if clientrequest_form.is_valid():
            clientrequest_form.save()
            messages.success(request, 'Client Details Updated')
            return redirect(reverse(client_list))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'tenants/client_update-template.html', {
                'form': clientrequest_form,
                'tenant': client_to_edit
            })
    else:
        messages.info(request, 'EDIT action will overwrite data')
        clientrequest_form = ClientRequestForm(instance=client_to_edit)
        return render(request, 'tenants/client_update-template.html', {
            'form': clientrequest_form,
            'tenant': client_to_edit
        })
    return render(request, 'tenants/client_list-template.html', {
        'tenant': client_to_edit
    })


def delete_client(request, request_id):
    client_to_del = get_object_or_404(ClientRequest, pk=request_id)
    if request.method == "POST":
        client_to_del.delete()
        messages.success(request, 'Client Data Deleted')
        return redirect(client_list)
    else:
        messages.warning(request, 'DELETE action cannot be undone')
        return render(request, 'tenants/client_delete-template.html', {
            'tenant': client_to_del
        })
