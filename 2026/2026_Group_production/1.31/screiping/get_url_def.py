import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

"""
このファイルはURLの中のURLを取得し、さらにその中のURLを取得し、それらのURLをリストで出力する関数とそのテストをするコードが書かれています。
引数には、一番初めのURLが入力され、その中にあるURLをすべて取得します。
不必要なものは除外することが可能で、今回はページ以外の画像ファイルや、動画ファイルなどを除外しています。
また、不必要なパターンを入力することで、除外することができます。
"""

def get_url(base_url):

    # URLを取得するための準備
    ## 引数のURLのドメイン名だけを変数に代入する
    domain = urlparse(base_url).netloc

    ## 訪問済みURLを順番に保存するリストを作成
    visited_list = []

    ## すべてのURLが入るリストを作成し、引数のURLをリストに入力する
    to_visit = [base_url]

    # とってくるURLの中にページに飛ばないURLがあるため、それらを除外する条件を変数に代入する
    ## 除外する拡張子（画像・ファイル類）の指定する
    exclude_ext = (".jpg", ".jpeg", ".png", ".gif", ".pdf", ".css", ".js", ".zip", ".ico", ".svg", ".mp4", ".mov")

    ## 除外するURLパターンの指定(テストで使う際のみ効力あり)
    exclude_keywords = ("blog", "glossary", "corona", "system", "feature", "#", "abroad-")  

    # URLの中にあるURLを取得する
    while to_visit:
        url = to_visit.pop(0)

        ## すでにとってきているURLなら除外する
        if url in visited_list:
            continue
        
        ## とってきたURLをリストに代入する
        visited_list.append(url)

        # URLの中のURLの取得
        ## そのリンクが生きているかの確認(リンクが死んでいれば内部の情報が取れないため、処理を飛ばす)
        try:
            response = requests.get(url, timeout=10) 
        except requests.RequestException as e:
            print(f"リクエスト失敗: {url} ({e})")
            continue
        
        ## HTMLの内容を解析する
        soup = BeautifulSoup(response.text, "html.parser")

        # URLの中のURLをリストに保存する
        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            link_domain = urlparse(link).netloc

            ## 除外条件で必要ないものを除外する
            if not link.startswith("https://"):
                continue
            if link_domain != domain:
                continue
            if link.endswith(exclude_ext):
                continue
            if any(keyword in link for keyword in exclude_keywords):
                continue
            if link in visited_list or link in to_visit:
                continue

            to_visit.append(link)

    ## 訪問順にURLリストを返す
    return visited_list  

# 実行例
# urls = get_url("https://www.oca.ac.jp/")
# print(urls)
