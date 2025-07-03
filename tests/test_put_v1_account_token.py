
import uuid




def test_put_v1_account_token(account_helper):
    login = str(uuid.uuid4())
    email = login + '@mail.ru'
    password = '123456789'
    response = account_helper.register_new_user(login, email, password)
    assert response.status_code == 200