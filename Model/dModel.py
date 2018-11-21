import time,os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class PictureDate(db.Model):
    __tablename__ = 'PictureDate'
    Id = db.Column(db.Integer, primary_key=True)
    Uuid = db.Column(db.String(64), unique=True)
    Title = db.Column(db.String(64))
    Description = db.Column(db.String(128))

    def __init__(self
                 , Uuid
                 , Title
                 , Description
                 ):
        self.Uuid = Uuid
        self.Title = Title
        self.Description = Description

class GoogleDrive_callputjpg(db.Model):
    __tablename__ = 'CallPutJPG'
    Id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25))
    title1 = db.Column(db.String(86))
    modifiedDate = db.Column(db.String(26))
    
    def __init__(self
                 , title
                 , title1
                 , modifiedDate
    #             , Remark
                 ):
        self.title = title
        self.title1 = title1
        self.modifiedDate = modifiedDate

class BulkInsertTest():
    def __init__(self,db):
        self.db = db

    """Batched INSERT statements via the ORM in "bulk", discarding PKs."""
    def test_bulk_save(self,list_folderfiles):
        
        self.db.session.bulk_save_objects([
                GoogleDrive_callputjpg(
                title=dic_files['title'],
                title1=dic_files['title1'],
                modifiedDate=dic_files['modifiedDate']
                )
                for dic_files in list_folderfiles
        ])        
        

    """Batched INSERT statements via the ORM "bulk", using dictionaries."""
    def test_bulk_insert_mappings(self,list_folderfiles):

        self.db.session.bulk_insert_mappings(GoogleDrive_callputjpg, [
                    dic_files
                    for dic_files in list_folderfiles 
        ])        

if __name__ == '__main__':
    manager.run()