from django.shortcuts import render
from customer.forms import CreateCustomerForm
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View
from administration.models import Customer
from django.contrib.auth.decorators import permission_required


class CustomerMain(View):
    """
    This view is a for a user enter customer information
    """

    def dispatch(self, *args, **kwargs):
        """directs to get and posts
                :param args:
                :param kwargs:
                :return:
        """
        return super().dispatch(*args, **kwargs)

    @method_decorator(permission_required('access_customer_form', login_url='unauthorized_page'))
    def get(self, request):
        """
        Accepts a user_identifier and returns a formatted table with that user's information, if a user is found
        :param request:
        :param user_identifier:
        :return:
        """
        # self.session = requests.Session()
        # access = rest_login(self)
        self.request = request
        self.template = 'customer_main.html'
        # HEADERS['Authorization'] = f"Bearer {access['access_token']}"
        # #params = {'containerName':'Commercial/LBHN/Bakersfield/Customer'}
        # params = 'Commercial/LBHN/Bakersfield/Customer'
        #
        # #Populate Re
        # regions = get_region(self, params)
        # context_dict = {"region": regions.text }

        # return render(request, self.template, fill_footer_parameters({}, request))
        return render(request, self.template)

    def post(self, request):
        pass