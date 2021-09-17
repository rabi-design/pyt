from bs4 import BeautifulSoup
import requests


class soup:
    def __init__(
            self,
            f="t",
            ses_id: str = "",
            ses_pass: str = "",
            ses_token: str = "",
            login_url: str = "",
            id_l: str = "",
            password: str = ""
    ):
        self.f = f
        self.ses_id = ses_id
        self.ses_pass = ses_pass
        self.ses_token = ses_token
        self.login_url = login_url
        self.id_l = id_l
        self.password = password

    def login(self):
        ses = requests.session()
        res = ses.get(self.login_url)
        soup1 = BeautifulSoup(res.text, "html.parser")
        login_data = {
            self.ses_id: self.id_l,
            self.ses_pass: self.password
        }
        get_token = soup1.find(attrs = {"name": self.ses_token}).get("value")
        login_data[self.ses_token] = get_token
        ses.post(self.login_url, data = login_data)
        return ses

    def bs(self, url):
        # noinspection PyBroadException
        try:
            if self.f == "t":
                req = requests.get(url)
            elif self.f == "f":
                req = self.login().get(url)

            soup1 = BeautifulSoup(req.text, "html.parser")
            return soup1

        except:
            print("error")

    def main(self):
        url = "https://www.jetbrains.com/pycharm/download/download-thanks.html"
        return self.bs(url)


if __name__ == "__main__":
    ss = soup()
    print(ss.main())# test
