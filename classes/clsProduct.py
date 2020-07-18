import os
import secrets

from header import *
from classes.clsDbConnection import *


def getCategoryId(menuCategory):
    cmd = clsDbConnection.con.cursor()
    clsProduct.sql = f"select id from tblCategory where categoryname = '{menuCategory}'"
    cmd.execute(clsProduct.sql)
    result = cmd.fetchone()

    menuCategory = []

    for item in result:
        menuCategory.append(item)

    menuCategory_id = menuCategory[0]
    return menuCategory_id


class clsProduct:
    sql = ""

    # @app.route("/admin/product")
    @staticmethod
    def product_management():
        if 'username' not in session:
            return redirect(url_for('login'))

        cmd = clsDbConnection.con.cursor()
        clsProduct.sql = "select categoryname from tblcategory order by categoryname"
        cmd.execute(clsProduct.sql)
        category_list = cmd.fetchall()

        return render_template("admin_panel/product_management.html", title='Product Management', category_list=category_list)

    # @app.route("/admin/product-dashboard")
    @staticmethod
    def product_dashboard():
        if 'username' not in session:
            return redirect(url_for('login'))

        product_list = [
            # {
            #     'id': 1,
            #     'name': 'abc',
            #     'description': 'ice cream',
            #     'quantity': 1,
            #     'price': '2$',
            #     'image': 'not found.jpg'
            # },
            # {
            #     'id': 2,
            #     'name': 'dbc',
            #     'description': 'ice cream',
            #     'quantity': 1,
            #     'price': '2$',
            #     'image': 'not found.jpg'
            # }
        ]

        cmd = clsDbConnection.con.cursor()
        clsProduct.sql = "select tblproduct.id, name, description, categoryname, quantity, price, image from tblproduct inner join tblcategory on tblproduct.categoryid = tblcategory.id order by tblproduct.id"
        cmd.execute(clsProduct.sql)
        product_list = cmd.fetchall()

        return render_template("admin_panel/product_dashboard.html", title='Product Dashboard', product_list=product_list)

    @staticmethod
    def insert_product():
        try:
            name = request.form['txtName']
            description = request.form['txtDescription']
            category = request.form['selectCategory']
            quantity = request.form['txtQuantity']
            price = request.form['txtPrice']
            image = request.files['fileImage']

            random_hex = secrets.token_hex(8)
            f_name, f_ext = os.path.splitext(image.filename)
            picture_fn = random_hex + f_ext
            image.save(os.path.join("static/images/product_image", picture_fn))

            clsProduct.sql = f"insert into tblproduct(name, description, categoryid, quantity, price, image) values('{name}', '{description}', '{getCategoryId(category)}', {quantity}, {price}, '{picture_fn}')"

            cmd = clsDbConnection.con.cursor()
            cmd.execute(clsProduct.sql)
            clsDbConnection.con.commit()

            return redirect(url_for('product_dashboard'))
        except mysql.connector.errors as error:
            clsDbConnection.con.rollback()
            return "Error {}".format(error)
        except Exception as error:
            return "Error {}".format(error)
        finally:
            if clsDbConnection.con.is_connected():
                cmd.close()
                clsDbConnection.con.close

    @staticmethod
    def edit_product(product_id):
        cmd = clsDbConnection.con.cursor()
        cmd.execute(f"select tblproduct.id, name, description, tblcategory.categoryname, quantity, price "
                    f"from tblproduct inner join tblcategory on tblproduct.categoryid = tblcategory.id where tblproduct.id = {product_id}")
        result = cmd.fetchall()

        product = []

        for item in result:
            product.append(item[0])
            product.append(item[1])
            product.append(item[2])
            product.append(item[3])
            product.append(item[4])
            product.append(item[5])

        clsProduct.sql = "select categoryname from tblcategory order by categoryname"
        cmd.execute(clsProduct.sql)
        category_list = cmd.fetchall()

        return render_template("/admin_panel/product_management_update.html", title='Update Product', product=product, category_list=category_list)

    @staticmethod
    def update_product():
        try:
            productId = request.form['txtProductId']
            name = request.form['txtName']
            description = request.form['txtDescription']
            category = request.form['selectCategory']
            quantity = request.form['txtQuantity']
            price = request.form['txtPrice']
            image = request.files['fileImage']

            cmd = clsDbConnection.con.cursor()

            # exist
            if image:
                random_hex = secrets.token_hex(8)
                f_name, f_ext = os.path.splitext(image.filename)
                picture_fn = random_hex + f_ext
                image.save(os.path.join("static/images/product_image", picture_fn))

                clsProduct.sql = f"update tblproduct set name='{name}', description = '{description}', categoryid = '{getCategoryId(category)}', quantity='{quantity}', price='{price}', image='{picture_fn}' where id = '{productId}';"

            # not exist
            else:
                clsProduct.sql = f"update tblproduct set name='{name}', description = '{description}', categoryid = '{getCategoryId(category)}', quantity='{quantity}', price='{price}' where id = '{productId}'"

            print(clsProduct.sql)

            cmd.execute(clsProduct.sql)
            clsDbConnection.con.commit()

            return redirect(url_for('product_dashboard'))
        except mysql.connector.errors as error:
            clsDbConnection.con.rollback()
            return "Error {}".format(error)
        except Exception as error:
            return "Error {}".format(error)
        finally:
            if clsDbConnection.con.is_connected():
                cmd.close()
                clsDbConnection.con.close

    @staticmethod
    def delete_product(product_id):
        try:
            cmd = clsDbConnection.con.cursor()
            cmd.execute(f"delete from tblproduct where id = '{product_id}'")
            clsDbConnection.con.commit()

            return redirect(url_for('product_dashboard'))
        except mysql.connector.errors as error:
            clsDbConnection.con.rollback()
            return "Error {}".format(error)
        finally:
            if clsDbConnection.con.is_connected():
                cmd.close()
                clsDbConnection.con.close
