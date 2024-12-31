from pathlib import Path
from time import sleep

# https://pypi.org/project/selenium/
# Tem todos os links dos drivers dos navegadores que tem suporte
from selenium import webdriver
# Não tem mais a necessidade disto abaixo
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/

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
    # Example
    options = ('--disable-gpu', '--no-sandbox',)
    browser = make_chorme_browser(*options)

    # Como antes
    browser.get('https://www.google.com/')

    # Dorme por 10 segundos
    sleep(10)

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
