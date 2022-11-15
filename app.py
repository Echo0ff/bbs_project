from flask import Flask
from exts import db
import config
from flask_migrate import Migrate
from models import auth

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/index/<int:id>')
def index(id):
    return f'hello World1{id}'


if __name__ == '__main__':
    app.run()
