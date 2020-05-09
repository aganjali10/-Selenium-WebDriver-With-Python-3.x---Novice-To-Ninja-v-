import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//div[@id='navbar']//li[@class='dropdown']"


    def navigateToAllCourses(self):
        time.sleep(5)
        if not self.isElementPresent(locator=self._all_courses, locatorType="link"):
            self.goBack()
        self.elementClick(locator=self._all_courses, locatorType="link")

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType="link")

    def navigateToPractice(self):
        self.elementClick(locator=self._practice, locatorType="link")

    def navigateToUserSettings(self):
        userSettingsElement = self.waitForElement(locator=self._user_settings_icon,
                                      locatorType="xpath", pollFrequency=1)
        self.elementClick(element=userSettingsElement)