import hillel_api
import unittest

class QAAPI_tests(unittest.TestCase):

    def test_01_sigin_positive(self):
        s = hillel_api.s
        user_data = {
        "email": "qam2608@2022test.com",
        "password": "Qam2608venv",
        "remember": False
        }
        r = hillel_api.auth_signin(s, user_data)
        self.assertEqual(r.status_code, 200, "Wrong status code")
        r_json = hillel_api.after_processsing(r)
        self.assertEqual(r_json["status"], "ok", "Key 'status' is not ok")
    
    def test_02_sigin_negative(self):
        s = hillel_api.s
        user_data = {
        "email": "qam@2022test.com",
        "password": "Qam2",
        "remember": False
        }
        r = hillel_api.auth_signin(s, user_data)
        self.assertEqual(r.status_code, 400, "Wrong status code")
        r_json = hillel_api.after_processsing(r)
        self.assertEqual(r_json["status"], "error", "Key 'status' is not error")


if __name__ == '__main__':
    unittest.main(verbosity=2)
