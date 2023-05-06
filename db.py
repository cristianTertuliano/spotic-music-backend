import os
import pymysql
from flask import jsonify

db_user = 'root'
db_password = 'QjV"FGSh;M);H%LP'
db_name = 'spotmusic'
db_local_host = '34.72.96.119'
db_connection_name = 'grupo-11-384916:us-central1:spotmusic01'

def open_connection():
    try:
        if db_connection_name:
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
            print ('tchau')
        else:
            print ('oi')
            conn = pymysql.connect(user=db_user, password=db_password,
                                host=db_local_host, db=db_name,cursorclass=pymysql.cursors.DictCursor)

    except pymysql.MySQLError as e:
        print(e)

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
