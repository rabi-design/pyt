from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from time import sleep
from soup import Soup
from webdriver_manager.utils import chrome_version
import os, glob, shutil, subprocess, zipfile
import pyautogui as pg


def help_s():
    ver = chrome_version()[:2]
    print(ver)
    n = ""
    if ver == "95":
        n = 0
    elif ver == "94":
        n = 1
    elif ver == "93":
        n = 2

    li = Soup.bs("https://chromedriver.chromium.org/downloads")
    lis = li.find_all("li", class_="TYR86d wXCUfe zfr3Q")
    down = lis[n].find("a", class_="XqQF9c").get("href")
    print(down)
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", down])
    sleep(3)
    for i in range(4):
        pg.hotkey("tab")
    pg.hotkey("enter")
    # dri, no = bs_req(down)
    # print(dri)
    # url = dri.find("tbody").find_all("tr")[4].find("a").get("href")
    # url = "https://chromedriver.storage.googleapis.com/" + url


def nfreez():
    with zipfile.ZipFile('C:\\Users\\sml\\Downloads\\chromedriver_mac64.zip') as exi_zip:
        exi_zip.extract("chromedriver", "extensions")


def start_chrome(path):
    # Chrome起動
    options = webdriver.ChromeOptions()

    options.add_argument("start-maximized")
    options.add_argument('--user-data-dir={0}'.format(path))
    driver = webdriver.Chrome(options=options,
                              executable_path="extensions/chromedriver.exe")
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


def gfp_option(driver):
    driver.get("chrome-extension://fdpohaocaechififmbbbbbknoalclacl/options.html")
    sleep(5)
    driver.find_elements_by_class_name("options-input")[6].click()
    # driver.execute_script('return document.querySelectorAll(".options-input")[6].click()')
    sleep(2)
    pg.hotkey("left")
    sleep(1)
    pg.hotkey("enter")
    sleep(1)
    driver.quit()


def expand_shadow_element_gfp(driver):
    driver.get(
        "https://chrome.google.com/webstore/detail/gofullpage-full-page-scre/fdpohaocaechififmbbbbbknoalclacl?hl=ja")
    sleep(5)
    driver.execute_script('return document'
                          '.querySelector(".g-c-x").click()')

    sleep(3)
    pg.hotkey("left")
    sleep(2)
    pg.hotkey("enter")

    # return shadow_root


def expand_shadow_element_ext(driver, j):
    driver.get("chrome://extensions/")
    sleep(3)
    print(j)
    # j = str(j)
    # j = j.replace("\\", "\\\\")
    driver.execute_script('return document.querySelector("extensions-manager")'
                          '.shadowRoot.querySelector("extensions-toolbar")'
                          '.shadowRoot.querySelector("#packExtensions").click()')
    input()
    # sleep(3)
    # # driver.execute_script('return document.querySelector("extensions-manager")'
    # #                       '.shadowRoot.querySelector("extensions-toolbar")'
    # #                       '.shadowRoot.querySelector("extensions-pack-dialog")'
    # #                       '.shadowRoot.querySelector("cr-dialog").querySelector("#root-dir")'
    # #                       '.shadowRoot.querySelector("#input").value="{0}"'.format(j))
    # driver.execute_script('return document.querySelector("extensions-manager")'
    #                       '.shadowRoot.querySelector("extensions-toolbar")'
    #                       '.shadowRoot.querySelector("extensions-pack-dialog")'
    #                       '.shadowRoot.querySelector("cr-dialog").querySelector("#root-dir")'
    #                       ".setAttribute('focused_', '')")
    # driver.execute_script('return document.querySelector("html").setAttribute("class","in-dev-mode focus-outline-visible")')
    #
    # sleep(3)
    # print(j)
    # a = 'button-container'
    # driver.execute_script('return document.querySelector("extensions-manager")'
    #                       '.shadowRoot.querySelector("extensions-toolbar")'
    #                       '.shadowRoot.querySelector("extensions-pack-dialog")'
    #                       '.shadowRoot.querySelector("cr-dialog")'
    #                       '.querySelector("[slot= {0}]").querySelector(".action-button").setAttribute("aria-disabled", "false")'.format(a))
    # driver.execute_script('return document.querySelector("extensions-manager")'
    #                       '.shadowRoot.querySelector("extensions-toolbar")'
    #                       '.shadowRoot.querySelector("extensions-pack-dialog")'
    #                       '.shadowRoot.querySelector("cr-dialog")'
    #                       '.querySelector("[slot= {0}]").querySelector(".action-button").setAttribute("tabindex", "0")'.format(a))
    # driver.execute_script('return document.querySelector("extensions-manager")'
    #                       '.shadowRoot.querySelector("extensions-toolbar")'
    #                       '.shadowRoot.querySelector("extensions-pack-dialog")'
    #                       '.shadowRoot.querySelector("cr-dialog")'
    #                       '.querySelector("[slot= {0}]").querySelector(".action-button").removeAttribute("disabled")'.format(a))
    #
    #
    # driver.execute_script('return document.querySelector("extensions-manager")'
    #                       '.shadowRoot.querySelector("extensions-toolbar")'
    #                       '.shadowRoot.querySelector("extensions-pack-dialog")'
    #                       '.shadowRoot.querySelector("cr-dialog").querySelector("[slot={0}]").querySelector(".action-button").click()'.format(a))


# noinspection PyBroadException
def main():
    u_name = os.getlogin()
    ud_path = 'C:\\Users\\{0}\\AppData\\Local\\Google\\Chrome\\User Data'.format(u_name)
    driver2 = start_chrome(ud_path)

    expand_shadow_element_gfp(driver2)
    sleep(10)
    driver2.quit()
    gfp_id = "fdpohaocaechififmbbbbbknoalclacl"
    gfp_path = glob.glob(os.path.join(ud_path, "Default\Extensions", gfp_id, "*"))
    try:
        os.mkdir("extensions")
    except:
        pass
    driver2 = start_chrome(ud_path)
    for i in gfp_path:
        expand_shadow_element_ext(driver2, i)
    gfp_option(driver2)
    crx_path = glob.glob(os.path.join(ud_path, "Default\Extensions", gfp_id, "*.crx"))
    for i in crx_path:
        shutil.copyfile(i, "extensions\{0}".format(os.path.basename(i)))

    # x = input()
    # pg.hotkey("shift", "ctrl", "i")
    # sleep(1)
    # pg.hotkey("shift", "ctrl", "m")
    # sleep(1)
    # pg.hotkey("shift", "alt", "p")
    # sleep(50)
    driver2.quit()


if __name__ == "__main__":
    help_s()
    nfreez()
    main()
    # Googleにログイン
    # login_google(driver2)
