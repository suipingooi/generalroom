from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import ClientRequest, crAdmin
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
    cr_to_edit = get_object_or_404(ClientRequest, pk=tenant_id)
    cr_form = ClientRequestForm(instance=cr_to_edit)
    if request.method == "POST":
        a_form = AdminForm(request.POST)
        if a_form.is_valid():
            followup = a_form.save(commit=False)
            followup.manager = request.user
            followup.crequest = cr_to_edit
            followup.save()
            cr_to_edit.remarks = get_object_or_404(crAdmin, pk=followup.id)
            cr_to_edit.save(update_fields=['remarks'])

            messages.success(request, 'Client Details Updated')
            return redirect(reverse(client_list))
        else:
            messages.error(
                request, 'Action Unsuccessful, Please check error fields')
            return render(request, 'tenants/client_update-template.html', {
                'cr_form': cr_form,
                'a_form': a_form,
                'tenant': cr_to_edit
            })
    else:
        messages.info(request, 'You creating followup to a client request')
        a_form = AdminForm()
        return render(request, 'tenants/client_update-template.html', {
            'cr_form': cr_form,
            'a_form': a_form,
            'tenant': cr_to_edit
        })
    return render(request, 'tenants/client_list-template.html', {
        'cr_form': cr_form,
        'a_form': a_form,
        'tenant': cr_to_edit
    })
