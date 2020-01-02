import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import configparser

dir_name = "./images/"


class GsTaikin:
    def __init__(self):
        # config.ini読み込み
        self._ini = configparser.ConfigParser()
        if os.path.exists("./configGs.ini"):
            self._ini.read("./configGs.ini")
        else:
            sys.stderr.write('configGsTaikin.iniが見つかりません')
            sys.exit(2)

        # 捜査開始のURL
        self._url = "https://demo.groupsession.jp/gsession"

        # プラウザ起動（Chrome）
        options = Options()
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,1024')
        # options.add_argument('--no-sandbox')  # Running as root without --no-sandbox is not supported. See https://crbug.com/638180

        self.driver = webdriver.Chrome(executable_path="./vendor/driver/chromedriver", chrome_options=options,
                                       service_args=["--debug", "--log-path=./logs/debug.log"])

    def work(self):

        # 作業topページを開く
        self.driver.get(self._url)  # 画面get
        time.sleep(2)  # 読み込み待機時間
        self.driver.save_screenshot(dir_name + "01_top.png")  # imagesフォルダにスクリーンショットを保存

        # Loginフォームに値を入力してログインボタンをクリック
        self.driver.find_element_by_name("cmn001Userid").send_keys(self._ini['gsLogin']['username'])
        self.driver.find_element_by_name("cmn001Passwd").send_keys(self._ini['gsLogin']['password'])
        self.driver.save_screenshot(dir_name + "02_login_input.png")  # imagesフォルダにスクリーンショットを保存

        self.driver.find_element_by_class_name("login_btn").click()
        time.sleep(2)
        self.driver.save_screenshot(dir_name + "03_login_result.png")  # imagesフォルダにスクリーンショットを保存

        # iframeに入る
        iframe = self.driver.find_element('name', 'body')
        self.driver.switch_to.frame(iframe)
        self.driver.find_element_by_id("sts_zaiseki").click()
        time.sleep(1)
        self.driver.find_element_by_id("zskmain").find_element_by_class_name('btn_base0_1').click()
        time.sleep(1)
        self.driver.save_screenshot(dir_name + "04_帰宅.png")  # imagesフォルダにスクリーンショットを保存

        self.closeSelenium(self.driver)

    def closeSelenium(self, _driver):
        _driver.quit()
        sys.exit()
