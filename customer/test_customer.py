import time
import string
from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, HASH_SESSION_KEY, SESSION_KEY
from django.contrib.auth.models import User
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from model_mommy import mommy
import random
from administration.models import Customer
from selenium.common.exceptions import NoSuchElementException, UnexpectedTagNameException


class LocationCreateTest(StaticLiveServerTestCase):
    '''
    This is the full test class that will check the location create.
    '''
    fixtures = ['location_create_group_permissions.yaml', 'location_create_dashboard_filter_tests.yaml']
    display = None
    browser = None

    @classmethod
    def setUpClass(cls):

        # Setup a display for use by the selenium tests
        cls.display = Display(visible=0, size=(1024, 768))
        cls.display.start()

        # Probably should make it configurable which browser to use for the test
        cls.browser = webdriver.Chrome()
        # cls.browser = webdriver.Firefox()
        super(LocationCreateTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        '''
        breaks down the test browser session
        :return:
        '''
        cls.browser.quit()
        cls.display.stop()
        super(LocationCreateTest, cls).tearDownClass()

    def create_pre_authenticated_session(self, username):
        """Helper function that creates a pre-authenticated admin session"""
        user = User.objects.get(username=username)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session[HASH_SESSION_KEY] = user.get_session_auth_hash()
        session.save()
        # To set a cookie we need to first visit the domain.  404 pages load the quickest!
        self.browser.get(self.live_server_url + "/customer/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            secure=False,
            path='/',
        ))
        self.browser.refresh()



    def test_existing_location_button(self):
        '''
        This ensures the location link uses the  works correctly on the location page.
        :return:
        '''
        self.digits = string.digits
        self.letters = string.letters

        testing_customer = mommy.make(Customer,
                   name='Washington High',
                   city=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address2=(u''.join(
                       random.choice(self.letters) for _ in range(10))),

                   zip_code=(
                       u''.join(random.choice(self.digits) for _ in range(5)))
                   )
        mommy.make(Customer,
                   name=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   city='Washington',
                   street_address=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address2=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   region='SC',
                   zip_code=(
                       u''.join(random.choice(self.digits) for _ in range(5)))
                   )


        wd_wait = WebDriverWait(self.browser, 10)
        # This will create an actual location for testing purposes and also the location management button
        # when a location exists.
        self.create_pre_authenticated_session('admin')
        self.browser.get(self.live_server_url)
        wd_wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "New Location")))
        new_location_link = self.browser.find_element_by_partial_link_text("New Location")
        new_location_link.click()
        # elem = wd_wait.until(EC.element_to_be_clickable((By.ID, "id_clli_code")))
        # submit_element = self.browser.find_element_by_id("id_clli_code")
        # submit_element.click()
        # submit_element.send_keys(valid_clli)
        #location = Location.objects.get(clli_code=clli_code)
        # Keep CLLI Button
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_location_show")))
        keep_element = self.browser.find_element_by_id("id_location_show")
        keep_element.click()
        try:
            lambda: self.browser.find_element_by_xpath(
                "//*[@id='search_result_count']/td[1]").text
        except NoSuchElementException as nothing_here:
            self.fail(
                'There should be at least 3 search results, but found none. Error is {}'.format(nothing_here))