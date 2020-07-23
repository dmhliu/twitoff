from flask import Blueprint, current_app, render_template
from twitoff.models import DB, add_test_users
from ..twitter import update_all_users

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def admin_index():
    return render_template('admin.html')

@admin.route('/add_test_users')
def setup_test_users():
    DB.drop_all()
    DB.create_all()  # initial setup
    add_test_users()
    return render_template('admin.html', message='test users added')
@admin.route('/update_all')
def update_all():
    m = "All users updated successfully"
    try:
        update_all_users()
    except:
        m="there was a problem updating users!"
    return render_template('admin.html', message=m)
