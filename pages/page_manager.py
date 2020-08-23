from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import login_page_locators
from base import drivers
import time
driver = drivers.configure_dirvers().config_driver()


class page_manager(drivers.configure_dirvers):
    def __init__(self):
        super().__init__()

    # ---------------------function 1-----------------------
    permissions = login_page_locators.login_page_locators().clear_permissions
    def clear_all_permissions(self):
        wait = WebDriverWait(driver, 20)
        for i in self.permissions:
            X = wait.until(EC.presence_of_element_located((By.ID, i)))
            X.click()

    # ---------------------function 2-----------------------
    search_guide = login_page_locators.login_page_locators().search_guide
    search_field = login_page_locators.login_page_locators().search_field
    searched_click = login_page_locators.login_page_locators().searched_click
    def lets_search(self):
        self.clear_all_permissions()
        wait = WebDriverWait(driver, 60)
        for i in self.search_guide:
            element = wait.until(EC.presence_of_element_located((By.ID, i)))
            element.click()

        locations = ['HSR', 'mara']
        for i in locations:
            time.sleep(2)
            element = wait.until(EC.presence_of_element_located((By.ID, self.search_field)))
            driver.find_element_by_id(self.search_field).send_keys(i)

            WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, 'com.nobroker.app:id/loading_indicator')))
            print('------------------')
            driver.tap([(390, 885)], 900)

    # ---------------------function 3-----------------------
    search_params = login_page_locators.login_page_locators().search_params
    def search_parameters(self):
        self.lets_search()
        for i in self.search_params:
            wait = WebDriverWait(driver, 5)
            element = wait.until(EC.presence_of_element_located((By.ID, i)))
            element.click()
        driver.tap([(538, 1830)], 900)



page_manager().search_parameters()
