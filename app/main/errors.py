from flask import render_template
from . import main


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')

@main.errorhandler(403)
def forbidden(e):
    return render_template('403.html')
