from header import *
from classes.clsUser import *
from classes.clsProduct import *
from classes.using_cookie import *
from classes.using_session import *
from classes.clsCategory import *


@app.route('/home')
def hello_world():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template("admin_panel/index.html", title='Dashboard')


app.add_url_rule("/", view_func=clsUser.login, methods=['GET'])
app.add_url_rule("/login_get", view_func=clsUser.login, methods=['GET'])
app.add_url_rule("/login_post", view_func=clsUser.login_post, methods=['POST'])
app.add_url_rule("/signout", view_func=clsUser.logout)

app.add_url_rule("/admin/user", view_func=clsUser.user_management)
app.add_url_rule("/admin/user-dashboard", view_func=clsUser.user_dashboard)

app.add_url_rule("/admin/product", view_func=clsProduct.product_management)
app.add_url_rule("/admin/product-dashboard", view_func=clsProduct.product_dashboard)

app.add_url_rule("/admin/product", view_func=clsProduct.product_management)
app.add_url_rule("/admin/product-dashboard", view_func=clsProduct.product_dashboard)
app.add_url_rule("/admin/insert-product", view_func=clsProduct.insert_product, methods=['POST'])
app.add_url_rule("/admin/edit-product/<int:product_id>", view_func=clsProduct.edit_product, methods=['GET'])
app.add_url_rule("/admin/update-product", view_func=clsProduct.update_product, methods=['POST'])
app.add_url_rule("/admin/delete-product/<int:product_id>", view_func=clsProduct.delete_product)

app.add_url_rule("/admin/category", view_func=clsCategory.category_management)
app.add_url_rule("/admin/category-dashboard", view_func=clsCategory.category_dashboard)
app.add_url_rule("/admin/insert-category", view_func=clsCategory.insert_category, methods=['POST'])
app.add_url_rule("/admin/update-category/<int:category_id>", view_func=clsCategory.update_category)
app.add_url_rule("/admin/delete-category", view_func=clsCategory.delete_category)

# app.add_url_rule("/set_cookie/<value>", view_func=using_cookie.set_cookies(value))
app.add_url_rule("/get_cookie", view_func=using_cookie.get_cookies)
app.add_url_rule("/del_cookie", view_func=using_cookie.del_cookie)

# app.add_url_rule("/set_session/<value>", view_func=using_session.set_session(value))
app.add_url_rule("/get_session", view_func=using_session.get_session)
app.add_url_rule("/del_session", view_func=using_session.del_session)

if __name__ == '__main__':
    app.run()
