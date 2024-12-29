import time
from src.utils import Utils
from src.web_driver import WebDriver
from src.automation import Automation


def main():
    """Entrypoint Function"""
    # create chrome driver instance
    web_driver = WebDriver()
    driver = web_driver.get_driver()

    # utility function
    utils = Utils()

    # create automation instance
    automation = Automation(driver)

    # Step 1: Login to the page using credentials
    print("Logging in...")
    automation.login()
    print("Login successful.")
    
    # Step 2: Start Ration Card verification process
    print("Initiating verification process...")
    automation.verificationClick()
    print("Verification buttons clicked.")


    # Step 3: Read Excel to get ration card data
    print("Reading Excel file for ration card data...")
    rc_data_list = utils.read_excel()
    print(f"Loaded {len(rc_data_list)} records from the Excel file.")

    # Step 4: Iterate through each record
    for index, rc_data in enumerate(rc_data_list, start=1):
        print(f"Processing record {index}/{len(rc_data_list)}: {rc_data}")
        
        # Search for the application ID
        member_found = automation.search_applicationId(rc_data)
        if not member_found:
            print(f"Application ID not found for record {index}. Skipping...")
            continue

        # Step 5: Switch to the new window for detailed actions
        print("Switching to the next window...")
        automation.switch_to_next_window()

        # Step 6: Perform Aadhaar field verification
        print("Performing Aadhaar field verification...")
        automation.check_for_member__adhaar_field_verification()

        # Step 7: Close the current window
        print("Closing the current window...")
        automation.close_current_window()
        time.sleep(2)  # Optional: Pause before processing the next record

    print("Automation process completed successfully.")

    if driver:
        print("Closing the WebDriver...")
        driver.quit()
        print("Automation script finished.")

    #for rc_data in rc_data_list:
        #member_found = automation.search_applicationId(rc_data)
        #if not member_found:
            #continue
        #automation.switch_to_next_window()
        #automation.check_for_member__adhaar_field_verification()
        #automation.proceed_for_upload_file_and_deletion(rc_data)
        #time.sleep(2)
        #automation.close_current_window()
        #time.sleep(2)


if __name__ == "__main__":
    main()
