from flask import Flask

from app.services.consumer import consume_emails_by_topic

app = Flask(__name__)


if __name__ == '__main__':
    consume_emails_by_topic('messages.all')
    app.run()