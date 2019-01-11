# coding:utf-8

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def index():
#     return "Hello Flask"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask
# from flask import json
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def get():
#     return "Hello Flask"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask

app = Flask(__name__)


@app.route("/")
def get():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)


