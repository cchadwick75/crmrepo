import logging
from django.shortcuts import render, redirect
from collections import OrderedDict
from customer.forms import CreateCustomerForm
from django.http import JsonResponse
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from administration.models import Customer
from django.contrib.auth.decorators import permission_required

LOGGER = logging.getLogger('')

class CustomerMain(View):
    """
    This view is a for a user enter customer information
    """

    template_name = "customer_main.html"
    form_class = CreateCustomerForm

    @method_decorator(permission_required('access_customer_form', login_url='unauthorized_page'))
    def get(self, request):
        '''

        get - basis is to do the customer validation
        :param request:
        :return:
        '''

        form = self.form_class

        form_name = request.GET.get('name')
        form_address1 = request.GET.get('phone')

        if form_name:

            is_taken = Customer.objects.filter(name__icontains=form_name).exists()
            data = {'is_taken': is_taken}
            try:

                data = {'is_taken': is_taken}

                #     message = 'Valid'
                #     data["NAME"] = []
                #     for i in result:
                #         data["LOCATION_NAME"].append(i["LOCATION_NAME"])
                #
                #     data['CITY'] = result[0]["CITY"]
                #     data['STATE'] = result[0]["STATE"]
                #     data['STREET_ADDRESS'] = result[0]["STREET_ADDRESS"]
                #     data['ZIP_CODE'] = result[0]["ZIP_CODE"]
                #     data['LOCATION_TYPE'] = 2  # default value for Business.
                # else:
                #     message = 'Invalid'
                #
                # data['granite_response'] = message

            except Exception as no_response:

                error_type = 'WARNING'
                message = 'registration encountered an invalid user'
                log_dict = OrderedDict({
                    'program': "{}.{}".format(__name__, self.__class__.__name__),
                    'method': "GET",
                    'log_level': error_type,
                    'user': request.user,
                    'message': message,
                    'exception_error': no_response
                })

                LOGGER.error(log_dict)
            data['loc_id'] = []
            if data['is_taken']:
                location_count = Customer.objects.filter(name__icontains=form_name).count()
                if location_count >= 1:
                    location_id = Customer.objects.filter(name__icontains=form_name).values_list('id', flat=True)

                    for loc_id in location_id:
                        data['loc_id'].append(loc_id)

            return JsonResponse(data)
        return render(request, self.template_name, {'form': form})

    @method_decorator(permission_required('access_customer_form', login_url='unauthorized_page'))
    def post(self, request):
        '''

        :param request:
        :return: redirects to customer page after the new customer is posted to oceanicnet
        '''

        form = self.form_class(request.POST)

        if form.is_valid():
            data = form.save()
            return redirect('/customer/', {"message":'Customer Successfully Added'})
        return redirect('/customer/', {"message": 'Not Added Check Your Data'})