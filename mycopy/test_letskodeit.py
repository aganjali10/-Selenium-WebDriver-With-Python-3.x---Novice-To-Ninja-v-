"""
https://groups.google.com/forum/#!forum/seleniumpython
nodes are of class: selenium.webdriver.remote.webelement.WebElement

in python2, for scripts to be used as modules, they should have a main funtion

find_element_by_...() OR find_element(By.ID, "..") (both are completely same imo)
find_elements_by_...() OR find_elements(By.XPATH, "..")

id
name
xpath
link_text (a link is <a></a>)
partial_link_text
tag_name
class_name (dont put more than 1 class names)
css_selector 

CSS_SELECTOR (ID-> #id, class-> .class, tag_name-> tag_name)
method 1. (tagname[attribute<special character>='value'], eg: input[id='displayed-text'], input[class='displayed-class']) (NOTE: while using input#[class='displayed-class'], use all the classes used in that element, same for xpath, //tagname[@class='value'])
method 2. (eg: #displayed-text, .displayed-class)(NOTE: can use any number of classes; order doesnt matter)
method 3. (eg: input#displayed-text, input.displayed-class)(NOTE: can use any number of classes; order doesnt matter)
special character: 1.^ starts with 2.$ ends with 3.* contains
to go down to childnode use > (eg: tag1>tag2>tag3#id)

XPATH (//tagname[@attribute='value'] or //tagname[contains(@attribute,'value')] or tagname[starts-with(@attribute,'value')])
absolute: html/body/header/div/...
relative: //*[id='displayed-text']/div/div/div/a..
single slash: look for an element immediately inside the parent element
double slash: look for any child or nested child element inside the parent element
//a[text()='Enroll now'] 
//div[@id='navbar']//a[contains(@class,'navbar-link') and contains(@href,'sign_in')]
parent: xpath_to_some_element//parent::<tag>
preceding sibling: xpath_to_some_element//preceding_sibling::<tag> (not immediate; but all)
following sibling: xpath_to_some_element//following_sibling::<tag> (not immediate; but all)

static IDs (but how to 1.check if static or dynamic? 2.how to work with dynamic IDs)
unique elements/nodes
preference: id>css>xpath>link_text>classname
classname, tagname, linktext not preferred due to un-uniqueness
node.text (gives text) OR node.get_attribute("innerText")
node.get_attribute(attributename), eg: node.get_attribute("class")
time.sleep() vv imp in many cases
find_elements never raises an exception. If the element isnt found, it returns an empty list.

METHODS AND ATTRIBUTES OF DRIVER
maximize_window()
get()
title
current_url
refresh()
back()
forward()
page_source
close()
quit()
implicitly_wait(argument in secs): 
current_window_handle (returns the handle to the focussed  window)
window_handles (returns a list to handles of all opened windows)
switch_to.window(handle)
switch_to.frame(id)
switch_to.frame(name)
switch_to.frame(index) 0-based
switch_to.default_content()
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

METHODS OF DIFFERENT WEBELEMENTS
<a></a>: click
<input>: send_keys, clear
<select>: (dropdown menus)

if the html of an element contains the disabled attribute, then we cant interact with it. 
element.is_enabled() //is true if enabled else false
real life scenario: if check box is ticked, then the following fields are enabled else disabled.

radiobuttons and checkboxes are <input> only and have a property is_selected() which is true if selected else false

working with hidden elements: ele.is_displayed()

waits
explicit wait: An explicit wait is a code you define to wait for a certain condition to occur before proceeding further in the code.
implicit wait: An implicit wait tells WebDriver to poll the DOM for a certain amount of time when trying to find any element (or elements) not immediately available. 

position(): The position function returns a number equal to the context position from the expression evaluation context. 
a node's position in a context is not zero-based. The first node has a position of 1.
<xsl:template match="//div[@class='foo']/bar[position() = 1]">
<!-- this template matches the first bar element that is a child of a div element with a class attribute equal to "foo" -->
</xsl:template>

we can also find_element on a WebElement.

to execute javascript commands: driver.execute_script(javascript_command)

when we open another window, focus stays on the previous window only.

three types of popups: html/css, javascript, windows
javascript popups are of two types: alert and confirm.
they cant be inspected.
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

Actions Class
actions = ActionChains(driver)
eg: actions.move_to_element(element).perform()
other egs: drag_and_drop, click_and_hold, release etc.

Logging
Levels
1. Debug
2. Info
3. Warning
4. Error
5. Critical
https://docs.python.org/3/library/logging.html#logrecord-attributes
https://docs.python.org/3/library/time.html#time.strftime
logging level of handler and not that of the logger decides which logs will be printed (?doubt)
default logging level is warning.

writng tests
flow: test fixture->test case->test suite->test runner->test report
test method names should start with 'test'
if a test fails at a certain statement, then that particular test doesnt continue and terminates
https://docs.python.org/3/library/unittest.html#unittest.TestCase
for pytest, file name should start with test_
py.test [-v] [-s] [file_name]
-s to print statements
-v verbose
1. py.test test_mod.py               #run tests in module
2. py.test somepath                  #run all tests below somepath
3. py.test test_mod.py::test_method  #only run test_method in test_mod
To control the order in which tests run, pip install pytest-ordering. Then @pytest.mark.run(order=2) is added as a decorator.
https://pytest-ordering.readthedocs.io/en/develop/S

Page Testing Model
base(base classes)
    |
    |
    |
pages(page classes)
    |
    |
    |
tests(test classes)
    |
    |
    |
utilities
	Utility Classes
    |
    |
configuration Files
    |
    |
    |
screenshots
"""

# CODE

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging
import logging.config
import inspect
import unittest
import pytest
# import sys
# sys.path.append('C:\\Users\\Anjali\\Desktop\\')
# from folder_name.folder1 import file_name
# # import folder_name.folder1.file_name
# print(file_name.pss)

# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://letskodeit.teachable.com/pages/practice')
# driver.implicitly_wait(10)

#driver.find_element_by_id("name")
# if not found, then raises an exception, NoSuchElementException.
#driver.find_element_by_name("show-hide")
#* is wildcard
#driver.find_element_by_xpath("//*[@id='name']")
#driver.find_element_by_css_selector('#displayed_text')
#driver.find_element_by_link_text("Login")
#driver.find_element_by_partial_link_text("Pra")
#driver.find_element_by_class_name("displayed-class")
#driver.find_element_by_tag_name("a")

#driver.find_element(By.ID, "name")
#driver.find_element(By.XPATH, "//*[@id='displayed_text']")
#driver.find_element(By.LINK_TEXT, "Login")

# returns list
#driver.find_elements_by_class_name("inputs")
#driver.find_elements(By.TAG_NAME, "h1")
#driver.find_elements(By.TAG_NAME, "td")

#dropdown menus
# element=driver.find_element_by_id('carselect')
# sel=Select(element)
# sel.select_by_value("benz")
# sel.select_by_index("2")
# sel.select_by_visible_text("BMW")
# sel.select_by_index(2)

#working with hidden elements
# textboxele=driver.find_element_by_id('displayed-text')
# textboxstate=textboxele.is_displayed()
# print(textboxstate)
# time.sleep(2)
# driver.find_element_by_id('hide-textbox').click()
# textboxstate=textboxele.is_displayed()
# print(textboxstate)
# time.sleep(2)
# driver.find_element_by_id('show-textbox').click()
# textboxstate=textboxele.is_displayed()
# print(textboxstate)

#logging in and dynamic xpath
# driver.find_element_by_xpath("//a[@href='/sign_in']").click()
# driver.find_element_by_id('user_email').send_keys('aganjali10@gmail.com')
# driver.find_element_by_id('user_password').send_keys(correct_password)
# driver.find_element_by_xpath("//input[@name='commit']").click()
# course_name="JavaScript for beginners"
# driver.find_element_by_xpath("//div[@title='{}']".format(course_name)).click()

#explicit wait
# driver.get('https://www.expedia.com/')
# driver.find_element_by_class_name('uitk-icon-flights').click()
# driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']").send_keys("del")
# driver.find_element_by_xpath("//input[@id='flight-destination-hp-flight']").send_keys("hyd")
# driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']").send_keys("05/05/2020")
# x=driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")
# x.clear()
# x.send_keys("05/07/2020")
# driver.find_element_by_xpath("//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']").click()
# wait=WebDriverWait(driver, 10, poll_frequency=1,ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
# ele=wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
# ele.click()

#choose date from calender
# driver.get('https://www.expedia.com/')
# driver.find_element_by_class_name('uitk-icon-flights').click()
# driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']").click()
# driver.find_element_by_xpath("//button[@data-day='31']").click()

#using autocomplete
# driver.get('https://www.southwest.com')
# driver.find_element_by_id("LandingAirBookingSearchForm_originationAirportCode").send_keys("New York")
# time.sleep(3)
# driver.find_element_by_xpath("//ul[@id='LandingAirBookingSearchForm_originationAirportCode--menu']/li[2]/button[@type='button']").click()

#screenshot
# driver.find_element_by_xpath("//a[@href='/sign_in']").click()
# driver.find_element_by_id('user_email').send_keys('aganjali10@gmail.com')
# driver.find_element_by_id('user_password').send_keys('abc') #incorrect password
# driver.find_element_by_xpath("//input[@name='commit']").click()
# driver.save_screenshot("C:\\Users\\Anjali\\Desktop\\python scripts\\ss.png")

#javascript commands
# print(driver.execute_script("return window.innerHeight;")) #get height
# print(driver.execute_script("return window.innerWidth;")) #get width
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,3000);") #scroll down
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,-3000);") #scroll up
# ele=driver.find_element_by_id("mousehover")
# driver.execute_script("arguments[0].scrollIntoView(true)",ele) #scroll element into view
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,-150);")
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,-3000);")
# time.sleep(3)
# location=ele.location_once_scrolled_into_view #native way to scroll element into view
# print(str(location))
# time.sleep(3)
# driver.execute_script("window.scrollBy(0,-150);")

#working with iframes
# driver.switch_to.frame('courses-iframe')
# time.sleep(2)
# driver.find_element_by_id('search-courses').send_keys('python')
# time.sleep(2)
# driver.switch_to.default_content()
# time.sleep(2)
# driver.find_element_by_id('name').send_keys('test successful')

#handling mousehovers
# ele=driver.find_element_by_id("mousehover")
# itemToClickLocator="//a[@href='#top']"
# actions=ActionChains(driver)
# actions.move_to_element(ele).perform()
# time.sleep(2)
# topLink=driver.find_element_by_xpath(itemToClickLocator)
# actions.move_to_element(topLink).click().perform()

#drag and drop
# driver.get('https://jqueryui.com/droppable/')
# driver.switch_to.frame(0)
# fromele=driver.find_element_by_id("draggable")
# toele=driver.find_element_by_id("droppable")
# actions=ActionChains(driver)
# time.sleep(2)
# # actions.drag_and_drop(fromele,toele).perform() #method1
# actions.click_and_hold(fromele).move_to_element(toele).release().perform() #method2

#slider
# driver.get('https://jqueryui.com/slider/')
# driver.switch_to.frame(0)
# ele=driver.find_element_by_xpath("//div[@id='slider']//span")
# time.sleep(2)
# actions=ActionChains(driver)
# actions.drag_and_drop_by_offset(ele,100,0).perform()

# basic logging
# #will print warning and error because info<warning
# logging.warning("warning")
# logging.info("info")
# logging.error("error")
# #will print all three because all three>debug
# logging.basicConfig(filename="test.log", level=logging.DEBUG)
# logging.warning("warning")
# logging.info("info")
# logging.error("error")
# #if filename isnt mentioned, then logs are printed on the console
# #formatting of log
# logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
# logging.warning("warning")
# logging.info("info")
# logging.error("error")

# advanced logging: Logger part 1
# def customLogger(logLevel):
# 	# Gets the name of the class/method from where it is called
# 	loggerName = inspect.stack()[1][3]
# 	logger = logging.getLogger(loggerName) #logger = logging.getLogger('sample-log') OR logger = logging.getLogger(LoggerDemoConsole.__name__)
# 	#By default, log all messages
# 	logger.setLevel(logging.DEBUG)
# 	#consoleHandler
# 	# consoleHandler = logging.StreamHandler()
# 	# consoleHandler.setLevel(logLevel)
# 	#fileHandler
# 	fileHandler = logging.FileHandler("{0}.log".format(loggerName), mode='w')
# 	fileHandler.setLevel(logLevel)
# 	formatter = logging.Formatter('%(asctime)s: -%(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# 	# consoleHandler.setFormatter(formatter)
# 	fileHandler.setFormatter(formatter)
# 	# logger.addHandler(consoleHandler)
# 	logger.addHandler(fileHandler)
# 	return logger
# class LoggingDemo():
# 	log = customLogger(logging.DEBUG)
# 	def method1(self):
# 		self.log.debug("debug")
# 		self.log.info("info")
# 		self.log.warning("warning")
# 		self.log.error("error")
# 		self.log.critical("critical")
# 	def method2(self):
# 		log1 = customLogger(logging.INFO)
# 		log1.debug("debug")
# 		log1.info("info")
# 		log1.warning("warning")
# 		log1.error("error")
# 		log1.critical("critical")
# 	def method3(self):
# 		log2 = customLogger(logging.INFO)
# 		log2 .debug("debug")
# 		log2 .info("info")
# 		log2 .warning("warning")
# 		log2 .error("error")
# 		log2 .critical("critical")
# lg=LoggingDemo()
# lg.method1()
# lg.method2()
# lg.method3()

# advanced logging: Logger part 2 #not working
# logging.config.fileConfig('C:\\Users\\Anjali\\Desktop\\python scripts\\logging')
# logger = logging.getLogger(LoggerDemoConf.__name__)

# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")
# logger.critical("critical")

#testing
# class TestCaseDemo1(unittest.TestCase):
# 	#runs only once
# 	@classmethod
# 	def setUpClass(self):
# 		print("SetupClass")
# 	#runs before every method
# 	def setUp(self):
# 		print("Setup")
# 	def testmethod1(self):
# 		print("method1")
# 	def testmethod2(self):
# 		print("method2")
# 	def testasserttruefalse(self):
# 		a, b=True, True
# 		self.assertTrue(a, "a is not true")
# 		self.assertFalse(b, "b is not false") #will fail
# 	def testassertequals(self):
# 		a = b = "Test"
# 		self.assertEqual(a,b, "a isnt equal to b")
# 	def tearDown(self):
# 		print("Teardown")
# 	@classmethod
# 	def tearDownClass(self):
# 		print("TeardownClass")
# class TestCaseDemo2(unittest.TestCase):
# 	#runs only once
# 	@classmethod
# 	def setUpClass(self):
# 		print("SetupClass")
# 	#runs before every method
# 	def setUp(self):
# 		print("Setup")
# 	def testmethod1(self):
# 		print("method1")
# 	def testmethod2(self):
# 		print("method2")
# 	def testasserttruefalse(self):
# 		a, b=True, True
# 		self.assertTrue(a, "a is not true")
# 		self.assertFalse(b, "b is not false") #will fail
# 	def testassertequals(self):
# 		a = b = "Test"
# 		self.assertEqual(a,b, "a isnt equal to b")
# 	def tearDown(self):
# 		print("Teardown")
# 	@classmethod
# 	def tearDownClass(self):
# 		print("TeardownClass")
# # unittest.main()
# tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo2)
# smoke_test = unittest.TestSuite([tc1, tc2])
# unittest.TextTestRunner().run(smoke_test)

#pytest
# method1
# @pytest.fixture()
# def setUp():
# 	print("Setup")
# method2
# @pytest.yield_fixture()
# def setUp():
# 	print("Setup")
# 	yield
# 	print("Teardown")
# method3: fixtures in conftest.py
# @pytest.mark.run(order=2)
# def testmethod1(setUp, oneTimeSetUp):
# 	print("method1")
# @pytest.mark.run(order=3)
# def testmethod2(setUp, oneTimeSetUp):
# 	print("method2")
# @pytest.mark.run(order=1)
# def testmethod3(setUp, oneTimeSetUp):
# 	print("method3")
# method 4
class SomeClassToTest():
	def __init__(self,value):
		self.value=value
	def sumNumbers(self,a,b):
		return a+b+self.value
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():
	@pytest.fixture(autouse=True)
	def classSetup(self, oneTimeSetUp):
		# self.abc=SomeClassToTest(10)
		self.abc=SomeClassToTest(self.value)
	def testmethod1(self):
		result=self.abc.sumNumbers(2,8)
		assert result==20
		print("method1")
	def testmethod2(self):
		result=self.abc.sumNumbers(2,8)
		assert result>20
		print("method2")
