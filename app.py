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
    
# @app.route('/book/<int:id>', methods=['GET', 'PUT','DELETE'])
# def single_book(id):
#     if request.method == 'GET':
#         for book in books_list:
#             if book['id']==id:
#                 return jsonify(book)
#             pass
#         if request.method =='PUT':
#             for book in books_list:
#                 if book['id'] ==id:
#                     book['author']= request.form['author']
#                     book['language']= request.form['language']
#                     book['title']= request.form['title']
#                     updated_book = {
#                         'id':id,
#                         'author':book['author'],
#                         'language':book['language'],
#                         'title':book['title']
                    
#                     }
#                     return jsonify(updated_book)
#                 if request.method == 'DELETE':
#                     for index, book in enumerate(books_list):
#                         if book['id'] == id:
#                             books_list.pop(index)
#                             return jsonify(books_list)

@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        # Find
        book = next((book for book in books_list if book['id'] == id), None)
        if book:
            return jsonify(book), 200
        return jsonify({"error": "Book not found"}), 404

    elif request.method == 'PUT':
        # Update
        book = next((book for book in books_list if book['id'] == id), None)
        if book:
            try:
                book['author'] = request.form.get('author', book['author'])
                book['language'] = request.form.get('language', book['language'])
                book['title'] = request.form.get('title', book['title'])
                return jsonify(book), 200
            except KeyError as e:
                return jsonify({"error": f"Missing field: {e}"}), 400
        return jsonify({"error": "Book not found"}), 404

    elif request.method == 'DELETE':
        # Delete
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify({"message": "Book deleted", "books": books_list}), 200
        return jsonify({"error": "Book not found"}), 404


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