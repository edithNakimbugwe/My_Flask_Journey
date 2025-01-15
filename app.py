#imports
# from flask import Flask, render_template
# from flask_scss import Scss
# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request,jsonify

#my app
app = Flask(__name__)

books_list = [
    {
        "id":0,
        "author": "Edith N",
        "title": "The Beginning"
    },
    # {
    #     "id":1,
    #     "author": "Shanitah D"
    #     "title": "Things Fall Apart"
    # },
    {
        "id":2,
        "author": "Edith N",
        "title": "The Beginning"
    },
    {
        "id":3,
        "author": "Edith N",
        "title": "The Beginning"
    },
    {
        "id":4,
        "author": "Edith N",
        "title": "The Beginning"
    },
    {
        "id":5,
        "author": "Edith N",
        "title": "The End"
    },

]

@app.route('/books', methods=['GET','POST'])
def books():
    if request.method == 'GET':
        if len(books_list)>0:
            return jsonify(books_list)
        else:
            "Nothing Found",404

    if request.method =='POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'author':new_author,
            'language':new_lang,
            'title':new_title
        }

        books_list.append(new_obj)
        return jsonify(books_list), 201

# @app.route("/")
# def index():
#     return "Welcome"

# @app.route("/<name>")
# def print_name(name):
#     return "Welcome, {}".format(
#         name
#     )

# @app.route("/<name>/<position>")
# def print_position(name, position):
#     return "Dear {},".format(position)

if __name__ in "__main__":
    app.run(debug=True)