
import uuid



def test_put_v1_account_email(account_helper):
    login = str(uuid.uuid4())
    email = login + '@mail.ru'
    password = '123456789'
    response = account_helper.register_new_user(login, email, password)
    assert response.status_code == 200
    response = account_helper.login(login, password)
    assert response.status_code == 200
    new_email = f'{uuid.uuid4()}@mail.com'
    response = account_helper.change_email(login, password, new_email)
    assert response.status_code == 200
    response = account_helper.login(login, password)
    assert response.status_code == 403

    activation_token = account_helper.find_token(login)
    response = account_helper.dm_api_account.account_api.put_v1_account_token(token=activation_token)
    assert response.status_code == 200

    response = account_helper.login(login, password)
    assert response.status_code == 200
