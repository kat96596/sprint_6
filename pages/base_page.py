from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Элемент {locator} не найден")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Элементы {locator} не найдены")

    def click_element(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                          message=f"Элемент {locator} не кликабелен")
        element.click()

    def input_text(self, locator, text, time=10):
        element = self.find_element(locator, time)
        element.clear()
        element.send_keys(text)

    def wait_for_element_visible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        
        windows = self.driver.window_handles
        original_window = self.driver.current_window_handle
        
        for window in windows:
            if window != original_window:
                self.driver.switch_to.window(window)
                break
        
        return original_window

    def switch_to_window(self, window_handle):
        self.driver.switch_to.window(window_handle)

    def get_current_url(self):
        return self.driver.current_url

    def scroll_to_element(self, locator, time=10):
        element = self.find_element(locator, time)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    def is_element_visible(self, locator, time=5):
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False
