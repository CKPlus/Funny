# -*- coding: utf-8 -*-  

from my_sites import app
from my_sites.tikann import tikann_app

from flask import render_template

from my_sites.tikann.models import Article

@tikann_app.route('/')
def index():
	articles = Article.query.all()
	return render_template('index.html', articles=articles)