#!usr/bin/env python
import os
from flask_script import Shell, Manager
from app.models import User, Role, Post, Permission, Comment
from app import db, create_app
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('PIXIE_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post, Permission=Permission, Comment=Comment)


manager.add_command('shell', Shell(make_context=make_shell_context))

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit test"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
