from flask import Flask

from app.routs.all_messages import messages_blueprint

app = Flask(__name__)

if __name__ == '__main__':
    app.register_blueprint(messages_blueprint, url_prefix="/api")
    app.run()