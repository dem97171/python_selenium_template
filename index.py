import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

dir_name = "./images/"


def main():
    # config.ini読み込み
    _ini = configparser.ConfigParser()
    if os.path.exists("./config.ini"):
        _ini.read("./config.ini")
    else:
        sys.stderr.write('%s が見つかりません' % INI_FILE)
        sys.exit(2)

    # 捜査開始のURL
    _url = "https://s-portal.cloud.global.fujitsu.com/SK5PCOM001/"

    # プラウザ起動（Chrome）
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,1024')
    options.add_argument('--no-sandbox')  # Running as root without --no-sandbox is not supported. See https://crbug.com/638180

    driver = webdriver.Chrome(executable_path="./vendor/driver/chromedriver", chrome_options=options,
                              service_args=["--debug", "--log-path=./logs/debug.log"])

    # 作業topページを開く
    driver.get(_url)  # 画面get
    time.sleep(2)  # 読み込み待機時間
    driver.save_screenshot(dir_name + "01_top.png")  # imagesフォルダにスクリーンショットを保存

    # Loginボタンをクリックしてlogin画面を開く
    driver.find_element_by_class_name("login-link").click()
    time.sleep(2)
    driver.save_screenshot(dir_name + "02_login.png")  # imagesフォルダにスクリーンショットを保存

    # Loginフォームに値を入力してログインボタンをクリック
    driver.find_element_by_id("keiyakuno").send_keys(_ini['login']['keiyakuno'])
    driver.find_element_by_id("username").send_keys(_ini['login']["username"])
    driver.find_element_by_id("password").send_keys(_ini['login']['password'])
    driver.save_screenshot(dir_name + "03_login_input.png")  # imagesフォルダにスクリーンショットを保存

    driver.find_element_by_id("Submit").click()
    time.sleep(2)
    driver.save_screenshot(dir_name + "04_login_result.png")  # imagesフォルダにスクリーンショットを保存

    _unExpectedUrl = "https://k5-authentication.paas.cloud.global.fujitsu.com/cloudlink/module.php/core/loginuserpass.php?"
    if driver.current_url == _unExpectedUrl:
        closeSelenium(driver)   # ログインに失敗したらselenium終了


    closeSelenium(driver)


def closeSelenium(_driver):
    _driver.save_screenshot(dir_name + "05_login_result.png")  # imagesフォルダにスクリーンショットを保存
    _driver.quit()
    sys.exit()


main()
