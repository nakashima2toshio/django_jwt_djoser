#### API / URL 一覧


| 機能                                   | URL                                               | Method |
| -------------------------------------- | ------------------------------------------------- | ------ |
| 1. アカウント仮登録 / Create User      | http://localhost:8000/api/auth/users/             | POST   |
| - メール                               | アカウント仮登録後のメールに、uid, token が URLに | メール |
| - tokenの取得                          | http://localhost:8000/api/auth/jwt/create/        | POST   |
| - アクティベーション / User Activate   | http://localhost:8000/api/auth/                   | POST   |
| 2. アカウント本登録                    | api/auth/users/activation/                        | POST   |
| 3. アカウント本登録再送信              | api/auth/users/resend_activation/                 |        |
| 4. ログイン / JWT: Login               | api/auth/jwt/create/                              |        |
| 5. リフレッシュトークン / JWT: Refresh | api/auth/jwt/refresh/                             |        |
| 6. 認証チェック / JWT: verify          | api/auth/jwt/verify/                              |        |
| 7. ユーザー情報取得                    | api/auth/users/me/                                | GET    |
| 8. ユーザー情報変更                    | api/auth/users/me/                                | POST   |
| 9. ユーザーリスト取得                  | api/auth/users/                                   |        |
| 10. メールアドレス変更                 | (Djoserのデフォルトでは提供されていない)          |        |
| 11. メールアドレス変更確認             | (Djoserのデフォルトでは提供されていない)          |        |
| 12. パスワード変更                     | api/auth/users/set_password/                      |        |
| 13. パスワードリセット                 | api/auth/users/reset_password/                    |        |
| 14. パスワードリセット確認             | api/auth/users/reset_password_confirm/            |        |
| 15. アカウント削除                     | api/auth/users/{username}/                        |        |
| 16. アカウント削除確認                 | (Djoserのデフォルトでは提供されていない)          |        |

#### DJOSER設定・json


| キー                       | 値                                      |
| -------------------------- | --------------------------------------- |
| PASSWORD_RESET_CONFIRM_URL | `/password/reset/confirm/{uid}/{token}` |
| USERNAME_RESET_CONFIRM_URL | `/username/reset/confirm/{uid}/{token}` |
| ACTIVATION_URL             | `/activate/{uid}/{token}`               |
| SEND_ACTIVATION_EMAIL      | True                                    |
| SERIALIZERS                | {}                                      |

#### アカウント・メールでの登録


| 機能名                 | エンドポイント                       | メソッド | 備考     |
| ---------------------- | ------------------------------------ | -------- | -------- |
| アカウント仮登録       | `/api/auth/users/`                   | POST     |          |
| アカウント本登録       | `/activate/{uid}/{token}/`           | GET      | メール内 |
| アカウント本登録再送信 | `/api/auth/users/resend_activation/` | POST     |          |
| ログイン               | `/api/auth/jwt/create/`              | POST     |          |
| リフレッシュトークン   | `/api/auth/jwt/refresh/`             | POST     |          |
| 認証チェック           | `/api/auth/jwt/verify/`              | POST     |          |

---

ユーザー情報取得                /api/auth/users/me/                 [GET]
ユーザー情報変更                /api/auth/users/me/                 [PUT]
ユーザーリスト取得               /api/auth/users/                    [GET]

---

メールアドレス変更               /api/auth/users/set_email/          [POST]
メールアドレス変更確認            /api/auth/users/set_email/          [POST]

---

パスワード変更                 /api/auth/users/set_password/       [POST]
パスワードリセット               /api/auth/users/reset_password/     [POST]
パスワードリセット確認           /api/auth/users/reset_password/     [POST]
アカウント削除                 /api/auth/users/me/                 [DELETE]

---

[Djoser]

---

Token Endpoints

---

Token Create                    /auth/token/create/                [POST]
Token Destroy                   /auth/token/destroy/               [POST]

---

JWT Endpoints

---

JWT Create                      /auth/jwt/create/                  [POST]
JWT Refresh                     /auth/jwt/refresh/                 [POST]
JWT Verify                      /auth/jwt/verify/                  [POST]

---

API                             Base Endpoints                      HTTP Method

---

User Create                     /users/                             [POST]
User Activate                   /users/activate/                    [POST]
User Resend Activation E-mail   /users/resend_activation/           [POST]
User                            /users/me/                          [GET, PUT, PATCH]
User Delete                     /users/me/                          [DELETE]
Set Username                    /users/set_username/                [POST]
Reset Username                  /users/reset_username/              [POST]
Reset Username Confirmation¶    /users/reset_username_confirm/      [POST]
Set Password                    /users/set_password/                [POST]
Reset Password                  /users/reset_password/              [POST]
Reset Password Confirmation     /users/reset_password_confirm/      [POST]

Email Change                    /users/set_email/                   [POST]
