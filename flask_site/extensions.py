from flask import session
from flask_admin import Admin, AdminIndexView
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


# class from flask-admin AdminIndexView
# class AdminIndexView(BaseView):
#     """
#         Default administrative interface index page when visiting the ``/admin/`` URL.
#
#         It can be overridden by passing your own view class to the ``Admin`` constructor::
#
#             class MyHomeView(AdminIndexView):
#                 @expose('/')
#                 def index(self):
#                     arg1 = 'Hello'
#                     return self.render('admin/myhome.html', arg1=arg1)
#
#             admin = Admin(index_view=MyHomeView())
#
#
#         Also, you can change the root url from /admin to / with the following::
#
#             admin = Admin(
#                 app,
#                 index_view=AdminIndexView(
#                     name='Home',
#                     template='admin/myhome.html',
#                     url='/'
#                 )
#             )
#
#         Default values for the index page are:
#
#         * If a name is not provided, 'Home' will be used.
#         * If an endpoint is not provided, will default to ``admin``
#         * Default URL route is ``/admin``.
#         * Automatically associates with static folder.
#         * Default template is ``admin/index.html``
#     """
#
#     def __init__(self, name=None, category=None,
#                  endpoint=None, url=None,
#                  template='admin/index.html',
#                  menu_class_name=None,
#                  menu_icon_type=None,
#                  menu_icon_value=None):
#         super(AdminIndexView, self).__init__(name or babel.lazy_gettext('Home'),
#                                              category,
#                                              endpoint or 'admin',
#                                              '/admin' if url is None else url,
#                                              'static',
#                                              menu_class_name=menu_class_name,
#                                              menu_icon_type=menu_icon_type,
#                                              menu_icon_value=menu_icon_value)
#         self._template = template
#
#     @expose()
#     def index(self):
#         return self.render(self._template)


class MyAdminView(AdminIndexView):
    def is_accessible(self):
        return session.get('is_logged')


db = SQLAlchemy()
admin = Admin(index_view=MyAdminView())
login_manager = LoginManager()
toolbar = DebugToolbarExtension()
