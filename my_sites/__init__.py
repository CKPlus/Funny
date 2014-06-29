from flask import Flask

app = Flask(__name__)


from my_sites.tikann import tikann_app
app.register_blueprint(tikann_app, url_prefix="/tikann")

