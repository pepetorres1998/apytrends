from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class LoadFirefox:
    """ Load driver and browser in Firefox """
    def __init__(self, driver):
        """ Init of class, initializes the browser of webdriver in the variable browser """
        self.browser = self._return_browser(driver)

    def __del__(self):
        """ Called on garbage recolection, destroy the webdriver window, it can be stoped with an input() """
        self.browser.close()

    def _return_browser(self, driver):
        """ Return the browser of webdriver """
        try:
            print(driver)
            #opti = Options()
            #opti.set_headless(headless=True)
            br_path = str(driver)
            #browser = webdriver.Firefox(firefox_options=opti, executable_path=br_path)
            browser = webdriver.Firefox(executable_path=br_path)
            print('Headless Browser Invoked!')
            browser.implicitly_wait(10) #seconds
            return browser
        except:
            print('Exception ocurred when Initializing the browser')
            browser.close()

    def get_trending_realtime(self):
        """ Send the GET request to trending realtime """
        self.browser.get('https://trends.google.com.mx/trends/trendingsearches/realtime?geo=MX&category=all')

    def no_mames(self):
        """ This is a test function :v """
        print('no_mames')

if(__name__=='__main__'):
    browser = LoadFirefox('/home/jose/Dropbox/Drivers/geckodriver')
    browser.no_mames()
    browser.get_trending_realtime()
    input('Press any key')
