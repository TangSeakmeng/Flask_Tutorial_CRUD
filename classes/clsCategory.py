from header import *
from classes.clsDbConnection import *


class clsCategory:
    sql = ""

    # @app.route("/admin/category-management")
    @staticmethod
    def category_management():
        if 'username' not in session:
            return redirect(url_for('login'))
        return render_template("admin_panel/category_management.html", title='Category Management')

    # @app.route("/admin/category-dashboard")
    @staticmethod
    def category_dashboard():
        if 'username' not in session:
            return redirect(url_for('login'))

        category_list = [
            # {
            #     'id': 1,
            #     'name': 'Computer'
            # },
            # {
            #     'id': 2,
            #     'name': 'Phone',
            # },
            # {
            #     'id': 3,
            #     'name': 'Tablet',
            # },
            # {
            #     'id': 4,
            #     'name': 'Desktop',
            # }
        ]

        cmd = clsDbConnection.con.cursor()
        clsCategory.sql = "select id, categoryname from tblcategory order by id"
        cmd.execute(clsCategory.sql)
        category_list = cmd.fetchall()

        return render_template("admin_panel/category_dashboard.html", title='Category Dashboard',
                               category_list=category_list)

    @staticmethod
    def insert_category():
        name = request.form['txtName']

        cmd = clsDbConnection.con.cursor()
        cmd.execute(f"insert into tblcategory(categoryname) values('{name}')")
        clsDbConnection.con.commit()

        return redirect(url_for('category_dashboard'))

    @staticmethod
    def update_category(category_id):
        return category_id

    @staticmethod
    def delete_category():
        pass