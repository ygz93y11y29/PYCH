


#������
CSRF_ENABLED = True     #���� ��վ������α�� ����
SECRET_KEY = 'you-will-never-guess'     #����һ�����ܵ�����


OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


#SQLALCHEMY���ݿ�����
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.2.8:3306/ods'  #���ݿ���Ϣ
SQLALCHEMY_TRACK_MODIFICATIONS = True


# ͨ�������ʼ����ʹ�������
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None
# administrator list
ADMINS = ['2211866596@qq.com']
