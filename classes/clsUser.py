from header import *


class clsUser:
    # @app.route("/login", methods=['GET'])
    @staticmethod
    def login():
        if 'username' in session:
            return render_template("./admin_panel/index.html", title='Dashboard', username=session.get("username"))
        return render_template("login.html", message="")

    # @app.route("/login", methods=['POST'])
    @staticmethod
    def login_post():
        username = request.form["txtUsername"]
        password = request.form["txtPassword"]
        if username == "admin" and password == "Sea03107778":
            session['username'] = username
            return render_template("./admin_panel/index.html", title='Dashboard', username=session.get("username"))
        else:
            message = "Please Login again!"
            return render_template("login.html", message=message)

    # app.add_url_rule("/", "login", login)

    # @app.route("/signout")
    @staticmethod
    def logout():
        session.pop('username', None)
        return render_template("login.html")

    # @app.route("/admin/user")
    @staticmethod
    def user_management():
        if 'username' not in session:
            return redirect(url_for('login'))
        return render_template("admin_panel/user_management.html", title='User Management')

    # @app.route("/admin/user-dashboard")
    @staticmethod
    def user_dashboard():
        user_list = [
            {
                'id': 1,
                'username': 'Bill Gates',
                'dateofbirth': '12/12/1950',
                'description': 'The Richest Man in the world',
                'phone': '12344567',
                'position': 'Software Developer',
                'password': '456123456',
                'salary': '200000$',
                'active': 'yes',
                'image': 'not found.jpg'
            },
            {
                'id': 2,
                'username': 'Jeff Bezos',
                'dateofbirth': '12/12/1940',
                'description': 'The Richest Man in the world',
                'phone': '12344567',
                'position': 'Software Engineer',
                'password': '456123456',
                'salary': '200000$',
                'active': 'yes',
                'image': 'not found.jpg'
            }
        ]

        if 'username' not in session:
            return redirect(url_for('login'))
        return render_template("admin_panel/user_dashboard.html", title='User Dashboard', user_list=user_list)