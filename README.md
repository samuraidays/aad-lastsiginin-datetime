# AzureAD LastSignIn DateTime
AzureADの最終サインイン日時を取得する

1. AzureADのアプリの登録からアプリを追加  
その際に"アプリケーションの許可"で"User.Read.All"と"AuditLog.Read.All"を許可する

2. テナントID、クライアントID、クライアントキーを環境変数として設定する  

```
export TENANT_ID="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  
export CLIENT_ID="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  
export CLIENT_KEY="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  
```

3. 実行  

```
python getLastSignInDateTime.py  
```

4. 結果をスプレッドシートに貼り付けて区切り文字を;(セミコロン)で列を区切る

```
$ python getLastSignInDateTime.py                        
1;XXXX@XXXX.com;2022-02-09T01:35:52Z
2;XXXX@XXXX.com;2022-02-08T23:44:01Z
3;XXXX@XXXX.com;2022-02-08T21:50:02Z
4;XXXX@XXXX.com;2022-02-04T01:15:03Z
```
