import requests

IFTTT_URL = "https://maker.ifttt.com/trigger/{event}/with/key/rMTojRrPmXho8xbr1bUPS"


def get_issues():
    print("get_issues start")
    response = requests.get('https://github.com/timeline.json')
    print(response.status_code)    # HTTPのステータスコード取得
    print(response.text)    # レスポンスのHTMLを文字列で取得
    print("get_issues end")

    return response.text


def post_issues():
    print("post_issues start")
    # "Content-Type: application/json"
    # https://maker.ifttt.com/trigger/{event}/with/key/rMTojRrPmXho8xbr1bUPS
    response = requests.get(IFTTT_URL.format(event="task"))
    print(response.status_code)    # HTTPのステータスコード取得
    print(response.text)    # レスポンスのHTMLを文字列で取得
    print("post_issues end")


if __name__ == '__main__':
    res = get_issues()
    post_issues()


print('モジュール名：{}'.format(__name__))  # 実行したモジュール名を表示する
