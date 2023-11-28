# django_jwt_djoser
### Django 認証 Docs
- [Django] Customizing authentication in Django
- Using the Django authentication system
- https://docs.djangoproject.com/en/4.2/topics/auth/default/
- https://docs.djangoproject.com/en/4.2/topics/auth/customizing/
- [Djoser] Documentation
- https://djoser.readthedocs.io/en/latest/
- https://djoser.readthedocs.io/en/latest/getting_started.html
### Django JWT(json web token)認証 + Djoser(メール対応)
- アカウント仮登録
- アカウント本登録
- アカウント本登録再送信
- ログイン
- リフレッシュトークン
- 認証チェック
- ユーザー情報取得
- ユーザー情報変更
- ユーザーリスト取得
- メールアドレス変更
- メールアドレス変更確認
- パスワード変更
- パスワードリセット
- パスワードリセット確認
- アカウント削除

### API
##### Base Endpoints
- User Create
- User Activate
- User Resend Activation E-mail
- User
- User Delete
- Set Username
- Reset Username
- Reset Username Confirmation
- Set Password
- Reset Password
- Reset Password Confirmation
##### Token Endpoints
- Token Create
- Token Destroy
##### JWT Endpoints
- JWT Create
- JWT Refresh
- JWT Verify
##### Social Endpoints
- Provider Auth
##### Signals
- user_registered
- user_activated
- user_updated
##### WebAuthn
- Configuration
- Endpoints
- Example app
