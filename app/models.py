# project/models.py


from app import db


class Task(db.Model):
    import datetime
    
    __tablename__ = "tasks"
    
    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    status = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__( self, name, due_date, priority, posted_date, status, user_id ):
        self.name = name
        self.due_date = due_date
        self.priority = priority
        self.posted_date = posted_date
        self.status = status
        self.user_id = user_id
    
    def __repr__( self ):
        return '<name %r>' % self.name


class Search(db.Model):
    import datetime
    
    __tablename__ = 'searches'
    
    search_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    source = db.Column(db.String, nullable=False)
    data = db.Column(db.Text, nullable=False)
    posted_date = db.Column(db.Date, default=datetime.datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def __init__( self, name, source, data, posted_date, user_id ):
        self.name = name
        self.source = source
        self.data = data
        self.posted_date = posted_date
        self.user_id = user_id
    
    def __repr__( self ):
        return '<name %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    tasks = db.relationship('Task', backref='poster')
    searches = db.relationship('Search', backref='poster')
    role = db.Column(db.String, default='user')
    
    def __init__( self, name=None, email=None, password=None, role=None ):
        self.username = name
        self.email = email
        self.password = password
        self.role = role
    
    def __repr__( self ):
        return '<User %r>' % self.usernamename
