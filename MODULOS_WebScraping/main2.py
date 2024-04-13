from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome Options
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
    # Example
    # options = ('--disable-gpu', '--no-sandbox',)
    # options = ()
    options = ('--headless', '--disable-gpu')
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Dorme por 10 sec
    sleep(10)
