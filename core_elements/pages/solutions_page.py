from retry import retry
from selenium.webdriver.common.by import By
from core_elements.models.elements import Button, TextBox
from core_elements.project_decorators import log_click_button
from core_elements.pages.base_page import BasePage


class Solutions(BasePage):

    MULTIPLATFORM = (By.XPATH, '//a[@id="mp-scroll"]/span')
    PREMIUM_SECURITY = (By.XPATH, '//div[@id="MultiplatformSecurity"]//h3[contains(text(), "PREMIUM SECURITY")]')
    BUY_PREMIUM_SECURITY = (By.XPATH, f'{PREMIUM_SECURITY[1]}/..//a[contains(text(), "Cumpără")]')
    PRICE_INFORMATION = (By.XPATH, f'{PREMIUM_SECURITY[1]}/../div/span')

    def __init__(self):
        super(Solutions, self).__init__()

        self.driver.wait_for_element_to_be_visible(self.MULTIPLATFORM)

    @retry(tries=3, delay=1)
    @log_click_button
    def click_multiplaform(self):
        Button(self.MULTIPLATFORM).click()

    @property
    def premium_security(self):
        return TextBox(self.PREMIUM_SECURITY)

    @retry(tries=3, delay=1)
    @log_click_button
    def click_cumpara_premium_security(self):
        Button(self.BUY_PREMIUM_SECURITY).click(check_element=True)

    @property
    def old_price(self):
        return TextBox(self.driver.get_locator_by_index(self.PRICE_INFORMATION, index=1))

    @property
    def discount(self):
        return TextBox(self.driver.get_locator_by_index(self.PRICE_INFORMATION, index=2))

    @property
    def new_price(self):
        return TextBox(self.driver.get_locator_by_index(self.PRICE_INFORMATION, index=3))

    def get_price_information_premium_security(self):
        """
        Returns dictionary with price information for 'PREMIUM SECURITY'
        All values are 'STR'
        """
        return {'old_price': self.old_price.contents,
                'discount': self.discount.contents,
                'last_price': self.new_price.contents
                }
