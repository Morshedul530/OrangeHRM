from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class EmergencyContacts():
    def test_emergency_contacts_details(self):
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

        # Click Emergency Contacts
        driver.find_element(By.LINK_TEXT, 'Emergency Contacts').click()

        add = driver.find_element(By.ID, 'btnAddContact')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'btnCancel')
        cancel.click()
        time.sleep(2)

        add = driver.find_element(By.ID, 'btnAddContact')
        add.click()
        time.sleep(2)

        name = driver.find_element(By.ID, 'emgcontacts_name')
        name.clear()
        name.send_keys('Md: Mahamud Hasan')

        relationship = driver.find_element(By.ID, 'emgcontacts_relationship')
        relationship.clear()
        relationship.send_keys('Brother')

        home_telephone = driver.find_element(By.ID, 'emgcontacts_homePhone')
        home_telephone.clear()
        home_telephone.send_keys('+8809678910')

        mobile = driver.find_element(By.ID, 'emgcontacts_mobilePhone')
        mobile.clear()
        mobile.send_keys('01746604763')

        work_telephone = driver.find_element(By.ID, 'emgcontacts_workPhone')
        work_telephone.clear()
        work_telephone.send_keys('+8809645678')

        save = driver.find_element(By.ID, 'btnSaveEContact')
        save.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'checkAll')
        status = checkbox.is_selected()

        if not status:
            checkbox.click()
            time.sleep(2)

        delete = driver.find_element(By.ID, 'delContactsBtn')
        delete.click()
        time.sleep(2)

        # Add Attachment
        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()
        time.sleep(2)

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(2)

        select_file = driver.find_element(By.ID, 'ufile')
        select_file.send_keys('C:\\Users\\morsh\\Desktop\\selenium_logo.png')
        time.sleep(2)

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('The image uploaded successfully')

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()

        if not status:
            checkbox.click()
            time.sleep(2)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()
        time.sleep(2)

        driver.close()


test_obj = EmergencyContacts()
test_obj.test_emergency_contacts_details()
