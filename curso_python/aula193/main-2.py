from pathlib import Path
from time import sleep

# https://pypi.org/project/selenium/
# Tem todos os links dos drivers dos navegadores que tem suporte
from selenium import webdriver
# Não tem mais a necessidade disto abaixo
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html

# Caminho para a raiz do projeto
ROOT_FOLEDR = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROMEDRIVER_EXEC = ROOT_FOLEDR / 'drivers' / 'chromedirver.exe'


def make_chorme_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    # Não tem mais a necessidade disto abaixo
    # chrome_service = Service(
    #     executable_path=CHROMEDRIVER_EXEC
    # )

    browser = webdriver.Chrome(
        # Não tem mais a necessidade disto abaixo
        # service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Example
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chorme_browser(*options)

    # Como antes
    browser.get('https://www.google.com/')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello World!')

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)

# -------------------- OLD -----------------------
# chrome_options = webdriver.ChromeOptions()
# # Não tem mais a necessidade disto abaixo
# # crhome_service = Service(executable_path=CHROMEDRIVER_EXEC)
# chrome_browser = webdriver.Chrome(
#     # Não tem mais a necessidade disto abaixo
#     # service=crhome_service,
#     options=chrome_options,
# )


# chrome_browser.get('https://www.google.com.br/')
# time.sleep(30)
