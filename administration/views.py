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

class GenericLoginPage(auth_views.LoginView):
    """
    The login page EVERYONE should see at one point or another
    """

    template = "seek_login.html"
    # ltwc_user_regex = re.compile('[eEvV]\d{6')

    def post(self, request, *args, **kwargs):
        pass



        #     username = request.POST['username']
        #     existing_user = user_is_present(user_ids=[username])
        #
        #     if not existing_user:
        #         charter_user = LDAPUtils().get_ldap_user(username)
        #         logger.debug(f"Charter user is something like this:\n{charter_user}")
        #
        #         if charter_user:
        #             user_info = parse_ldap_user_dict(charter_user)
        #
        #             if settings.AUTHENTICATE_TO_CHARTER_LDAP:
        #                 return self.chartercom_authentication(user_info)
        #             elif settings.AUTHENTICATE_TO_CHARTER_VDS:
        #                 return self.chartercom_vds_authentication(user_info)
        #
        #             if not LDAPUtils().authenticate_user(
        #                 user_info["distinguishedName"],
        #                 self.request.POST["password"]
        #             ):
        #                 logger.warning(f"Failed login for user {user_info['distinguishedName']}")
        #                 return self.form_invalid(form)
        #
        #             if "email" not in user_info:
        #                 user_info["email"] = ""
        #             username_set = set([user_info["ldap_username"]],)
        #             if DEBUG:
        #                 logger.info(f"All the usernames: {username_set}")
        #             if settings.AUTHENTICATE_TO_LTWC_LDAP:
        #                 for location in settings.AUTH_LDAP_TWC_PID_LOCATIONS.split(','):
        #                     if location in user_info:
        #                         if user_info[location]:
        #                             username_set.add(user_info[location])
        #             existing_user = user_is_present(
        #                 user_ids=username_set,
        #                 email=user_info["email"]
        #             )
        #             if not existing_user:
        #                 from django_auth_ldap.backend import LDAPBackend
        #                 new_user = LDAPBackend().populate_user(user_info["ldap_username"])
        #
        #                 self.replace_username_in_request(user_info["ldap_username"])
        #
        #                 for group in AUTOMAGIC_ACCOUNT_GROUPS:
        #                     try:
        #                         new_user.groups.add(Group.objects.get(name=group))
        #                     except ObjectDoesNotExist:
        #                         logger.error(f"could not add group {group} to {new_user}. It doesn't seem to be REAL")
        #                     except Exception as oh_no:
        #                         logger.error(f"didn't add group {group} to {new_user}\n{oh_no}")
        #
        #                 new_profile = UserProfile.objects.create(
        #                     user=new_user,
        #                 )
        #                 if "manager_dn" in user_info:
        #                     new_profile.direct_superior_officer_dn = user_info["manager_dn"]
        #                     new_profile.save()
        #                 auth_login(self.request, new_user, 'django_auth_ldap.backend.LDAPBackend')
        #                 return HttpResponseRedirect(self.get_success_url())
        #             else:
        #                 self.replace_username_in_request(existing_user.username)
        #                 auth_login(self.request, existing_user, 'django_auth_ldap.backend.LDAPBackend')
        #                 return HttpResponseRedirect(self.get_success_url())
        #         return self.form_invalid(form)
        #     else:
        #         if settings.AUTHENTICATE_TO_CHARTER_VDS or settings.AUTHENTICATE_TO_CHARTER_LDAP:
        #             try:
        #                 existing_user.userprofile.validate_ldap_settings()
        #             except UserProfile.DoesNotExist:
        #                 if not existing_user.has_usable_password():
        #                     logger.warning(f"User {existing_user.username} has no associated user profile")
        #         logger.info(f"Log in the user {existing_user.username}")
        #         self.replace_username_in_request(existing_user.username)
        #
        # if form.is_valid():
        #
        #     auth_login(self.request, form.get_user())
        #     return HttpResponseRedirect(self.get_success_url())
        #
        # else:
        #     return self.form_invalid(form)
