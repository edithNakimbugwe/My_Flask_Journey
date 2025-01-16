from flask import Blueprint, jsonify, request

books = Blueprint("books", __name__)

books_list = [
    {"id": 0, "author": "Edith N", "title": "The Beginning"},
    {"id": 1, "author": "Shanitah N", "title": "The Rain"},
    {"id": 2, "author": "Maria N", "title": "The Tears"},
    {"id": 3, "author": "Eva N", "title": "The Renewal"},
    {"id": 4, "author": "Edithiana N", "title": "The End"},
]

@books.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            return jsonify({"error": "No books found"}), 404

    if request.method == 'POST':
        data = request.get_json()
        if not data or 'author' not in data or 'title' not in data or 'language' not in data:
            return jsonify({"error": "Invalid input"}), 400

        iD = books_list[-1]['id'] + 1 if books_list else 0
        new_obj = {
            'id': iD,
            'author': data['author'],
            'language': data['language'],
            'title': data['title']
        }

        books_list.append(new_obj)
        return jsonify(new_obj), 201

@books.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
        return jsonify({"error": "Book not found"}), 404

    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                data = request.get_json()
                if not data or 'author' not in data or 'title' not in data or 'language' not in data:
                    return jsonify({"error": "Invalid input"}), 400

                book['author'] = data['author']
                book['language'] = data['language']
                book['title'] = data['title']
                return jsonify(book)
        return jsonify({"error": "Book not found"}), 404

    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify({"message": "Book deleted successfully"})
        return jsonify({"error": "Book not found"}), 404
