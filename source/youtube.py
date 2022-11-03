try:
    from pytube import YouTube
    from pytube import Playlist
    import pytube
    import urllib
    import requests
    from time import sleep
except Exception as e:
    print("Some Modules are missing {}".format(e))


def youtube_downloader(url):
    url = url

    try:
        ytd = YouTube(url)

        video_id = ytd.video_id

        fn = ytd.title
        thumb = ytd.thumbnail_url
        # title = fn.replace(" ", "-")
        fn = fn.replace(fn, "youtube_" + video_id)
        
        path = '[PATH_TO_STORE_DOWNLOADED_YOUTUBE_VIDEOS]'
        
        ytd.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path, filename=fn)
        
        r = requests.get(thumb)

        with open(path + fn + '.jpg', 'wb') as f:
            f.write(r.content)
        # Get Available High Resolution
        # print(ytd.streams.filter(progressive=True).all())

        # All the high quality streams
        # print(ytd.streams.filter(adaptive=True).all())

        # Only audio
        # print(ytd.streams.filter(only_audio=True).all())

        # Only mp4 streams
        # print(ytd.streams.filter(subtype="mp4").all())

        # Loop All Resolutions
        # for x in ytd.streams.all():
        #     print(x)
    except pytube.exceptions.RegexMatchError:
        print('\nThe Regex pattern did not return any matches for the video: {}'.format(url), end="", flush=True)

    except pytube.exceptions.ExtractError:
        print('\nAn extraction error occurred for the video: {}'.format(url), end="", flush=True)

    except pytube.exceptions.VideoUnavailable:
        print('\nThe following video is unavailable: {}'.format(url), end="", flush=True)

    # except(urllib2.URLError):
    #     print "No Internet connection"
    # except(KeyboardInterrupt):
    #     print "Unusal Termination Video Not Downloaded"

    # except OSError as err:
    #     print('\nNo such file or directory: {}'.format(err), end="", flush=True)

    # except urllib2.error.URLError as err:
    #     print('\nNo such file or directory: {}'.format(err), end="", flush=True)

    
