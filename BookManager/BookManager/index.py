from flask import session
from BookManager import app, dao, admin, login, utils, controllers


app.add_url_rule("/",'index',controllers.index)
app.add_url_rule('/book/<int:book_id>', 'book-detail', controllers.details)
app.add_url_rule('/login-admin', 'login-admin', controllers.login_admin, methods=['post'])
app.add_url_rule('/login', 'login-user', controllers.login_my_user, methods=['get', 'post'])
app.add_url_rule('/logout', 'logout', controllers.logout_my_user)
app.add_url_rule('/register', 'register', controllers.register, methods=['get', 'post'])
app.add_url_rule('/cart', 'cart', controllers.cart)
app.add_url_rule('/api/cart', 'add-cart', controllers.add_to_cart, methods=['post'])
app.add_url_rule('/api/cart/<book_id>', 'update-cart', controllers.update_cart, methods=['put'])
app.add_url_rule('/api/cart/<book_id>', 'delete-cart', controllers.delete_cart, methods=['delete'])
app.add_url_rule('/api/pay', 'pay', controllers.pay)
app.add_url_rule('/bill', 'bill', controllers.bill)
app.add_url_rule('/api/book/<int:book_id>/comments', 'comment-list', controllers.comments)
app.add_url_rule('/api/book/<int:book_id>/comments', 'comment-add', controllers.add_commment, methods=['post'])


@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


@app.context_processor
def common_attribute():
    categories = dao.load_categories()
    return {'categories': categories,
            'cart': utils.cart_stats(session.get(app.config['CART_KEY']))
            }


if __name__ == '__main__':
    app.run(debug=True)
