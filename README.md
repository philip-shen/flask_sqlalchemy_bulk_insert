# flask_sqlalchemy_bulk_insert
Performance test of bulk insert that inserts multiple rows from Google Drive by flask sqlalchemy

## Usage
Step 1.Update your individual Google Driver Credentials.
Step 2.Make sure Environment Configuration done.
Step 3.Edit content of config.ini.
Step 4.Follow DB Operation procedure.

## DB Operation
Step 1.

``` 
(Flask_trial) d:\project\Python\flask_sqlalchemy_bulk_insert>python .\Model\dModel.py db init
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
Creating directory d:\project\Python\flask_sqlalchemy_bulk_insert\migrations ... done
Creating directory d:\project\Python\flask_sqlalchemy_bulk_insert\migrations\versions ... done
Generating d:\project\Python\flask_sqlalchemy_bulk_insert\migrations\alembic.ini ... done
Generating d:\project\Python\flask_sqlalchemy_bulk_insert\migrations\env.py ... done
Generating d:\project\Python\flask_sqlalchemy_bulk_insert\migrations\README ... done
Generating d:\project\Python\flask_sqlalchemy_bulk_insert\migrations\script.py.mako ... done
Please edit configuration/connection/logging settings in 'd:\\project\\Python\\flask_sqlalchemy_bulk_insert\\migrations\\alembic.ini' before proceeding.

Step 2.

``` 
(Flask_trial) d:\project\Python\flask_sqlalchemy_bulk_insert>python .\Model\dModel.py db migrate
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'CallPutJPG'
INFO  [alembic.autogenerate.compare] Detected added table 'PictureDate'
Generating d:\project\Python\flask_sqlalchemy_bulk_insert\migrations\versions\42e75d1962fb_.py ... done

Step 3.

``` 
(Flask_trial) d:\project\Python\flask_sqlalchemy_bulk_insert>python .\Model\dModel.py db upgrade
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 42e75d1962fb, empty message

Step 4.

``` 
(Flask_trial) d:\project\Python\flask_sqlalchemy_bulk_insert>python app.py
d:\project\Python\flask_sqlalchemy_bulk_insert\Model
C:\Users\SCS\Envs\Flask_trial\lib\site-packages\flask_sqlalchemy\__init__.py:794: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
Google Authentication Started
Google Authentication Completed!
Get data from Google Drive duration: 13.02 seconds
Insert 1038 rows into table.
SA ORM Bulk insert, discarding PKs- total time: 0.11 seconds
Insert 1038 rows into table.
SA ORM Bulk insert, using dictionaries- total time: 0.05 seconds
DONE

## Environment Configuration
* Python 3.4.3
* Refer requirements.txt to pip necessary modules.

## Reference 
* [Flask-Migrate-Tutorial 透過 Flask-Migrate-Tutorial 管理資料庫 (database)](https://github.com/twtrubiks/Flask-Migrate-Tutorial)
* [Source code for examples.performance.bulk_inserts](https://docs.sqlalchemy.org/en/latest/_modules/examples/performance/bulk_inserts.html) 
* [Optimize Inserts Using SQLAlchemy](http://www.devx.com/dbzone/optimize-inserts-using-sqlalchemy.html)
* [Flask-Migrate sqlite 惹的麻煩](https://blog.burn-i.com/20180418/flask-migrate/)    

## License
MIT license