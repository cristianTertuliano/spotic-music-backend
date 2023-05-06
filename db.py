import os
import pymysql
from flask import jsonify

db_user = 'root'
db_password = 'QjV"FGSh;M);H%LP'
db_name = 'spotmusic'
db_local_host = '10.107.32.4'

def open_connection():

    print ('oi')
    conn = pymysql.connect(user=db_user, password=db_password,
                        host=db_local_host, db=db_name,cursorclass=pymysql.cursors.DictCursor)

    return conn

def get_songs():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM songs;')
        songs = cursor.fetchall()
        if result > 0:
           got_songs = jsonify(songs)

        else:
            got_songs = 'Nenhuma Musica Cadastrada na Playlist'

    conn.close()

    return got_songs
