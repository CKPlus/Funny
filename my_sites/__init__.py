from flask import Flask
from flask.ext.admin import Admin, BaseView, expose



app = Flask(__name__)

admin = Admin(name='Tikann')
class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')
admin.add_view(MyView(name='Hello'))
admin.init_app(app)


from my_sites.tikann import tikann_app
app.register_blueprint(tikann_app, url_prefix="/tikann")



from my_sites.tikann.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()