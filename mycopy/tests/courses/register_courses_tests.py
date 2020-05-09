from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        """
        call reqd methods from the page class to perform 
        the test
        enter course name
        select course
        enroll in course
        verify error message
        test status.markfinal()
        """
        self.lp.enterCourseName("JavaScript")
        self.lp.selectCourseToEnroll("javascript")
        self.lp.enrollCourse("10","10","10","10")
        result = self.lp.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")