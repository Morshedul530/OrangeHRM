from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class Immigration():
    def test_immigration_records(self):
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

        # Click Immigration
        driver.find_element(By.LINK_TEXT, 'Immigration').click()

        # Assigned Immigration Records
        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(1)

        cancel = driver.find_element(By.ID, 'btnCancel')
        cancel.click()
        time.sleep(1)

        add = driver.find_element(By.ID, 'btnAdd')
        add.click()
        time.sleep(1)

        document = driver.find_element(By.ID, 'immigration_type_flag_1')
        status = document.is_selected()
        if not status:
            document.click()
            time.sleep(1)

        number = driver.find_element(By.ID, 'immigration_number')
        number.clear()
        number.send_keys('19813090639100765')
        time.sleep(1)

        issued_date = driver.find_element(By.ID, 'immigration_passport_issue_date')
        issued_date.clear()
        issued_date.send_keys('2022-06-16')
        time.sleep(1)

        expiry_date = driver.find_element(By.ID, 'immigration_passport_expire_date')
        expiry_date.clear()
        expiry_date.send_keys('2027-06-16')
        time.sleep(1)

        eligible_status = driver.find_element(By.ID, 'immigration_i9_status')
        eligible_status.clear()
        eligible_status.send_keys('Eligible')
        time.sleep(1)

        issued_by = driver.find_element(By.ID, 'immigration_country')
        sel = Select(issued_by)
        sel.select_by_value('BD')
        time.sleep(1)

        eligible_review_date = driver.find_element(By.ID, 'immigration_i9_review_date')
        eligible_review_date.clear()
        eligible_review_date.send_keys('2024-06-12')
        time.sleep(1)

        comments = driver.find_element(By.ID, 'immigration_comments')
        comments.clear()
        comments.send_keys('Immigration was granted.')
        time.sleep(1)

        save = driver.find_element(By.ID, 'btnSave')
        save.click()
        time.sleep(2)

        checkbox = driver.find_element(By.ID, 'immigrationCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
            time.sleep(1)

        delete = driver.find_element(By.ID, 'btnDelete')
        delete.click()
        time.sleep(2)

        # Add Attachment
        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(1)

        cancel = driver.find_element(By.ID, 'cancelButton')
        cancel.click()
        time.sleep(1)

        add = driver.find_element(By.ID, 'btnAddAttachment')
        add.click()
        time.sleep(1)

        select_file = driver.find_element(By.ID, 'ufile')
        select_file.send_keys('C:\\Users\\morsh\\Desktop\\selenium_logo.png')
        time.sleep(1)

        comment = driver.find_element(By.ID, 'txtAttDesc')
        comment.send_keys('The image uploaded successfully')
        time.sleep(1)

        upload = driver.find_element(By.ID, 'btnSaveAttachment')
        upload.click()
        time.sleep(1)

        checkbox = driver.find_element(By.ID, 'attachmentsCheckAll')
        status = checkbox.is_selected()
        if not status:
            checkbox.click()
            time.sleep(1)

        delete = driver.find_element(By.ID, 'btnDeleteAttachment')
        delete.click()
        time.sleep(1)

        driver.close()


test_obj = Immigration()
test_obj.test_immigration_records()