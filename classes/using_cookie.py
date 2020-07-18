from header import *


class using_cookie:
    # @app.route("/set_cookie/<value>")
    @staticmethod
    def set_cookies(value):
        if value is not None:
            resp = make_response("Cookie has been created")
            import datetime
            expired_date = datetime.datetime.now()
            expired_date = expired_date + datetime.timedelta(days=5)
            resp.set_cookie("cookie_values", value, expires=expired_date)
        else:
            resp = make_response("Cookie has not been created! Value is None!")

        return resp

    # @app.route("/get_cookie")
    @staticmethod
    def get_cookies():
        if request.cookies.get("cookie_values"):
            return request.cookies.get("cookie_values")
        else:
            return "No any cookie is available!"

    # @app.route("/del_cookie")
    @staticmethod
    def del_cookie():
        if request.cookies.get("cookie_values"):
            resp = make_response("Cookie has been deleted!")
            resp.set_cookie("cookie_values", max_age=0)
            return resp
        else:
            return "No any cookie is available!"