from flask import Flask

from app.db.database import init_db
from app.routs.all_messages import messages_blueprint
from app.settings.admin import init_topics

app = Flask(__name__)

if __name__ == '__main__':
    init_db()
    init_topics()
    app.register_blueprint(messages_blueprint, url_prefix="/api")
    app.run()