# -*- coding:utf-8 -*-
from app_v1 import db

followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    __tablename__ = 'ods_p1_User'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    #db.relationship 字段。这并不是一个实际的数据库字段，因此是不会出现在上面的图中。对于一个一对多的关系，db.relationship 字段通常是定义在“一”这一边。在这种关系下
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    followed = db.relationship('User', secondary=followers, primaryjoin=(followers.c.follower_id == id),
                               secondaryjoin=(followers.c.followed_id == id),
                               backref=db.backref('followers', lazy='dynamic'),
                               lazy='dynamic')

    @property
    def is_authenticated(self):
        #is_authenticated 方法有一个具有迷惑性的名称。一般而言，这个方法应该只返回 True，除非表示用户的对象因为某些原因不允许被认证。
        return True

    @property
    def is_active(self):
        #is_active 方法应该返回 True，除非是用户是无效的，比如因为他们的账号是被禁止。
        return True

    @property
    def is_anonymous(self):
        #is_anonymous 方法应该返回 True，如果是匿名的用户不允许登录系统。
        return False

    def get_id(self):
        #get_id 方法应该返回一个用户唯一的标识符
        return str(self.id)

    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def __repr__(self): #__repr__ 方法告诉 Python 如何打印这个类的对象。我们将用它来调试。
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    __tablename__ = 'ods_p1_Post'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('ods_p1_User.id'))



    def __repr__(self): #__repr__ 方法告诉 Python 如何打印这个类的对象。我们将用它来调试。
        return '<Post %r>' % (self.body)


