from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, utils
from app import db, app


users_roles = db.Table('users_roles',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    description = db.Column(db.String(512), nullable=False)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    nick = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    active = db.Column(db.Boolean(), nullable=False)
    #TODO: explain/change lazy arg
    roles = db.relationship('Role', secondary='users_roles', backref=db.backref('users', lazy='dynamic'))

    def has_passw(self, pwPlain):
        return utils.verify_password(pwPlain, self.password)


class Datastore(SQLAlchemyUserDatastore):

    def create_user(self,nick,email,pwPlain):
        """ a more specific creation method for users,
            also handles password encryption.
        """ 
        pwEnc = utils.encrypt_password(pwPlain)
        super(Datastore,self).create_user(nick=nick,email=email,password=pwEnc,active=False)


# Store and Security setup
user_datastore = Datastore(db, User, Role)
security = Security(app, user_datastore)
