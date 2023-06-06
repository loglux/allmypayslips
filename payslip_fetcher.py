from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time


class PayslipFetcher:

    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        # Set User-Agent to mimic a Chrome browser on Windows
        self.options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
        # Replace 'path_to_chromedriver' with the actual path to your local chromedriver.exe
        self.driver = webdriver.Chrome('chromedriver.exe', options=self.options)
        # Or use the remote webdriver for Selenium Grid
        # self.driver = webdriver.Remote("http://192.168.10.32:4444/wd/hub", options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        self.driver.get('https://inpay.es.rsmuk.com/PayslipPortal4/Secured/Home.aspx')
        # Wait for the login page to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'txtUserName')))
        # Enter the username and password
        self.driver.find_element(By.ID, 'txtUserName').send_keys(username)
        self.driver.find_element(By.ID, 'txtPassword').send_keys(password)
        # Find the login button and click it
        self.driver.find_element(By.ID, 'cmdOK').click()
        # Wait for the login process to complete
        time.sleep(2)

    def fetch_documents(self):
        # Go to the home page
        self.driver.get('https://inpay.es.rsmuk.com/PayslipPortal4/Secured/Home.aspx')
        # Create a list to store the payslip URLs
        payslip_urls = []
        # Find all rows in the table
        rows = self.driver.find_elements(By.CSS_SELECTOR, ".table.dataTable.no-footer tbody tr")
        # Exit the loop if there are no more rows
        if len(rows) == 0:
            return
        # Extract the date and the URL of the payslip for each row
        for row in rows:
            try:
                # Extract the URL of the payslip
                payslip_url = row.find_element(By.CSS_SELECTOR, "td a").get_attribute('href')
                # Add the payslip URL to the list
                payslip_urls.append(payslip_url)
            except NoSuchElementException:
                # Handle any other exception or skip the row if needed
                continue
        # Iterate over the payslip URLs
        for payslip_url in payslip_urls:
            # Navigate to the payslip page
            self.driver.get(payslip_url)
            time.sleep(2)
            # Wait for the PDF button to be clickable
            pdf_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, '_ctl0_CpBody_ExportToPDFBtn'))
            )
            # Click the PDF button
            pdf_button.click()
            # Wait for the download to complete
            time.sleep(2)
            # Go back to the home page
            self.driver.get('https://inpay.es.rsmuk.com/PayslipPortal4/Secured/Home.aspx')

    def fetch_p60_forms(self):
        # Go to the P60 forms page
        self.driver.get('https://inpay.es.rsmuk.com/PayslipPortal4/Secured/P60Viewer.aspx')
        # Wait for the page to load
        time.sleep(2)
        # Find the PDF button and click it to save the latest P60 form
        pdf_button = self.driver.find_element(By.ID, '_ctl0_CpBody_ExportToPDFBtn')
        pdf_button.click()
        # Wait for the download to complete
        time.sleep(2)
        # Find the dropdown for selecting tax years
        tax_year_dropdown = self.driver.find_element(By.ID, '_ctl0_CpBody_ddlTaxYear')
        # Get all the options in the dropdown
        options = tax_year_dropdown.find_elements(By.TAG_NAME, 'option')
        # Create a list to store the options
        option_list = []
        # Iterate over the options to select and save each P60 form
        for option in options:
            # Get the value (tax year) and text (displayed year) of each option
            value = option.get_attribute('value')
            text = option.text
            # Skip the currently selected option (latest P60 form)
            if option.is_selected():
                continue
            # Add the option to the list
            option_list.append((value, text))
        # Iterate over the option list to fetch and save P60 forms
        for option in option_list:
            value, text = option
            # Select the option to fetch the P60 form
            tax_year_dropdown = self.driver.find_element(By.ID, '_ctl0_CpBody_ddlTaxYear')
            tax_year_dropdown.send_keys(value)
            # Wait for the form to load
            time.sleep(2)
            # Find the PDF button and click it to save the P60 form
            pdf_button = self.driver.find_element(By.ID, '_ctl0_CpBody_ExportToPDFBtn')
            pdf_button.click()
            # Wait for the download to complete
            time.sleep(2)
            # Print the tax year and text for verification
            print(f"Tax Year: {value}, Displayed Year: {text}")
        # Go back to the P60 forms page
        self.driver.get('https://inpay.es.rsmuk.com/PayslipPortal4/Secured/P60Viewer.aspx')

    def fetch_p11d_forms(self):
        # Go to the P11D forms page
        self.driver.get('https://inpay.es.rsmuk.com/PayslipPortal4/Secured/P11DViewer.aspx')
        # Wait for the page to load
        time.sleep(2)
        # Find the PDF button and click it to save the P11D form
        pdf_button = self.driver.find_element(By.ID, '_ctl0_CpBody_ExportToPDFBtn')
        pdf_button.click()
        # Wait for the download to complete
        time.sleep(2)
        # Find the dropdown for selecting tax years
        tax_year_dropdown = self.driver.find_element(By.ID, '_ctl0_CpBody_ddlTaxYear')
        # Get all the options in the dropdown
        options = tax_year_dropdown.find_elements(By.TAG_NAME, 'option')
        # Create a list to store the options
        option_list = []
        # Iterate over the options to select and save each P11D form
        for option in options:
            # Get the value (tax year) and text (displayed year) of each option
            value = option.get_attribute('value')
            text = option.text
            # Add the option to the list
            option_list.append((value, text))
        # Iterate over the option list to fetch and save P11D forms
        print(option_list)
        # Iterate over the option list to fetch and save P11D forms
        for index in range(1, len(option_list)):  # Start from index 1
            value, text = option_list[index]
            # Select the option to fetch the P11D form
            tax_year_dropdown = Select(self.driver.find_element(By.ID, '_ctl0_CpBody_ddlTaxYear'))
            tax_year_dropdown.select_by_value(value)
            # Wait for the form to load
            time.sleep(5)
            # Find the PDF button and click it to save the P11D form
            pdf_button = self.driver.find_element(By.ID, '_ctl0_CpBody_ExportToPDFBtn')
            pdf_button.click()
            # Wait for the download to complete
            time.sleep(5)
            # Print the tax year and text for verification
            print(f"Tax Year: {text}")
        # Go back to the P11D forms page
        self.driver.get('https://inpay.es.rsmuk.com/PayslipPortal4/Secured/P11DViewer.aspx')

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    payslip_fetcher = PayslipFetcher()
    payslip_fetcher.login('<replace-with-your-username>', '<replace-with-your-password>')
    payslip_fetcher.fetch_documents()
    payslip_fetcher.fetch_p60_forms()
    payslip_fetcher.fetch_p11d_forms()
    payslip_fetcher.quit()
