"""
Views which allow users to create and activate accounts.

"""

import logging

from django.shortcuts import redirect

logger = logging.getLogger('')
def home_redirect(request):
    """
    All people going to the url are redirected to the customer
    :param request:
    :return:
    """
    return redirect('/customer/')