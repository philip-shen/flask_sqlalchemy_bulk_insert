#2018/11/22 Initial
#################################################################
from Model.dModel import *
from Model.googleDrive import  *
from Model.readConfig import *
import time,uuid
from pydrive.drive import GoogleDrive

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

start = time.time()

strabspath=os.path.abspath(__file__)
strdirname=os.path.dirname(strabspath)

str_candlestick_filepath = ''#
localgoogle_drive = GoogleCloudDrive(str_candlestick_filepath)

configPath=os.path.join(strdirname,"config.ini")
localReadConfig = ReadConfig(configPath)
str_client_credentials = localReadConfig.get_flask_sqlalchemy_setting('client_credentials')
gauth = localgoogle_drive.GDriveAuth(str_client_credentials)
drive = GoogleDrive(gauth)

parent_id = localReadConfig.get_flask_sqlalchemy_setting('parent_id_folder')
list_foldersfiles=localgoogle_drive.listfolder(drive,parent_id)
'''{'id': '14mFtlnxOE79JMCIIaC8-PNx9QZA8GBko', 'title': '20181118', 
    'list':[{'title': 'put_波段_6176_瑞儀.jpg', 'title1': 'https://drive.google.com/file/d/1GaM7zn9_QFbH0Wg2_u9gOd6UkNjA7Li4/view?usp=drivesdk', 
    'modifiedDate': '2018-11-17T08:25:05.280Z'}, .....
    {'title': '僅作個人紀錄，盈虧個人自負', 'title1': 'https://docs.google.com/document/d/17GYHTa7g-umwQyodd9tFWpNbnkxydsN5Bv1t7iNfU2o/edit?usp=drivesdk', 'modifiedDate': '2018-09-24T04:38:07.577Z'}, {'id': '1Bx-lHazUXYhxQNe9zupA5TrA_oJWX97a', 'title': '20180923', 'list': [{'title': 'put_波段_6202_盛群.jpg', 'title1': 'https://drive.google.com/file/d/1rBJZFsYChQ4B4QqWW5KRVqXwp_fhgaVt/view?usp=drivesdk', 'modifiedDate': '2018-09-29T13:02:48.014Z'}, {'title': 'put_波段_5371_中光電.jpg', 'title1': 'https://drive.google.com/file/d/1idCEKBuiMoTvsJCktTKvLKOrC6d7k8_j/view?usp=drivesdk', 'modifiedDate': '2018-09-29T13:02:36.092Z'}, {'title': 'put_波段_2488_漢平.jpg', 'title1': 'https://drive.google.com/file/d/1U7uR7dvqabrJowxVNNmSQ8qtGKmTZuJU/view?usp=drivesdk', 'modifiedDate': '2018-09-29T13:02:31.419Z'}, {'title': 'put_景氣_2617_台航.jpg', 'title1': 'https://drive.google.com/file/d/163XJWtgm7Y4c5IRDHTfkIaYBQkfcGD33/view?usp=drivesdk', 
    'modifiedDate': '2018-09-29T13:02:26.760Z'},#no key:"list"
'''
duration = time.time() - start
print('Get data from Google Drive duration: {:.2f} seconds'.format(duration)) 

# bulk insert atonce then commit
starttime=time.time()
for dic_folderfiles in list_foldersfiles:
    try:
        #for dic_files in dic_folderfiles['list']:
            #print('title:{}, modifiedDate:{}'.format(dic_files['title'],dic_files['modifiedDate']))
            #print('URL:{}'.format(dic_files['title1']))
        BulkInsertTest(db,GoogleDrive_callputjpg).test_bulk_save(dic_folderfiles['list'])
    except KeyError as error:
            print(error)
    except Exception as exception:
            print(exception)

db.session.commit()
duration = time.time() - starttime
q = db.session.query(GoogleDrive_callputjpg)
print('Insert {} rows into table.'.format(get_count(q)))
print('SA ORM Bulk insert, discarding PKs- total time: {:.2f} seconds'.format(duration)) 

# bulk insert atonce then commit
starttime=time.time()
row_count=0
for dic_folderfiles in list_foldersfiles:
    try:
        BulkInsertTest(db,GoogleDrive_callputjpg).test_bulk_insert_mappings(dic_folderfiles['list'])
    except KeyError as error:
            print(error)
    except Exception as exception:
            print(exception)

    row_count += len(dic_folderfiles['list'])

db.session.commit()
duration = time.time() - starttime
print('Insert {} rows into table.'.format(row_count))
print('SA ORM Bulk insert, using dictionaries- total time: {:.2f} seconds'.format(duration))


print("DONE")