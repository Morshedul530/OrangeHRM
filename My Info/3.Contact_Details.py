from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Contact():
    def test_contact_details(self):
        base_url = 'https://opensource-demo.orangehrmlive.com/'
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(base_url)

        # Find Elements
        username = driver.find_element(By.XPATH, '//*[@id="txtUsername"]')
        password = driver.find_element(By.CSS_SELECTOR, '#txtPassword')
        login_btn = driver.find_element(By.ID, 'btnLogin')

        # Login Action
        username.clear()
        username.send_keys('Admin')

        password.clear()
        password.send_keys('admin123')

        login_btn.click()

        # My Info Link Click
        driver.find_element(By.LINK_TEXT, 'My Info').click()

        # Click Contact Details
        driver.find_element(By.LINK_TEXT, 'Contact Details').click()

        # Click Edit
        edit = driver.find_element(By.ID, 'btnSave')
        edit.click()
        time.sleep(3)

        address_street1 = driver.find_element(By.ID, 'contact_street1')
        address_street1.clear()
        address_street1.send_keys('Road 05, Block A, Shagufta Housing')

        address_street2 = driver.find_element(By.ID, 'contact_street2')
        address_street2.clear()
        address_street2.send_keys('Road 05, Block A, Mipur 12')

        city = driver.find_element(By.ID, 'contact_city')
        city.clear()
        city.send_keys('Dhaka')

        state_province = driver.find_element(By.ID, 'contact_province')
        state_province.clear()
        state_province.send_keys('Dhaka')

        zip_postal_code = driver.find_element(By.ID, 'contact_emp_zipcode')
        zip_postal_code.clear()
        zip_postal_code.send_keys('1216')

        country = driver.find_element(By.ID, 'contact_country')
        sel = Select(country)
        sel.select_by_value('BD')

        home_telephone = driver.find_element(By.ID, 'contact_emp_hm_telephone')
        home_telephone.clear()
        home_telephone.send_keys('+8809678910')

        mobile = driver.find_element(By.ID, 'contact_emp_mobile')
        mobile.clear()
        mobile.send_keys('01746604763')

        work_telephone = driver.find_element(By.ID, 'contact_emp_work_telephone')
        work_telephone.clear()
        work_telephone.send_keys('+8809645678')

        work_email = driver.find_element(By.ID, 'contact_emp_work_email')
        work_email.clear()
        work_email.send_keys('shuvo@gmail.com')

        other_email = driver.find_element(By.ID, 'contact_emp_oth_email')
        other_email.clear()
        other_email.send_keys('morshedul@gmail.com')

        # Click Save
        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        # Add Attachment
        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()
        time.sleep(3)

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        select_file = driver.find_element(By.ID, 'ufile')
        select_file.send_keys('C:\\Users\\morsh\\Desktop\\selenium_logo.png')

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('The image uploaded successfully')

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()

        if not status:
            checkbox.click()
            time.sleep(5)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()

        driver.close()


test_obj = Contact()
test_obj.test_contact_details()
