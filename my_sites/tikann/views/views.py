from my_sites import app
from my_sites.tikann import tikann_app


@tikann_app.route('/')
def index():
	return 'Hello World!'