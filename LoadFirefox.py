from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup as bf
import pandas as pd

class LoadFirefox:
    """ Load driver and browser in Firefox """
    def __init__(self, driver):
        """ Init of class, initializes the browser of webdriver in the variable browser """
        self.driver = driver
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

    def get_trending_realtime(self, geo='US', cat='all'):
        """ Send the GET request to trending realtime """
        (self.browser.get('https://trends.google.com.mx/trends/trendingsearches/realtime?geo='
        +str(geo)+'&category='+str(cat))) #this is the same function lol
        soup = bf(self.browser.page_source, 'html.parser')
        details_top = soup.find_all('div', {'class': 'details-top'})
        #print(details_top)
        marks = []
        #print(details_top[0])
        #print(details_top[0].find('a').text.strip())
        for i in details_top:
            a = i.find_all('a')
            a_list = []
            for j in a:
                a_list.append(j.text.strip())
            marks.append(', '.join(a_list))
        #print(marks)
        #print(len(marks))
        #print(df)
        return pd.Series(marks, index=list(range(len(marks))))

    def get_trending_daily(self, geo='US'):
        """ Send the GET request to trending realtime """
        (self.browser.get('https://trends.google.com/trends/trendingsearches/daily?geo='+
        geo)) #this is the same function lol
        details_top = self.browser.find_elements_by_class_name('details-top')
        count_title = self.browser.find_elements_by_class_name('search-count-title')
        summary_text = self.browser.find_elements_by_class_name('summary-text')
        #print(details_top)
        a = [i.find_element_by_tag_name('a').text for i in details_top]
        b = [j.text for j in count_title]
        c = [k.find_element_by_tag_name('a').text for k in summary_text]
        #links_news = [k.find_element_by_tag_name('a').get_attribute('href') for k in summary_text]
        #c = _NewsSeo(links_news[0], self.driver)
        #print(a)
        #print()
        #print(b)
        #print()
        #print(c)
        daily_dict = {
            'keyword': a,
            'searches': b,
            'first_new': c
        }
        return pd.DataFrame(daily_dict)


    def no_mames(self):
        """ This is a test function :v """
        print('no_mames')

class _NewsSeo():
    """ News SEO information (meta tags) """
    def __init__(self, link, driver):
        self.link = link
        self.browser = self._return_browser(driver)
        self.metas = self._get_meta()

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

    def _get_meta(self):
        self.browser.get(self.link)
        metas = self.browser.find_elements_by_tag_name('meta')
        metas_i = []
        for i in metas:
            try:
                metas_i.append(i.get_attribute('name'))
            except:
                continue
        print(metas_i)
        return metas

if(__name__=='__main__'):
    browser = LoadFirefox('/home/jose/Dropbox/Drivers/geckodriver')
    browser.no_mames()
    data = browser.get_trending_realtime()
    data2 = browser.get_trending_daily()
    print(data2)
    input('Press any key')
