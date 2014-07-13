from flask import Flask
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.sqlalchemy import SQLAlchemy




app = Flask(__name__)
# db = SQLAlchemy(app)



from my_sites.tikann import tikann_app
app.register_blueprint(tikann_app, url_prefix="/tikann")



#Admin Initial
from my_sites.tikann.database import db_session
from my_sites.tikann.models import User, Article, Image
admin = Admin(name='Tikann')
admin.add_view(ModelView(User, db_session))
admin.add_view(ModelView(Article, db_session))
admin.add_view(ModelView(Image, db_session))
admin.init_app(app)




@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()