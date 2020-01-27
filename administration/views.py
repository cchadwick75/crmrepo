from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from django.contrib.auth import views as auth_views, login as auth_login

# Create your views here.

class AdminMain(View):
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

    def get(self, request):
        """
        Accepts a user_identifier and returns a formatted table with that user's information, if a user is found
        :param request:
        :param user_identifier:
        :return:
        """

        self.request = request
        self.template = 'customer_main.html'

        return render(request, self.template)

    def post(self, request):
        pass

class GenericLoginPage(auth_views.LoginView):
    """
    The login page EVERYONE should see at one point or another
    """

    template = "seek_login.html"
    # ltwc_user_regex = re.compile('[eEvV]\d{6')

    def post(self, request, *args, **kwargs):
        pass




