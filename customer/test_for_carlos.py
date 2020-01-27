'''
test_location_create.py - this will run different testing scenarios to test
the new location creation page.
By - Collin Chadwick
'''
# pylint: disable=e1101, W0703, C0103, R0915
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
from ics.models import Location, Region, LocationType, ServiceType
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
        self.browser.get(self.live_server_url + "/404_no_such_url/")
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            secure=False,
            path='/',
        ))
        self.browser.refresh()

    def populate_form_valid(self):
        '''
        This fills the form with valid successful data entry,
        this is used multiple times in the test
        :return:
        '''
        time.sleep(3)
        wd_wait = WebDriverWait(self.browser, 10)
        valid_name = "Tasta Pizza"
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_name")))
        name_element = self.browser.find_element_by_id("id_name")
        name_element.click()
        name_element.send_keys(valid_name)

        # making sure no errors pop up
        name_error = self.browser.find_element_by_id("id_name_error")



        # No Errors on Name - Fill Street
        if not name_error.is_displayed():
            wd_wait.until(EC.element_to_be_clickable((By.ID, "id_street_address")))
            valid_street = "E State St"
            street_element = self.browser.find_element_by_id("id_street_address")
            street_element.click()
            street_element.send_keys(valid_street)

            # making sure no errors pop up
            id_street_address_error = self.browser.find_element_by_id("id_street_address_error")
        else:
            self.fail('Name Error On valid post info : Response - {}'.format(name_error.text))

        #No Errors on Street - Fill city
        if not id_street_address_error.is_displayed():
            wd_wait.until(EC.element_to_be_clickable((By.ID, "id_city")))
            city_element = self.browser.find_element_by_id("id_city")
            valid_city = "Olean"
            city_element.click()
            city_element.send_keys(valid_city)

            # making sure no errors pop up
            id_city_error = self.browser.find_element_by_id("id_city_error")
        else:
            self.fail('Street Error On valid post info : Response - {}'.format(id_street_address_error.text))
            # No Errors on City - Fill State

        if not id_city_error.is_displayed():

            wd_wait.until(EC.visibility_of_element_located((By.ID, "id_state")))
            state = Select(self.browser.find_element_by_id("id_state"))
            state.select_by_visible_text("Connecticut")

            # making sure no errors pop up
            id_state_error = self.browser.find_element_by_id("id_state_error")
        else:
            self.fail('City Error On valid post info : Response - {}'.format(id_city_error.text))

        if not id_state_error.is_displayed():
            wd_wait.until(EC.element_to_be_clickable((By.ID, "id_zip_code")))
            # street_address_element = self.browser.find_element_by_id("id_zip_code")
            valid_zip = "14760"
            zip_element = self.browser.find_element_by_id("id_zip_code")
            zip_element.click()
            zip_element.send_keys(valid_zip)

            # making sure no errors pop up
            id_zip_error = self.browser.find_element_by_id("id_zip_code_error")
        else:
            self.fail('State Error On valid post info : Response - {}'.format(id_state_error.text))

        if not id_zip_error.is_displayed():
            wd_wait.until(EC.element_to_be_clickable((By.ID, "id_location_type")))
            valid_loc = "3"
            loc_type = Select(self.browser.find_element_by_id("id_location_type"))
            loc_type.select_by_value(valid_loc)

            # making sure no errors pop up
            id_location_type_error = self.browser.find_element_by_id("id_location_type_error")
        else:
            self.fail('Location Type Error On valid post info : Response - {}'.format(id_zip_error.text))

        if not id_location_type_error.is_displayed():
            wd_wait.until(EC.element_to_be_clickable((By.ID, "id_region")))
            valid_region = "6"
            name = Select(self.browser.find_element_by_id("id_region"))
            name.select_by_value(valid_region)

            # making sure no errors pop up
            id_region_error = self.browser.find_element_by_id("id_region_error")
        else:
            self.fail('Region Error On valid post info : Response - {}'.format(id_location_type_error.text))

        if not id_region_error.is_displayed():
            wd_wait.until(EC.element_to_be_clickable((By.ID, "id_master_billing_account")))
            billing_element = self.browser.find_element_by_id("id_master_billing_account")
            valid_mba = "90999900090"
            billing_element.click()
            billing_element.send_keys(valid_mba)

            # making sure no errors pop up
            id_mba_error = self.browser.find_element_by_id("id_master_billing_account_error")
        else:
            self.fail('Region Error On valid post info : Response - {}'.format(id_region_error.text))

        if not id_mba_error.is_displayed():
            try:

                submit_element = self.browser.find_element_by_id("id_location_create")
                submit_element.click()
            except Exception as timed_out:
                self.fail('Button Timed Out there are errors to correct in test.  Results ; {}'.format(timed_out))
        else:
            self.fail('Master Billing Error On valid post info : Response - {}'.format(id_mba_error.text))

    def test_invalid_entries(self):
        '''
        Tests invalid entries into the form, and makes sure the correct errors are showing.
        :return:
        '''
        wd_wait = WebDriverWait(self.browser, 10)
        # The SEER admin wants to verify that the we can drill down through a location
        # So he navigates to the SEER website
        self.create_pre_authenticated_session('admin')
        self.browser.get(self.live_server_url)
        wd_wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "New Location")))
        new_location_link = self.browser.find_element_by_partial_link_text("New Location")
        new_location_link.click()

        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_clli_code")))
        clli_code_exists = self.browser.find_element_by_id("id_clli_code")
        invalid_state_clli = "MTTDFSAT"
        clli_code_exists.send_keys(invalid_state_clli)
        try:
            (EC.visibility_of_element_located((By.ID, "id_clli_error")))
        except NoSuchElementException as element_doesnt_exist:
            self.fail('Name Errors Not Displaying For < 3 Characters:')

        # Look for errors in name############
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_name")))
        name_add = self.browser.find_element_by_id("id_name")
        name_add.send_keys("ha")
        try:
            wd_wait.until(EC.visibility_of_element_located((By.ID, "id_name_error")))
            name_add = self.browser.find_element_by_id("id_name_error")
            self.assertTrue(name_add.text == 'More than 3 characters needed!')
            "Name Error is Incorrect, expected: {}, actual : {}".format(
                'More than 3 characters needed', name_add.text)
        except NoSuchElementException as element_doesnt_exist:
            self.fail('Name Errors Not Displaying at all : Response - {}'.format(element_doesnt_exist))

        # Look for errors in street address###########
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_street_address")))
        street_add = self.browser.find_element_by_id("id_street_address")
        street_add.send_keys("sA")
        try:
            wd_wait.until(EC.visibility_of_element_located((By.ID, "id_street_address_error")))
            street_add = self.browser.find_element_by_id("id_street_address_error")
            self.assertTrue(street_add.text == 'More than 3 characters needed!')
            "Street Error is Incorrect, expected: {}, actual : {}".format(
                'More than 3 characters needed', street_add.text)
        except NoSuchElementException as element_doesnt_exist:
            self.fail('Name Errors Not Displaying at all : Response - {}'.format(element_doesnt_exist))

        # Look for errors in city#############
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_city")))
        city_add = self.browser.find_element_by_id("id_city")
        city_add.send_keys("VA")
        try:
            wd_wait.until(EC.visibility_of_element_located((By.ID, "id_city_error")))
            city_add = self.browser.find_element_by_id("id_city_error")
            self.assertTrue(street_add.text == 'More than 3 characters needed!')
            "City Error is Incorrect, expected: {}, actual : {}".format(
                'More than 3 characters needed', city_add.text)
        except NoSuchElementException as element_doesnt_exist:
            self.fail('City Errors Not Displaying at all : Response - {}'.format(element_doesnt_exist))

    # Look for Characters in zip code#############
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_zip_code")))
        city_add = self.browser.find_element_by_id("id_zip_code")
        city_add.send_keys("VA")
        try:
            wd_wait.until(EC.visibility_of_element_located((By.ID, "id_city_error")))
            city_add = self.browser.find_element_by_id("id_city_error")
            self.assertTrue(street_add.text == 'More than 3 characters needed!')
            "City Error is Incorrect, expected: {}, actual : {}".format(
                'More than 3 characters needed', city_add.text)
        except NoSuchElementException as element_doesnt_exist:
            self.fail('City Errors Not Displaying at all : Response - {}'.format(element_doesnt_exist))

    def test_success_with_modal(self):
        '''
        This ensures modal works correctly on the location page.
        :return:
        '''
        wd_wait = WebDriverWait(self.browser, 10)
        # This will create an actual location for testing purposes and also the location management button
        # when a location exists.
        self.create_pre_authenticated_session('admin')
        self.browser.get(self.live_server_url)
        wd_wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "New Location")))
        new_location_link = self.browser.find_element_by_partial_link_text("New Location")
        new_location_link.click()
        valid_clli = "MNOPTXBK"
        elem = wd_wait.until(EC.element_to_be_clickable((By.ID, "id_clli_code")))
        submit_element = self.browser.find_element_by_id("id_clli_code")
        submit_element.click()
        submit_element.send_keys(valid_clli)

        # Keep CLLI Button
        wd_wait.until(EC.element_to_be_clickable((By.ID, "keep_button")))
        keep_element = self.browser.find_element_by_id("keep_button")
        keep_element.click()
        if submit_element.get_attribute('value') != valid_clli:
            self.fail('CLLI shouldnt change on keep button : Correct Value is - {}, Current value - {}'.format
                      (valid_clli, elem.getAttribute('value')))


        # Enters Customer Information
        self.populate_form_valid()


        # Edit CLLI Button
        self.browser.get(self.live_server_url)
        wd_wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "New Location")))
        new_location_link = self.browser.find_element_by_partial_link_text("New Location")
        new_location_link.click()
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_clli_code")))
        edit_clli = 'HRHTTXXX'
        submit_element = self.browser.find_element_by_id("id_clli_code")
        submit_element.click()
        submit_element.send_keys(edit_clli)
        form_value = 'HRHTTXSX'
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_clli_modal")))
        edit_element = self.browser.find_element_by_id("id_clli_modal")
        edit_element.send_keys(form_value)
        self.browser.find_element_by_id("edit_button").click()
        time.sleep(5)

        elem = wd_wait.until(EC.element_to_be_clickable((By.ID, "id_clli_code")))
        submit_element = self.browser.find_element_by_id("id_clli_code")
        submit_element.click()
        # if submit_element.get_attribute('value') != form_value:
        #     self.fail(
        #         'CLLI should match form on edit button : Correct Value is - {}, Current value - {}'.format
        #         (valid_clli, submit_element.get_attribute('value')))
        # Enters Customer Information
        self.populate_form_valid()


    def test_granite_population_success(self):
        '''
        This ensures successful entries on the location page.
        :return:
        '''
        wd_wait = WebDriverWait(self.browser, 10)
        # This will create an actual location for testing purposes and also the location management button
        # when a location exists.
        self.create_pre_authenticated_session('admin')
        self.browser.get(self.live_server_url)
        wd_wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "New Location")))
        new_location_link = self.browser.find_element_by_partial_link_text("New Location")
        new_location_link.click()
        valid_clli = "HRHTTXBK"
        wd_wait.until(EC.element_to_be_clickable((By.ID, "id_clli_code")))
        submit_element = self.browser.find_element_by_id("id_clli_code")
        submit_element.click()
        submit_element.send_keys(valid_clli)
        time.sleep(3)
        # check for drop down
        try:
            wd_wait.until(EC.visibility_of_element_located((By.ID, "id_name")))
            name = Select(self.browser.find_element_by_id("id_name"))
            name.select_by_visible_text("AT&T WIRELINE")
        except (NoSuchElementException, UnexpectedTagNameException) as no_element:
            self.fail("This selection doesnt exist : {}".format(no_element))

        try:
            street_address = self.browser.find_element_by_id("id_street_address")
            street_address.get_attribute("value")
            if street_address.get_attribute('value') == '':
                self.fail(
                    'street address should contain granite data :  Current value - {}'.format
                    (street_address.get_attribute('value')))
        except (NoSuchElementException, UnexpectedTagNameException) as no_element:
            self.fail("This street address element doesnt exist : {}".format(no_element))

        try:
            city = self.browser.find_element_by_id("id_city")
            city.get_attribute("value")
            if city.get_attribute('value') == '':
                self.fail(
                    'city should contain granite data :  Current value - {}'.format
                    (city.get_attribute('value')))
        except (NoSuchElementException, UnexpectedTagNameException) as no_element:
            self.fail("This city element doesnt exist : {}".format(no_element))

        try:
            wd_wait.until(EC.visibility_of_element_located((By.ID, "id_region")))
            region = Select(self.browser.find_element_by_id("id_region"))
            region.select_by_value("6")

        except (NoSuchElementException, UnexpectedTagNameException) as no_element:
            self.fail("This region element doesnt exist : {}".format(no_element))


        try:
            master_billing = self.browser.find_element_by_id("id_master_billing_account")
            master_billing.click()
            valid_billing = "9999"
            master_billing.send_keys(valid_billing)

        except (NoSuchElementException, UnexpectedTagNameException) as no_element:
            self.fail("This street address element doesnt exist : {}".format(no_element))

        # the use of jquery in validation of the field makes send keys not work
        # so I am executing javascript to pudate the fields.  You will see this throughout
        try:
            # wd_wait.until(EC.element_to_be_clickable((By.ID, "id_location_create")))
            submit_element = self.browser.find_element_by_id("id_location_create")
            submit_element.click()
        except Exception as timed_out:
            self.fail('Button Timed Out there are errors to correct in test.  Results ; {}'.format(timed_out))


    def test_existing_location_button(self):
        '''
        This ensures the location link uses the  works correctly on the location page.
        :return:
        '''
        self.digits = string.digits
        self.letters = string.letters
        mommy.make(
            LocationType,
            id=2,
            name="Business"
        )
        mommy.make(
            Region,
            id=2,
            name="HI",
            support_number="000-000-0000",
            parent_id=None
        )
        mommy.make(ServiceType, id=1, name=u'WIFI (Legacy)')
        mommy.make(ServiceType, id=2, name=u'Video Transport')
        mommy.make(ServiceType, id=3, name=u'Video Backhaul')
        mommy.make(ServiceType, id=4, name=u'VDSL')
        mommy.make(ServiceType, id=5, name=u'SIP')
        mommy.make(ServiceType, id=6, name=u'Set Back Box')
        mommy.make(ServiceType, id=7, name=u'Pro:Idiom')
        mommy.make(ServiceType, id=8, name=u'Managed Security')
        mommy.make(ServiceType, id=9, name=u'Managed Router')
        mommy.make(ServiceType, id=10, name=u'EE/CE')

        clli_code = 'HFDSSCTD'
        testing_location = mommy.make(Location,
                   name='Washington High',
                   clli_code= clli_code,
                   master_billing_account=(u''.join(
                       random.choice(self.digits) for _ in range(10))),
                   city=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address2=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   region=Region.objects.get(name='HI'),
                   location_type=LocationType.objects.get(id=2),
                   zip_code=(
                       u''.join(random.choice(self.digits) for _ in range(5)))
                   )
        mommy.make(Location,
                   name=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   clli_code=clli_code,
                   master_billing_account=(u''.join(
                       random.choice(self.digits) for _ in range(10))),
                   city='Washington',
                   street_address=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address2=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   region=Region.objects.get(name='HI'),
                   location_type=LocationType.objects.get(id=2),
                   zip_code=(
                       u''.join(random.choice(self.digits) for _ in range(5)))
                   )
        mommy.make(Location,
                   name=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   clli_code=clli_code,
                   master_billing_account=(u''.join(
                       random.choice(self.digits) for _ in range(10))),
                   city=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   street_address='123 Washington Street',
                   street_address2=(u''.join(
                       random.choice(self.letters) for _ in range(10))),
                   region=Region.objects.get(name='HI'),
                   location_type=LocationType.objects.get(id=2),
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
        valid_clli = clli_code
        elem = wd_wait.until(EC.element_to_be_clickable((By.ID, "id_clli_code")))
        submit_element = self.browser.find_element_by_id("id_clli_code")
        submit_element.click()
        submit_element.send_keys(valid_clli)
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



