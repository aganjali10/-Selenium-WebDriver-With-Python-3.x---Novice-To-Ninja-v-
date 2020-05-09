import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"
    _enroll_button = "enroll-button-top"
    _cc_nu  = "//input[@name='cardnumber']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cv = "//input[@name='cvc']"
    _cc_pincode ="//input[@name='postal']"
    _submit_enroll = "//main[@id='sr-main-content']//div[@class='spc__primary-submit']"
    _enroll_error_message = "is-disabled"
    _agree = "agreed_to_terms_checkbox"

    def enterCourseName(self, name):
        self.sendKeys(name, self._search_box)

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(self._enroll_button)

    def enterCardNum(self, num):
        self.switchFrame("__privateStripeFrame8")
        self.sendKeys(num, self._cc_nu, locatorType="xpath")
        self.switchDefaultFrame()

    def enterCardExp(self, exp):
        self.switchFrame("__privateStripeFrame9")
        self.sendKeys(exp, self._cc_exp, locatorType="xpath")
        self.switchDefaultFrame()

    def enterCardCVV(self, cvv):
        self.switchFrame("__privateStripeFrame10")
        self.sendKeys(cvv, self._cc_cv, locatorType="xpath")
        self.switchDefaultFrame()

    def enterPinCode(self, pincode):
        self.switchFrame("__privateStripeFrame11")
        self.sendKeys(pincode, self._cc_pincode, locatorType="xpath")
        self.switchDefaultFrame()

    def agree(self):
        self.elementClick(self._agree)

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv, pin):
        #hint call all 3 methods to enter card details
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        self.enterPinCode(pin)
        self.agree()

    def enrollCourse(self, num="", exp="", cvv="", pin=""):
        """
        Hint:
        click on enroll button
        scroll down
        enter credit card info
        click enroll in course button
        """
        self.clickOnEnrollButton()
        self.webScroll("down")
        self.enterCreditCardInformation(num, exp, cvv, pin)
        # self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        """
        verify the element for error message is displayed, 
        not just present.
        you need to verify if it is displayed.
        hint: the element is not instantly displayed, it
        takes some time to display
        you need to wait for it to display
        """
        return self.isElementPresent(self._enroll_error_message, "class")