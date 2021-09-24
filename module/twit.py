from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def twit(url):
    options = Options()
    # options.add_argument('--hide-scrollbars')  # スクロールバーを消す
    # options.add_argument('--incognito')  # シークレットモード
    # options.add_argument('--headless')  # ヘッドレス（ブラウザが見えなくなります。テスト終了後にこのオプションを追加するのがよい）
    driver = webdriver.Chrome(options=options)  # パスが通っているときの記述
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
    sleep(6)
    html = driver.page_source.encode('utf-8')
    bs = BeautifulSoup(html, "html.parser")
    return driver, bs


if __name__ == "__main__":
    a, b = twit("https://twitter.com/search?q=%23%E3%83%84%E3%82%A4%E3%83%83%E3%82%BF%E3%83%BC")
    print(b)
    a.close()
    a.quit()
