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
from selenium.common.exceptions import NoSuchElementException
class CustomerCreateTest(StaticLiveServerTestCase):
    '''
    This is the full test class that will check the customer create.
    '''

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
        super(CustomerCreateTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        '''
        breaks down the test browser session
        :return:
        '''
        cls.browser.quit()
        cls.display.stop()
        super(CustomerCreateTest, cls).tearDownClass()

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



    def test_existing_customer(self):
        '''
        This ensures the location link uses the  works correctly on the location page.
        :return:
        '''
        self.digits = string.digits
        self.letters = string.ascii_letters

        mommy.make(Customer,
                   name='Collin Cbadwick',
                   city=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address2=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   phone='7163977777',
                   state='SC',
                   zip_code=(
                       u''.join(random.choice(self.digits) for _ in range(5)))
                   ),

        mommy.make(Customer,
                   name=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   city='Washington',
                   street_address=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address2=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   state='SC',
                   zip_code=(
                       u''.join(random.choice(self.digits) for _ in range(5)))
                   )

        wd_wait = WebDriverWait(self.browser, 10)
        # This will create an actual test customer
        self.create_pre_authenticated_session('admin')
        self.browser.get(self.live_server_url)
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_name")))
        name_add = self.browser.find_element_by_id("id_name")
        name_add.send_keys("Collin")

        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_phone")))
        name_add = self.browser.find_element_by_id("id_phone")
        name_add.send_keys("7163977777")

        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_street_address")))
        name_add = self.browser.find_element_by_id("id_street_address")
        name_add.send_keys("123 main st")

        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_street_address2")))
        name_add = self.browser.find_element_by_id("id_street_address2")
        name_add.send_keys("apt 108")

        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_city")))
        name_add = self.browser.find_element_by_id("id_city")
        name_add.send_keys("Fort Mill")

        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_zip")))
        name_add = self.browser.find_element_by_id("id_zip")
        name_add.send_keys("12345")

        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_customer_create")))
        keep_element = self.browser.find_element_by_id("id_customer_create")
        keep_element.click()

        try:
            wd_wait.until(EC.visibility_of_element_located((By.ID, "id_error")))
            customer_add = self.browser.find_element_by_id("id_error")
            self.assertTrue(customer_add.text == 'Not Added Check Your Data!')
            f"expected: More than 3 characters needed', actual : {name_add.text}"
        except NoSuchElementException as element_doesnt_exist:
            self.fail(f'Name Errors Not Displaying at all : Response - {element_doesnt_exist}')


