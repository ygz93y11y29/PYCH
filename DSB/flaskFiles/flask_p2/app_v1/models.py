# -*- coding:utf-8 -*-
from app_v1 import db
from sqlalchemy import or_, not_




class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship('Post', backref='users', lazy='dynamic')

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)


posts_tags = db.Table('posts_tags',
                      db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
                      db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

class Post(db.Model):
    """Represents Proected posts."""

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # Set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    # Establish contact with Comment's ForeignKey: post_id
    comments = db.relationship('Comment',backref='posts',lazy='dynamic')
    # many to many: posts <==> tags
    tags = db.relationship('Tag',secondary=posts_tags,backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)


class Comment(db.Model):
    """Represents Proected comments."""

    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.name)

class Tag(db.Model):
    """Represents Proected tags."""

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    add = db.Column(db.String(255))
    add1 = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)


class db_addDeleteUpdateSelect():
    def read_one_select(self, User):
        #1  返回表中的第一条记录
        user = User.query.first()

        #2      返回表中指定主键的一条记录
        user = User.query.get('49f86ede-f1e5-410e-b564-27a97e12560c')

        #3     返回符合过滤条件的第一条记录
        user = db.session.query(User).filter_by(id='49f86ede-f1e5-410e-b564-27a97e12560c').first()

    def read_more_select(self, User):
        #1      获取多条记录
        user = db.session.query(User).filter_by(username='fanguiju').all()

        #2      获取全部数据
        users = User.query.all()

        users = db.session.query(User).all()

        users = db.session.query(User).limit(10).all()

        users = db.session.query(User).order_by(User.username).all()

        users = db.session.query(User).order_by(User.username.desc()).all()

        users = db.session.query(User).order_by(User.username).limit(10).all()

    def pagination_select(self):
        '''
            分页
        :return:
        '''
        #第一个参数表示查询返回第几页的内容
        #第二个参数表示每页显示的对象数量
        user_page = user_page = User.query.paginate(1, 10)

        #获取这一页所包含的数据对象
        print(user_page.items)

        #获取这一页的页码
        print(user_page.page)

        #获取总共的页数
        print(user_page.pages)

        # 是否有上一页
        print(user_page.has_prev)
        #False

        # 如果有上一页的话, 获取上一页的 pagination 对象
        if user_page.has_prev:
            print(user_page.prev())

        # 是否有下一页
        print(user_page.has_next)

        # 如果有下一页的话, 获取下一个的 pagination 对象
        if user_page.has_next:
            user_page.next()

    def filter_select(self):
        '''
            SQLAlchemy 提供了过滤器 query.filter_by() 和 query.filter(),
            字段键值对, EG. username='fanguiju'
            比较表达式, EG. User.id > 100
            逻辑函数, EG. in_/not_/or_
        :return:
        '''

        user = db.session.query(User).filter(User.username.in_(['fanguiju', 'jmilkfan'])).limit(1).all()  # 当然也可以结合链式函数来使用

        user = db.session.query(User).filter(not_(User.password == None)).all()

        user = db.session.query(User).filter(or_(not_(User.username == None), User.password != None)).all()


    def Update_(self):
        '''
            Update 更新数据
                注意: 更新的内容必须是 Dict 数据类型.
                需要注意的是: 就如使用原生 SQL 指令来更新记录一样, 如果没有指定要更新具体的哪一条记录的话, 会将该字段所在
                列的所有记录值一同更新, 所以切记使用过滤条件来定位到具体需要更新的记录.
        :return:
        '''
        user = db.session.query(User).first()

        user = db.session.query(User).update({'username': 'update_fanguiju'})
        db.session.commit()

        user = db.session.query(User).first()


    def Delete_(self):
        '''
            Delete 删除数据
        :return:
        '''
        user = db.session.query(User).first()
        db.session.delete(user)
        db.session.commit()


    def add_(self):
        from uuid import uuid4
        user = User(id=str(uuid4()), username='jmilkfan', password='fanguiju')
        db.session.add(user)
        db.session.commit()


    def join(self):
        '''
            关联查询
        :return:
        '''
        #第一个是其它的表，我们的 followers 表。第二参数就是连接的条件。
        return Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id).order_by(Post.timestamp.desc())


class db_relationship():

    def one_to_many(self):
        '''
            db.relationsformat(self.username)hip： 会在 SQLAlchemy 中创建一个虚拟的列，
               该列会与 Post.user_id (db.ForeignKey) 建立联系。这一切都交由 SQLAlchemy 自身管理。
            backref：用于指定表之间的双向关系，如果在一对多的关系中建立双向的关系，这样的话在对方看来这就是一个多对一的关系
            lazy：指定 SQLAlchemy 加载关联对象的方式。
                lazy=subquery: 会在加载 Post 对象后，将与 Post 相关联的对象全部加载，这样就可以减少 Query 的动作，也就是减少了
                    对 DB 的 I/O 操作。但可能会返回大量不被使用的数据，会影响效率。
                lazy=dynamic: 只有被使用时，对象才会被加载，并且返回式会进行过滤，如果现在或将来需要返回的数据量很大，
                    建议使用这种方式。Post 就属于这种对象。
        :return:        Query 对象
        '''
        posts = db.relationship('Post',backref='users',lazy='dynamic')

        #list = user.posts.all()

    def many_to_many(self):
        '''
            多对多关系会在两个类之间增加一个关联表。 这个关联的表在 relationship() 方法中通过 secondary 参数来表示。
                所以这个 ForeignKey 指令会使用链接来定位到远程的表：

            many to many 的关系仍然是由 db.relationship() 来定义
            seconddary(次级)：会告知 SQLAlchemy 该 many to many 的关联保存在 posts_tags 表中
            backref：声明表之间的关系是双向，帮助手册 help(db.backref)。需要注意的是：在 one to many 中的 backref
                是一个普通的对象，而在 many to many 中的 backref 是一个 List 对象

            NOTE 1：实际上 db.Table 对象对数据库的操作比 db.Model 更底层一些。后者是基于前者来提供的一种对象化包装，
                表示数据库中的一条记录。 posts_tags 表对象之所以使用 db.Table 不使用 db.Model 来定义，是因为我们不需要对
                 posts_tags (self.name)进行直接的操作(不需要对象化)，posts_tags 代表了两张表之间的关联，会由数据库自身来
                 进行处理。
            NOTE 2： posts_tags 的声明定义最好在 Post 和 Tag 之前。
            NOTE 3: 没添加一个 models class 都要记得在 manage.py 中导入并返回，方便之后的调试，这里就不作重复了。
        :return:
        '''

        followed = db.relationship('User',
                                   secondary=followers,
                                   primaryjoin=(followers.c.follower_id == id),
                                   secondaryjoin=(followers.c.followed_id == id),
                                   backref=db.backref('followers', lazy='dynamic'),
                                   lazy='dynamic')

        '''
        User’ 是这种关系中的右边的表(实体)(左边的表/实体是父类)。因为定义一个自我指向的关系，我们在两边使用同样的类。
        secondary 指明了用于这种关系的辅助表。
        primaryjoin 表示辅助表中连接左边实体(发起关注的用户)的条件。注意因为 followers 表不是一个模式，获得字段名的语法有些怪异。
        secondaryjoin 表示辅助表中连接右边实体(被关注的用户)的条件。
        backref 定义这种关系将如何从右边实体进行访问。当我们做出一个名为 followed 的查询的时候，将会返回所有跟左边实体联系的右边的用户。当我们做出一个名为 followers 的查询的时候，将会返回一个所有跟右边联系的左边的用户。lazy 指明了查询的模式。dynamic 模式表示直到有特定的请求才会运行查询，这是对性能有很好的考虑。
        lazy 是与 backref 中的同样名称的参数作用是类似的，但是这个是应用于常规查询。
        '''

