from behave import *
from datetime import datetime


@then ('verify that the logo present on page')
def Logo_Verification(context):
    logo_text = context.driver.find_element_by_xpath("//img[@alt='company-branding']").is_displayed()
    print(logo_text)
    dt = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    context.driver.save_screenshot("C:\\Users\\shaik\\PycharmProjects\\HRM_Project_Behave_Framework\\Features_page\\Screenshots\\login_page_logo_{dt}.png")

    assert  logo_text is True


@then('close browser')
def Close_Browser(context):
    context.driver.close()