# Payslip Fetcher

This script allows you to fetch all your payslips, P60 and P11D forms from rsmuk.com portal. 

## Prerequisites

- Python 3.9+
- Selenium module (`pip install selenium`)
- Chrome browser and Chrome WebDriver or Selenium Grid

## Installation

1. Clone the repository:

```bash
git clone https://github.com/loglux/allmypayslips.git
```


2. Install the required dependencies:
```bash
pip install selenium
```

3. Download the Chrome WebDriver from the official website: [Chrome WebDriver Downloads](https://sites.google.com/chromium.org/driver/downloads?authuser=0)

4. Place the downloaded Chrome WebDriver executable in the project's directory.

Script reffers to the Windows version of the webdriver (webdriver.exe). Update it, if you use Mac or Linux.

Alternatively to steps 3 and 4, you can use Selenium Grid instead of webdriver, just update 'self.driver =' uncommenting and commenting out correspodning lines.

## Usage

1. Open the `payslip_fetcher.py` script in a text editor.

2. Replace the placeholders with your username and password in the `login` method:

```python
payslip_fetcher.login('<replace-with-your-username>', '<replace-with-your-password>')
```

Save the changes.

Run the payslip_fetcher.py script:
```python 
python payslip_fetcher.py
```

### Headless Mode

By default, the PayslipFetcher script runs in headless mode, which means the Chrome browser runs in the background without a visible UI. If you want to disable headless mode and run the script with a visible browser window, you can comment out the following line in the `PayslipFetcher` class:

```python
# self.options.add_argument("--headless=new")
```

## Notes
Ensure that the Chrome browser is installed and compatible with the Chrome WebDriver version.
You can also use Selenium Grid by configuring the remote WebDriver URL in the script.
All files are saved into a default directory (Downloads)

