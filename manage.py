#!/usr/bin/env python
import os
from app import create_app, db
from app.auth.models import User, Role, Datastore, users_roles

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role \
            Datastore=Datastore)

manager.add_command('shell', Shell(make_context=make_shell_context))

@manager.command
def deploy(nick='admin', email='admin@app.de'):
    db.create_all()
    # create a superuser
    import getpass
    password = getpass.getpass()
    u = User(nick=nick, email=email, password=password, \
            '''role=admin''')
    db.session.add(u)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
