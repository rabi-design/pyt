from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
import os
import pyautogui as pg
from selenium.webdriver.chrome.options import Options


def start_chrome():
    # Chrome起動
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('--user-data-dir=C:\\Users\\sml\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(options = options)
    driver.maximize_window()  # 画面サイズ最大化

    # GoogleログインURL
    # url = 'https://www.google.com/accounts?hl=ja-JP'
    # driver.get(url)

    return driver


def login_google(driver):
    # ログイン情報
    login_id = "yuki.ikura.kojima@gmail.com"
    login_pw = "yuki1311"

    # 最大待機時間（秒）
    wait_time = 30

    # IDを入力
    login_id_xpath = '//*[@id="identifierNext"]'
    # xpathの要素が見つかるまで待機します。
    sleep(10)
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH,
                                                                           login_id_xpath)))
    driver.find_element_by_name("identifier").send_keys(login_id)
    driver.find_element_by_xpath(login_id_xpath).click()

    # パスワードを入力
    login_pw_xpath = '//*[@id="passwordNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH,
                                                                           login_pw_xpath)))
    driver.find_element_by_name("password").send_keys(login_pw)
    sleep(1)  # クリックされずに処理が終わるのを防ぐために追加。
    driver.find_element_by_xpath(login_pw_xpath).click()

def expand_shadow_element(element):
    shadow_root = driver2.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

if __name__ == "__main__":
    driver2 = start_chrome()
    driver2.get("https://chrome.google.com/webstore/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl?hl=ja")
    elemen = driver2.find_element_by_class_name("g-c-R  webstore-test-button-label")
    shadow_root1 = expand_shadow_element(elemen)
    shadow_root1.click()
    sleep(10)
    y = input()
    for i in range(10):
        pg.hotkey("tab")
    pg.hotkey("enter")
    sleep(3)
    pg.hotkey("left")
    sleep(2)
    pg.hotkey("enter")
    sleep(20)
    driver2.quit()
    driver2 = start_chrome()
    sleep(3)
    driver2.get("chrome://extensions/")
    sleep(3)
    for i in range(4):
        pg.hotkey("tab")
    pg.hotkey("enter")
    x = input()
    pg.hotkey("shift", "ctrl", "i")
    sleep(1)
    pg.hotkey("shift", "ctrl", "m")
    sleep(1)
    pg.hotkey("shift", "alt", "p")
    sleep(50)
    driver2.quit()
    # Googleにログイン
    # login_google(driver2)
