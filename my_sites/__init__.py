from flask import Flask

app = Flask(__name__)


from my_sites.tikann import tikann_app
app.register_blueprint(tikann_app, url_prefix="/tikann")



from my_sites.tikann.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()