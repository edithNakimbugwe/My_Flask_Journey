from flask import Blueprint

admin_page = Blueprint(
    "admin", __name__, static_folder= "static", template_folder="templates"
)

@admin_page.route("/admin")
def admin1():
    return '<h1>Hello! Welcome to this page1</h1>'


@admin_page.route("/admin/1")
def admin2():
    return '<h1>Hello! Welcome to this page2</h1>'

@admin_page.route("/admin/2")
def admin3():
    return '<h1>Hello! Welcome to this page3</h1>'

@admin_page.route("/admin/3")
def admin4():
    return '<h1>Hello! Welcome to this page4</h1>' 