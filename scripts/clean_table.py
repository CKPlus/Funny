import sys
sys.path.append("../")

from my_sites import db_session
from my_sites.tikann.models import Article,Image

Image.query.delete()
Article.query.delete()

db_session.commit()

print " Clean table success! "
