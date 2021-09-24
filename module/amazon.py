# -*- coding: utf-8 -*-
#  https://www.amazon.co.jp/%E3%83%A9%E3%83%95%E3%83%9E-Lafuma-%E3%83%9E%E3%82%AD%E3%82%B7%E3%83%88%E3%83%A9%E3%83%B3%E3%82%B6%E3%83%83%E3%83%88-TRANSAT-LFM2652/dp/B016Y20WRS/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=B016Y20WRS&qid=1632276790&s=sports&sr=1-1#HLCXComparisonWidget_feature_div

from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def amazon(asin_code):
    options = Options()
    # options.add_argument('--hide-scrollbars')  # スクロールバーを消す
    # options.add_argument('--incognito')  # シークレットモード
    # options.add_argument('--headless')  # ヘッドレス（ブラウザが見えなくなります。テスト終了後にこのオプションを追加するのがよい）
    driver = webdriver.Chrome(options = options)  # パスが通っているときの記述
    url = "https://www.amazon.co.jp/dp/" + asin_code
    while True:
        # noinspection PyBroadException
        try:
            WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located)
            driver.get(url)
            break
            # ↑キャプチャ対象のURLに移動する　画像や宣伝の多いサイトは突如タイムアウトエラーが頻発することがあるので　
        except:
            pass
            # ここにドライバーの再起動の記述を書く
    sleep(10)
    html = driver.page_source.encode('utf-8')
    bs = BeautifulSoup(html, "html.parser")
    return driver, bs


if __name__ == "__main__":
    a, b = amazon("B016Y20WRS").find("title")
    print(b)
    a.close()
    a.quit()
