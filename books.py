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
            return jsonify(f"Below are the books present in our library, {books_list}")
        else:
            return jsonify({"error": "No books found"})

    if request.method == 'POST':
        data = request.get_json()
        if data == None or 'author' not in data or 'title' not in data or 'language' not in data:
            return jsonify({"error": "Invalid input"})

        iD = 0
        if len(books_list) > 0:
            iD = books_list[-1]['id'] + 1

        new_obj = {
            'id': iD,
            'author': data['author'],
            'language': data['language'],
            'title': data['title']
        }

        books_list.append(new_obj)
        return jsonify(f"New book added!, {new_obj}")

@books.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(f"Here is the book you requested, {book}")
        return jsonify({"error": "Book not found"})

    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                data = request.get_json()
                if data == None or 'author' not in data or 'title' not in data or 'language' not in data:
                    return jsonify({"error": "Invalid input"})

                book['author'] = data['author']
                book['language'] = data['language']
                book['title'] = data['title']
                return jsonify(book)
        return jsonify({"error": "Book not found"})

    if request.method == 'DELETE':
        for index, book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify({"message": "Book deleted successfully"})
        return jsonify({"error": "Book not found"})