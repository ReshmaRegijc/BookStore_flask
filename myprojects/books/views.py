from flask import Blueprint, render_template,redirect,url_for


from myprojects import db
from myprojects.models import Book

from myprojects.books.forms import *


book_blueprint = Blueprint('books',__name__,template_folder= 'templates/books')

@book_blueprint.route('/add', methods=['GET','POST'])
def add():

    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        author = form.author.data
        price = form.price.data

        new_book = Book(name,author,price)

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('books.list'))
    
    return render_template('add.html',form=form)

@book_blueprint.route('/delete', methods=['GET','POST'])
def delete():

    form = DeleteForm()

    if form.validate_on_submit():
        id = form.id.data

        buy_book = Book.query.getid(id)

        db.session.delete(buy_book)
        db.session.commit()

        return redirect(url_for('books.list'))

    return render_template('delete.html',form=form)


@book_blueprint.route('/list')
def list():
    books = Book.query.all()
    return render_template('list.html',books=books)


