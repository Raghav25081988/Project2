from selenium.webdriver import Chrome
from time import sleep
import pytest
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

'''
@pytest.fixture(scope="module") --- scope = module, in this case browser open and close will happen once for all the test case
'''

@pytest.fixture(scope="module")
def starter():
    global driver
    driver = Chrome(executable_path="D:/PythonProjects/DISCOM/Drivers/chromedriver.exe")
    driver.get("https://www.google.com")
    driver.implicitly_wait(30)
    '''driver.implicitly_wait(30) --- waits for 30 secs untill page loads specific element'''
    yield
    driver.close()

def test_validation(starter):
    driver.maximize_window()
    wait = WebDriverWait(driver,30)
    wait.until(ec.visibility_of)
    driver.find_element_by_xpath("//input[@name='q']").send_keys("good morning messages")

def test_validation2(starter):
    assert driver.title == "Googley"
    driver.maximize_window()

def test_validation3(starter):
    assert driver.current_url == "https://gooogle.com"
    driver.maximize_window()

