from hillel_api import *
import onesecmail

def test_reset_password():
    user_data = {
    "email": "biu5yci087@dcctb.com"
    }
    r = auth.resetpassword(s, user_data)
    r_json = after_processsing(r) 
    assert r.status_code == 200, "Wrong status code"
    assert r_json["status"] == "ok", "Key 'status' is not ok"
    # далі просто приклад того, як може буть реалізований тест, це не працючий код
    mailbox = onesecmail.get("biu5yci087@dcctb.com")
    assert len(mailbox) >= 1
    assert mailbox[0].header == "Password reset"
    # ідея для покращеня тест-світу: додати дії, що призведуть до зміни пароля та
    # тест на вхід з новим паролем
