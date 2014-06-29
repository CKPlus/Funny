from flask import Blueprint

tikann_app = Blueprint('tikann', __name__)

import views.views
import database