from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import ClientRequest
from .forms import ClientRequestForm, QForm, AdminForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.

# CRUD tenant-client / CRM


def add_client(request):
    if request.method == 'POST':
        clientrequest_form = ClientRequestForm(request.POST)
        if clientrequest_form.is_valid():
            clientrequest_form.save()
            messages.success(
                request, ('Details Submitted! A confirmation call'
                          + ' will follow within 24hrs.'))
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
    q_form = QForm(request.GET)
    tenant = ClientRequest.objects.all()
    query = ~Q(pk__in=[])
    if 'name' in request.GET and request.GET['name']:
        query = query & (Q(first_name__icontains=request.GET['name']) | Q(
            last_name__icontains=request.GET['name']))

    if 'company' in request.GET and request.GET['company']:
        query = query & Q(
            company_name__icontains=request.GET['company'])

    if 'date' in request.GET and request.GET['date']:
        query = query & Q(
            viewing_date__month=request.GET['date'])

    tenant = tenant.filter(query).values().distinct()

    return render(request, 'tenants/client_list-template.html', {
        'tenant': tenant,
        'Qform': q_form
    })


def edit_client(request, tenant_id):
    client_to_edit = get_object_or_404(ClientRequest, pk=tenant_id)
    if request.method == "POST":
        admin_form = AdminForm(
            request.POST, instance=client_to_edit)
        if admin_form.is_valid():
            admin_form.save()
            messages.success(request, 'Client Details Updated')
            return redirect(reverse(client_list))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'tenants/client_update-template.html', {
                'form': admin_form,
                'tenant': client_to_edit
            })
    else:
        messages.info(request, 'EDIT action will overwrite data')
        admin_form = AdminForm(instance=client_to_edit)
        return render(request, 'tenants/client_update-template.html', {
            'form': admin_form,
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
