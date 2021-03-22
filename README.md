# AzureAD LastSignIn DateTime
AzureADの最終サインイン日時を取得する

1. AzureADのアプリの登録からアプリを追加  
その際に"アプリケーションの許可"で"User.Read.All"と"AuditLog.Read.All"を許可する

2. テナントID、クライアントID、クライアントキーを環境変数として設定する

3. 実行
    `python getLastSignInDateTime.py`