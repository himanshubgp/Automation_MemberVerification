import os
import time
from typing import Dict
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from src.config import Config
from src.constants import Constants as const, Attributes as attr, Urls

# load env file
load_dotenv()


class Automation:
    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver

    def login(self):
        """functionality to login into site and wait for user to enter captcha"""

        # get base url in browser
        self.driver.get(Urls.BASE_URL)
        # find usename tag and enter username
        
        self.driver.find_element(By.ID, attr.USERNAME_ID).send_keys(
            'Mo_Shahkund464')
        # find password tag and enter password
        self.driver.find_element(By.ID, attr.PASSWORD_ID).send_keys(
            os.getenv(const.PASSWORD)
        )
        # wait for a fixed time to get captcha intered by user
        time.sleep(Config.CAPTCHA_WAIT_TIME)

        # submit credentials/ click on login button
        self.driver.find_element(By.NAME, attr.LOGIN_BUTTON_NAME).click()

        # wait for a fixed time to get OTP intered by user
        time.sleep(Config.OTP_WAIT_TIME)

        # submit OTP click on login button
        self.driver.find_element(By.ID, attr.OTP_LOGIN_BUTTON_ID).click()
        # self.driver.find_element(By.NAME, attr.OTP_LOGIN_BUTTON_NAME).click()
        
        #click on Field Verification Button selection 
        # Wait until the button is clickable
        time.sleep(10)
        self.driver.find_element(By.XPATH, attr.FIELD_VERIFICATION_BUTTON).click()

    def verificationClick(self):
                        
        """Perform initial clicks for field verification."""
        try:
            # Wait for and click the rural radio button
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, attr.RURAL_RADIO_BUTTON))
            ).click()

            # Wait for and click the Application ID checkbox
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, attr.APPLICATION_ID_CHECKBOX))
            ).click()

            print("Verification selections completed.")
        except TimeoutException:
            print("Timeout while waiting for elements during verification click.")
        except Exception as err:
            print(f"An error occurred in verificationClick: {err}")

    def search_applicationId(self, rc_data: Dict):
        """navigate to search Application ID page and fill out details

        Args:
            rc_data (Dict): Ration card excel row
        """

        # enter Application ID number 
        application_id_num = str(rc_data.get(const.APPLICATION_ID_NUM)).strip()
        print(application_id_num)
        self.driver.find_element(By.ID, attr.APPLICATION_ID).send_keys(
            application_id_num)

        # click on show report  
        self.driver.find_element(By.ID, attr.SHOW_REPORT).click()

        #click on Verification View by Locating the link by its href containing a partial 
        # click on member link
        try:
            self.driver.find_element(By.XPATH, attr.VIEW_BUTTON).click()
            return True
        except NoSuchElementException:
            return False

        #Field Verification Name as Neelam Kumari   
        self.driver.find_element(By.ID, attr.FIELD_VERIFICATION_NAME).send_keys(
            'SANJIV KUMAR')

        #Auto Enter Designation as Block Supply Officer   
        self.driver.find_element(By.ID, attr.DESIGNATION_NAME).send_keys(
            'BLOCK SUPPLY OFFICER')
        
        # Enter Date of Application Verification   
        self.driver.find_element(By.ID, attr.VERIFICATION_DATE).send_keys(
            '12-12-2024')
        
        # Click on Choose File Button to Upload the pdf file
        try:
            self.driver.find_element(By.ID, attr.CHOOSE_FILE).click()
            return True
        except NoSuchElementException:
            return False
       
        # CLICKING ON CHOOSE FILE BUTTON AND FINDING THE PDF AND CLICKING OPEN BUTTON 
        self.driver.find_element(
                By.ID, attr.CHOOSE_FILE).send_keys(Config.CHOOSE_FILE_PATH + application_id_num.pdf)

        # CLICK ON UPDATE BUTTON
        self.driver.find_element(
                By.ID, attr.UPDATE).click()
        try:
            alert = Alert(self.driver) 
            alert.accept()
        except Exception as err:
            pass

    def check_for_member__adhaar_field_verification(self):
        """function to check for member addahar field verification
        """
        table = self.driver.find_element(By.ID, attr.TABLE_ID)
        index_to_check = []
        for index, row in enumerate(table.find_elements(By.XPATH, attr.ROW_XPATH)):
            row_data = [td.text for td in row.find_elements(
                By.XPATH, attr.DATA_XPATH)]
            # check if data has no adhaar
            if len(row_data) == 7 and not row_data[-2].strip():
                index_to_check.append(index-1)

        for idx in index_to_check:
            # click check box if adhar is null
            tag_id = attr.CHECK_BOX_ID.replace(const.INDEX, str(idx))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.ID, tag_id)))
            self.driver.find_element(
                By.ID, tag_id).click()

        #Click on first parameter for approval of TABLE_ID_VEHICLE_1
        self.driver.find_element(By.ID, attr.TABLE_ID_VEHICLE_1).click()

        #Click on first parameter for approval of TABLE_ID_MACHINE_2
        self.driver.find_element(By.ID, attr.TABLE_ID_MACHINE_2).click()

        #Click on first parameter for approval of TABLE_ID_REG_3
        self.driver.find_element(By.ID, attr.TABLE_ID_REG_3).click()

        #Click on first parameter for approval of TABLE_ID_INCOME_4
        self.driver.find_element(By.ID, attr.TABLE_ID_INCOME_4).click()

        #Click on first parameter for approval of TABLE_ID_PAYTAX_5
        self.driver.find_element(By.ID, attr.TABLE_ID_PAYTAX_5).click()

        #Click on first parameter for approval of TABLE_ID_PAYPROFTAX_6
        self.driver.find_element(By.ID, attr.TABLE_ID_PAYPROFTAX_6).click()

        #Click on first parameter for approval of TABLE_ID_WALLANDROOF_7
        self.driver.find_element(By.ID, attr.TABLE_ID_WALLANDROOF_7).click()

        #Click on first parameter for approval of TABLE_ID_ARGEQP_8
        self.driver.find_element(By.ID, attr.TABLE_ID_ARGEQP_8).click()

        #Click on first parameter for approval of TABLE_ID_CROPLAND_9
        self.driver.find_element(By.ID, attr.TABLE_ID_CROPLAND_9).click()

        #Click on first parameter for approval of TABLE_ID_ONEARC_FARMINGLAND_10
        self.driver.find_element(By.ID, attr.TABLE_ID_ONEARC_FARMINGLAND_10).click()

        #Click on first parameter for approval of TABLE_ID_GOVT_SERVICE_11
        self.driver.find_element(By.ID, attr.TABLE_ID_GOVT_SERVICE_11).click()

        # AFTER CLICKING ON NO TO ALL COLUMNS REMARKS TO BE WRITEDOWN
        self.driver.find_element(By.ID, attr.REMARKS).send_keys(
            'ACCEPT')

        # STATUS TO BE SELECTED 
        self.driver.find_element(By.ID, attr.STATUS).click()

        # IN STATUS TO Value for Fit To Be Selected 
        self.driver.find_element(By.ID, attr.VALUE_FOR_FIT_TO_BE_SELECTED).click()
    
        # SUBMIT TO FORWARD FOR AADHAR VERIFICATION
        
        if os.getenv(const.ENV) == 'prod':
            self.driver.find_element(
                By.ID, attr.SUBMIT_BUTTON_FORWARD_AADHAR_VERIFICATION).click()
            try:
                alert = Alert(self.driver) 
                alert.accept()
            except Exception as err:
                pass
    
    def search_member(self, rc_data: Dict):
        """navigate to search member page and fill out details

        Args:
            rc_data (Dict): Ration card excel row
        """
        #  click search member link
        self.driver.get(Urls.SEARCH_MEMBER_URL)

        # select distric dropdown
        select_element = self.driver.find_element(By.NAME, attr.DISTRIC_NAME)
        Select(select_element).select_by_value("224")

        # select subdivision dropdown
        select_element = self.driver.find_element(
            By.NAME, attr.SUBDIVISION_NAME)
        Select(select_element).select_by_value("0000022014")

        # select block/town
        select_element = self.driver.find_element(
            By.NAME, attr.BLOCK_TOWN_NAME)
        Select(select_element).select_by_value("01337")

        # enter ration card number
        
        rc_num = str(rc_data.get(const.RC_NUM)).strip()
        print(rc_num)
        self.driver.find_element(By.ID, attr.RC_NUMBER).send_keys(
            rc_num)

        # click on search button
        self.driver.find_element(By.ID, attr.SEARCH_BUTTON_ID).click()

        # click on member link
        try:
            self.driver.find_element(By.XPATH, attr.MEMBER_LINK_XPATH).click()
            return True
        except NoSuchElementException:
            return False

    def check_for_member_with_no_adhaar(self):
        """function to check for member with no addahar
        """
        table = self.driver.find_element(By.ID, attr.TABLE_ID)
        index_to_check = []
        for index, row in enumerate(table.find_elements(By.XPATH, attr.ROW_XPATH)):
            row_data = [td.text for td in row.find_elements(
                By.XPATH, attr.DATA_XPATH)]
            # check if data has no adhaar
            if len(row_data) == 7 and not row_data[-2].strip():
                index_to_check.append(index-1)

        for idx in index_to_check:
            # click check box if adhar is null
            tag_id = attr.CHECK_BOX_ID.replace(const.INDEX, str(idx))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
                (By.ID, tag_id)))
            self.driver.find_element(
                By.ID, tag_id).click()

    def proceed_for_upload_file_and_deletion(self, rc_data):
        """upload necessary metadata for deletion"""
        # write notice number
        self.driver.find_element(
            By.NAME, attr.NOTICE_ISSUE_NUMBER).send_keys(str(int(float(rc_data.get(const.NOTICE_NUM)))))

        # notice date
        self.driver.find_element(
            By.NAME, attr.NOTICE_ISSUE_DATE).send_keys(rc_data.get(const.NOTICE_DATE))
        self.driver.find_element(By.XPATH, "//html").click()

        # order number
        self.driver.find_element(
            By.NAME, attr.ORDER_ISSUE_NUMBER).send_keys(str(int(float(rc_data.get(const.ORDER_NO)))))

        # order date
        self.driver.find_element(
            By.NAME, attr.ORDER_ISSUE_DATE).send_keys(rc_data.get(const.ORDER_DATE))
        self.driver.find_element(By.XPATH, "//html").click()

        # marketing officer data
        select = self.driver.find_element(
            By.NAME, attr.SOURCE_OF_INFO_DELETION)
        Select(select).select_by_value("MO")

        time.sleep(1)
        self.driver.find_element(By.NAME, attr.MO_NAME).send_keys(
            'Krishnanand Anand')

        # reason for deletion
        select = self.driver.find_element(By.NAME, attr.REASON_FOR_DELETON)
        Select(select).select_by_value("P")

        # notice upload
        self.driver.find_element(
            By.NAME, attr.NOTICE_UPLOAD).send_keys(Config.NOTICE_FILE_PATH)

        # order upload
        self.driver.find_element(
            By.NAME, attr.ORDER_UPLOAD).send_keys(Config.ORDER_FILE_PATH)

        if os.getenv(const.ENV) == 'prod':
            self.driver.find_element(
                By.NAME, attr.FINAL_SUBMIT).click()
            try:
                alert = Alert(self.driver) 
                alert.accept()
            except Exception as err:
                pass

    def switch_to_next_window(self):
        """Switch to next window"""
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_current_window(self):
        """close current window and navigate to main"""
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
