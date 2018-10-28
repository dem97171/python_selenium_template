import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    url = "https://s-portal.cloud.global.fujitsu.com/SK5PCOM001/"

    # プラウザ起動（Chrome）
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,1024')
    options.add_argument('--no-sandbox')  # Running as root without --no-sandbox is not supported. See https://crbug.com/638180

    driver = webdriver.Chrome(executable_path="./vendor/driver/chromedriver", chrome_options=options,
                              service_args=["--debug", "--log-path=./logs/debug.log"])

    # 作業topページを開く。
    dir_name = "./images/"
    driver.get(url)  # 画面get
    time.sleep(2)  # 読み込み待機時間
    driver.save_screenshot(dir_name + "01_top.png")  # imagesフォルダにスクリーンショットを保存

    # Loginボタンをクリックしてlogin画面を開く
    driver.find_element_by_class_name("login-link").click()
    time.sleep(2)
    driver.save_screenshot(dir_name + "02_login.png")  # imagesフォルダにスクリーンショットを保存

    # プラウザを閉じる
    driver.quit()


main()
