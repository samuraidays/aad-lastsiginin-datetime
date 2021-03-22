import json
import os
import requests
import argparse

# Microsoft GraphAPI クレデンシャル情報の取得
TENANT_ID = os.environ['TENANT_ID']
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_KEY = os.environ['CLIENT_KEY']


# Azureアクセスのためのアクセストークンの取得
def get_azure_access_token() -> str:

    # access_token を取得するためのヘッダ情報
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    payload = {
        'client_id': CLIENT_ID,
        'scope': 'https://graph.microsoft.com/.default',
        'grant_type': 'client_credentials',
        'client_secret': CLIENT_KEY
    }

    # access_token を取得するためのURLを生成
    TokenGet_URL = "https://login.microsoftonline.com/" + \
        TENANT_ID + "/oauth2/v2.0/token"
    # print(TokenGet_URL)

    # 実行
    response = requests.get(
        TokenGet_URL,
        headers=headers,
        data=payload
    )
    # requrest処理のクローズ
    response.close

    # その結果を取得
    jsonObj = json.loads(response.text)
    return jsonObj["access_token"]

def get_user_last_signin(access_token):

    # Microsoft Graphを実行するためのヘッダ情報
    headers = {
        'Authorization': 'Bearer %s' % access_token
    }

    # APIエンドポイント
    reqUrl = "https://graph.microsoft.com/beta/users/?$select=userPrincipalName,signInActivity"
    #print(reqUrl)

    # ユーザ情報のGetリクエスト
    res1 = requests.get(
        reqUrl,
        headers=headers
    )
    # requrest処理をクローズする
    res1.close

    # signInActivityの存在確認をしつつ、userPrincipalNameとlastSignInDateTimeを出力する
    try :
        data = res1.json()['value']
        for index, item in enumerate(data):
            if item.get('signInActivity') is None:
                print(str(index+1) + ';' + item['userPrincipalName'] + ';' + 'No-SignInActivity')
            else:
                print(str(index+1) + ';' + item['userPrincipalName'] + ';' + item['signInActivity']['lastSignInDateTime'])
        return res1.json()['value']
    except KeyError :
        print(res1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='各IDの最終サインイン日時を取得する')
    args = parser.parse_args()

    access_token = get_azure_access_token()
    get_user_last_signin(access_token)

    #print("")
    #print("取得時間:{0}".format(generate_time) + " [sec]")
    #print("取得アクセストークン：")
    #print(access_token)
    #print("")