try:
    # from pytube import YouTube
    # from pytube import Playlist
    # import mysql.connector
    # from flask import Flask, jsonify, request, render_template
    from mysql.connector import Error
    from datetime import datetime
    import re
    import json
    import numpy as np
    # from decimal import Decimal
    
    # import ssl
    import requests
    import urllib
    from time import sleep
    import database
except Exception as e:
    print("Some Modules are missing {}".format(e))


# ssl._create_default_https_context = ssl._create_unverified_context

try:
    
    print("\n[+] Bot for cache has started (Press CTR + C to terminate")

    try:
        while True: 
            (connection, cursor) = database.database_connect()
            # query = "SELECT * FROM wp_bp_activity WHERE type = 'activity_status' OR type = 'activity_video' LIMIT 2"
            # wp_bp_activities = database.read(query)
            query = "SELECT * FROM wp_posts WHERE post_type = '[UPLOADED_YOUTUBE_VIDEO_POST_TYPE]'"
            wp_posts = database.read(connection, cursor, query)
            print("\r[-] Searching.........", end="", flush=True)
            for wp_post in wp_posts:
                url_result = re.findall(r'\b(?:http(?:s)?://)?(?:www\.)?(?:m\.)?(?:youtu\.be/|youtube\.com/(?:(?:watch)?\?(?:.*&)?v(?:i)?=|(?:embed)/))([^?&\"\'>][^\s]+)\b', wp_post[4])
                if len(url_result) > 0:
                    url_id = url_result[0]

                    query = "SELECT * FROM wp_options WHERE option_name = '[SAVED_TRANSIENT]" + url_id + "'"
                    wp_option = database.read(connection, cursor, query)
                    if wp_option[0] and not wp_option[0][2] == 'a:2:{s:2:"id";s:11:"' + url_id + '";s:6:"status";s:3:"404";}':
                        # sleep(1)
                        r = requests.get("http://www.youtube.com/oembed?url=http://www.youtube.com/watch?v=" + url_id + "&format=json", headers={"content-type": "text"})
                        if r.status_code == 404:
                            # a:2:{s:2:"id";s:11:"d8oNKlxxu_E";s:6:"status";s:3:"200";}
                            # print(wp_option[0][2][38:44])
                            # print(wp_option[0][2])
                            print("\r[-] Found 404 for youtube_", url_id, " - processing ...........")

                            option_query = """update wp_options set option_value='a:2:{s:2:"id";s:11:\"""" + url_id + """\";s:6:"status";s:3:"404";}'
                                            where option_name='[SAVED_TRANSIENT]""" + url_id + """'"""
                            
                            database.update(connection, cursor, option_query)
                            print("\r[+] Successful - youtube_", url_id, " has been cached")
                    
            continue

    except KeyboardInterrupt:
        print("Program has been terminated")

except Error as e:
    print("\nError while connecting to MySQL", e, end="", flush=True)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("\nMySQL connection is closed", end="", flush=True)


