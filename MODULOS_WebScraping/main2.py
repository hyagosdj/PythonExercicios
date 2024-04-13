# type: ignore
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# https://peter.sh/experiments/chromium-command-line-switches/


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent

# Caminho para a pasto do chromedriver
CHROMEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless)
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CHROMEDRIVER_EXEC),
    )
    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )
    return browser


# chrome_browser.get('https://www.google.com.br/')
# sleep(30)
if __name__ == '__main__':
    TIME_TO_WAIT = 10
    # Example
    # options = ('--disable-gpu', '--no-sandbox',)
    # options = ('--headless', '--disable-gpu')
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com.br')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    # print(links[0])
    links[0].click()
    browser.find_element(
        By.XPATH, '//*[@id="selectLanguage"]/div/div/div[2]/select').click()
    browser.find_element(
        By.XPATH, '//*[@id="selectLanguage"]/div/div/div[2]/select/option[47]').click()

    # Dorme por 10 sec
    sleep(TIME_TO_WAIT)
