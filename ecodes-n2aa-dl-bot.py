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
    
    print("\n[+] Bot for WP_POSTS has started (Press CTR + C to terminate")

    try:
        while True: 
            (connection, cursor) = database.database_connect()
            # query = "SELECT * FROM wp_bp_activity WHERE type = 'activity_status' OR type = 'activity_video' LIMIT 2"
            # wp_bp_activities = database.read(query)
            query = "SELECT * FROM wp_posts WHERE post_type = '[UPLOADED_YOUTUBE_VIDEO_POST_TYPE]'"
            wp_posts = database.read(connection, cursor, query)
            print("\r[-] Searching.........", end="", flush=True)
            for wp_post in wp_posts:
                url_result = re.search(r'\b(?:http(?:s)?://)?(?:www\.)?(?:m\.)?(?:youtu\.be/|youtube\.com/(?:(?:watch)?\?(?:.*&)?v(?:i)?=|(?:embed)/))([^?&\"\'>][^\s]+)\b', wp_post[4])
                if url_result:
                    url = url_result.group(0)
                    if not wp_post[7] == 'inherit':
                        # print(wp_post[7])
                        r = requests.get("http://example.com:5000/api?url=" + url)
                        if r.status_code == 200:
                            # a:2:{s:2:"id";s:11:"d8oNKlxxu_E";s:6:"status";s:3:"200";}
                            # print(wp_option[0][2][38:44])
                            # print(wp_option[0][2])
                            print("\r[-] Found pending post - Updating wp_posts ...........")

                            option_query = """update wp_posts set post_status='inherit'
                                            where post_content='""" + url + """'"""
                            
                            database.update(connection, cursor, option_query)
                            print("\r[+] Successful - wp_post has been updated")
                    
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


