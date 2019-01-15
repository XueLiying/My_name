
from flask import Flask

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# 导入flask-sqlalchemy扩展
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# sqlalchemy数据库实例
db = SQLAlchemy(app)
# 实例化管理器对象
manage = Manager(app)
# 使用迁移框架
Migrate(app, db)
# 通过管理器对象，添加迁移命令
manage.add_command("db", MigrateCommand)


@app.route("/")
def index():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)


