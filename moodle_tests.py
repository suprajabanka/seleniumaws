import unittest
import moodle_locators as locators
import moodle_methods as methods


class MoodleAppPositiveTestCases (unittest.TestCase):  # create class

    @staticmethod  # signal to Unittest that this is a static method
    def test_create_new_user():
        methods.setup()
        methods.log_in(locators.admin_username, locators.admin_password)
        methods.create_new_user()
        methods.search_user()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.check_new_user_can_login()
        methods.logger('created')
        methods.log_out()
        methods.log_in(locators.admin_username, locators.admin_password)
        methods.search_user()
        methods.delete_user()
        methods.logger('deleted')
        methods.log_out()
        methods.teardown()


