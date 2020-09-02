# Zebra Quotes User Flow Test
### Assignment
#### Verifications
- Verify that relevant and important elements and text are present on the page.
#### User Flow
- Write a test that will go through the user flow to receive insurance quotes.  With this test, you will need to enter the user, auto, and driver information.

### Framework
- Selenium Webdriver with Python Bindings and PyTest as the unit test framework.  The design pattern being used is a Page Object Model.  POM is used to have reusable WebElements/small helper methods separated from the actual test classes, allowing for cleaner code and easier test maintenance.
- Reason for using this framework over JS / Mocha was famarilty with python/pytest and time constraints.

### Methodologies
- Manually tested the user flow several times to get idea of how and what needs to tested
- "Whiteboarded" (pen and paper) the project layout
- Created the project dir and stubbed out the page methods for each page class
- Created a single test for the user flow
- Validated each element returned unique identifier then added locator attributes and interaction methods to the Page Objects
- Imported each module one at a time to Quote User flow test to that they were working as expected
- Added explict waits to most methods due to frequent "element not interactable" errors
### Improvements
- Ran out of time to built out PyTest Conftest, utilizing pytest fixtures for setup / teardown and create options for multiple browsers support
- Create more tests around error handling, and messaging.
- Add explicit waits method in a base class / custom driver for all interactions

# How to run tests with Selenium and PyTest 
1. Install Python 3.x
https://www.python.org/downloads/  
*Optionally, you can create a virtual env to isolate Python dependencies between projects*

2. In a terminal install the following packages:  
`pip install selenium`  
`pip install pytest`  

3. Add Python 3.x to your PATH environment variable
<details>
<summary>
<b><i><u>How to add python PATH in windows</u></i></b>
</summary>
<p>
	
- Search 'env'
- Edit the System Environment Variables
- Click on 'Environment Variables' button
- Click on 'New' in the System Variable section
- Enter `PYTHONPATH` in the Variable name field
- Enter in the Variable value field `C:\Python[version];C:\Python[version]\DLLs;C:\Python[version]\lib;C:\Python[version]\Scripts;`
- Select and click Edit on 'path' the list of system variables
- add `%PYTHONPATH%` to the end existing Path variable value
- open a terminal /cmd promp and type `python`.  Should be able to run the interpreter and see the python version

</p>
</details>

4. Clone repo to your local machine

### Driver Setup
 A driver is separate executable that WebDriver uses to control Browsers.  Use links below to get started:
   > [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

   > [Firefox Driver](https://github.com/mozilla/geckodriver/releases)
   	
#Note: Check Firefox + Chrome version & Selenium version compatibility before downloading geckodriver.
<details>
<summary>
<b><i><u>How to evoke browsers</u></i></b>
</summary>
<p>
	
- download chromedriver and extract the file
- copy file in desired location > Add path to executable_path variable in your tests
- `driver = webdriver.Chrome(executable_path = 'C:\\chromedriver.exe')`

</p>
</details>

### Running Tests Locally
To execute the tests just browse to the path where the selenium project is located in your terminal and type:
`py.test tests/car_insurnace_test.py`

### Commands for Running Tests

a)py.test [options]

	-s	used to display the output on the screen	
	-v      increase verbosity
	-h	help for more options 
	-n 	used to run tests in parallel
  example: `py.test -s -v tests/car_insurnace_test.py`

### Documentation
- [Offical Selenium Documentation](https://selenium.dev/documentation/en/)
- [Selenium with Python](https://selenium-python.readthedocs.io/index.html)
- [PyTest](https://docs.pytest.org/en/latest/index.html)
