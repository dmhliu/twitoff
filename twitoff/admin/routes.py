from flask import Blueprint, current_app, render_template
from twitoff.models import DB, add_test_users

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
def admin_index():
    return render_template('admin.html')

@admin.route('/add_test_users')
def setup_test_users():
    DB.drop_all()
    DB.create_all()  # initial setup
    add_test_users()
    return 'test users added'

