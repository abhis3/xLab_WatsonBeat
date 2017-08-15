from __future__ import print_function

import os
import sys
import time
import json
import random
import requests
import commands
from requests_oauthlib import OAuth1


MEDIA_ENDPOINT_URL_REQ = 'https://upload.twitter.com/1.1/media/upload.json'
POST_TWEET_URL_REQ = 'https://api.twitter.com/1.1/statuses/update.json'

MEDIA_ENDPOINT_URL = '/1.1/media/upload.json'
POST_TWEET_URL = '/1.1/statuses/update.json'


CONSUMER_KEY = 'pKU9RRaDjFtjefXJNTtypJr1k'
CONSUMER_SECRET = '0pRo0Qu05mBi9rxt8DuEAVS2BMRkqcQoGaKR6CRJpIsirRVGnw'
ACCESS_TOKEN = '837326619794526208-FMikFB9bw3ryfEHErhpKnejlZ3YHcGa'
ACCESS_TOKEN_SECRET = 'SyAiw2ZUkLwZsSck6eyPmBmIrkPC6lsoA82YhLIgYe9Tw'

VIDEO_FILENAME = "/Users/jmukund/Repo/Electron/WatsonBeatDesktopApp/app/mp4/wb.mp4"
VIDEO_FILENAME = ''
#ffmpeg -i input.mp4 -i input.mp3 -c copy -map 0:0 -map 1:0 output.mp4


oauth = OAuth1(CONSUMER_KEY,
  client_secret=CONSUMER_SECRET,
  resource_owner_key=ACCESS_TOKEN,
  resource_owner_secret=ACCESS_TOKEN_SECRET)

class VideoTweet(object):

    def __init__(self, file_name, twitterMessage):
        '''
        Defines video tweet properties
        '''
        self.video_filename = file_name
        self.total_bytes = os.path.getsize(self.video_filename)
        self.media_id = None
        self.processing_info = None
        self.twitterMessage = twitterMessage

    def upload_init_small_chunks(self):
        '''
        Initializes Upload
        '''
        print('INIT')

        # the twurl way
        #twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=INIT&media_type=video/mp4&total_bytes=1293379"
        initCmdStr = 'twurl -H upload.twitter.com "' + MEDIA_ENDPOINT_URL + '" -d "command=INIT&media_type=video/mp4&total_bytes=' + str(self.total_bytes) +'"'
        print (initCmdStr)
        initCmd = commands.getoutput(initCmdStr)
        json_initData = json.loads(initCmd)
        print(initCmd)
        self.media_id = json_initData['media_id']
        print(self.media_id)


    def upload_init_large_chunks(self):
        '''
        Initializes Upload
        '''
        print('INIT')

        #the requests way
        request_data = {
            'command': 'INIT',
            'media_type': 'video/mp4',
            'total_bytes': self.total_bytes,
            'media_category': 'tweet_video'
        }
        req = requests.post(url=MEDIA_ENDPOINT_URL_REQ, data=request_data, auth=oauth)
        self.media_id = req.json()['media_id']
        print('Media ID:', self.media_id)


    def upload_append_small_chunks (self) :
        '''
        Uploads media in one go. small chnunks <=1.5MB
        '''

        # the twurl way
        #twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=APPEND&media_id=837380537727647748&segment_index=0" --file out.mp4 --file-field "media"
        appendCmdStr = 'twurl -H upload.twitter.com "' + MEDIA_ENDPOINT_URL + '" -d "command=APPEND&media_id='+str(self.media_id)+'&segment_index=0"' + ' --file ' + self.video_filename + ' --file-field "media"'
        print(appendCmdStr)
        appendCmd = commands.getoutput(appendCmdStr)
        print(appendCmd)
        if ( appendCmd == '' ) :
            print ( "Append Success")
        else :
            print ( "Append Failed")
            sys.exit(-1)

    def upload_append_large_chunks (self) :
        '''
        Uploads media in chunks and appends to chunks uploaded
        '''

        segment_id = 0
        bytes_sent = 0
        file = open ( self.video_filename, mode='rb')

        while bytes_sent < self.total_bytes :
            chunk=file.read(2 * 1024 * 1024) # 2MB chunk

            print ( 'APPEND')

            request_data = {
                'command': 'APPEND',
                'media_id': self.media_id,
                'segment_index': segment_id
                }

            files = {
                'media':chunk
                }

            req = requests.post(url=MEDIA_ENDPOINT_URL_REQ, data=request_data, files=files, auth=oauth)

            if req.status_code < 200 or req.status_code > 299:
                print(req.status_code)
                print(req.text)
                sys.exit(0)

            segment_id = segment_id + 1
            bytes_sent = file.tell()

            print('%s of %s bytes uploaded' % (str(bytes_sent), str(self.total_bytes)))

        print('Upload chunks complete.')

    def upload_finalize_large_chunks(self):
        '''
        Finalizes uploads and starts video processing
        '''
        print('FINALIZE')

        request_data = {
        'command': 'FINALIZE',
        'media_id': self.media_id
        }

        req = requests.post(url=MEDIA_ENDPOINT_URL_REQ, data=request_data, auth=oauth)
        print("Request: ", req.json())
        print()

        self.processing_info = req.json().get('processing_info', None)
        self.check_status()

    def check_status(self):
        '''
        Checks video processing status
        '''
        if self.processing_info is None:
            return

        state = self.processing_info['state']

        print('Media processing status is %s ' % state)

        if state == u'succeeded':
            return

        if state == u'failed':
            sys.exit(0)

        check_after_secs = self.processing_info['check_after_secs']

        print('Checking after %s seconds' % str(check_after_secs))
        time.sleep(check_after_secs)

        print('STATUS')

        request_params = {
            'command': 'STATUS',
            'media_id': self.media_id
            }

        req = requests.get(url=MEDIA_ENDPOINT_URL_REQ, params=request_params, auth=oauth)

        print("Req Get: ", req.json())

        self.processing_info = req.json().get('processing_info', None)
        self.check_status()


    def upload_finalize_small_chunks ( self ) :

        '''
        Finalizes uploads and starts video processing
        '''
        print('FINALIZE')

        # the twurl way
        #twurl -H upload.twitter.com "/1.1/media/upload.json" -d "command=FINALIZE&media_id=837380537727647748"
        finalizeCmdStr = 'twurl -H upload.twitter.com "' + MEDIA_ENDPOINT_URL + '" -d "command=FINALIZE&media_id='+str(self.media_id)+'&segment_index=0"'
        print(finalizeCmdStr)
        finalizeCmd = commands.getoutput(finalizeCmdStr)
        print(finalizeCmd)
        json_finalizeData = json.loads(finalizeCmd)
        if ( self.media_id == json_finalizeData['media_id'] ) :
            print ( "Finalize Success")
        else :
            print ( "Finalize Failed")
            sys.exit(-1)

    def tweet( self ) :
        '''
        Publishes Tweet with attached video
        '''
        # the twurl way
        #twurl "/1.1/statuses/update.json" -d "media_ids=837380537727647748&status=Sample Tweet with media_ids and twurl"
        tweetCmdStr = 'twurl "' + POST_TWEET_URL + '" -d "media_ids='+str(self.media_id)+'&status=' + self.twitterMessage +'"'
        print ( tweetCmdStr )
        tweetCmd = commands.getoutput(tweetCmdStr)
        print ( tweetCmd )
        json_tweetData = json.loads(tweetCmd)
        if ( 'errors' in json_tweetData ) :
            print ( "Tweet Post Failed")
            sys.exit(-1)
        else :
            print ( "Tweet Success")

    def tweet_large_chunks(self):
        '''
        Publishes Tweet with attached video
        '''
        request_data = {
        'status': self.twitterMessage,
        'media_ids': self.media_id
        }

        req = requests.post(url=POST_TWEET_URL_REQ, data=request_data, auth=oauth)
        print("Tweet Req.json: ", req.json())


def CreateMp4 ( mp3File, dirname ) :

    fNameNoExt = mp3File.replace ( ".mp3", '')
    watsonVideoFile = dirname + "/mp4/watsonbeat16s.mp4"

    #convert mp3File to wav
    #ffmpeg -i amped-0.mp3 amped.wav
    cmd = 'ffmpeg -i ' + mp3File + " " + fNameNoExt + ".wav"
    print ( "convert mp3File to wav: ", cmd)
    if ( not os.path.isfile(fNameNoExt + ".wav")) :
        os.system(cmd)
    #time slice wav to 16s
    #ffmpeg -i amped.wav  -ss 0 -t 16 amped-16s.wav
    cmd = 'ffmpeg -i ' +  fNameNoExt + ".wav" + " -ss 0 -t 16 " +  fNameNoExt + "-16s.wav"
    print ( "time slice wav to 16s: ", cmd)
    if ( not os.path.isfile(fNameNoExt + "-16s.wav")) :
        os.system(cmd)
    #convert back to mp3
    #ffmpeg -i amped-16s.wav amped-16s.mp3
    cmd = 'ffmpeg -i ' +   fNameNoExt + "-16s.wav " + fNameNoExt + "-16s.mp3"
    print ( "convert back to mp3: ", cmd)
    if ( not os.path.isfile(fNameNoExt + "-16s.mp3")) :
        os.system(cmd)
    #add audio to video
    #ffmpeg -i amped-16s.mp3 -i watsonbeat16s.mp4 wb.mp4
    cmd = 'ffmpeg -i ' +   fNameNoExt + "-16s.mp3 " + " -i " + watsonVideoFile + " " + fNameNoExt + "-16s.mp4"
    print ( "add audio to video: ", cmd)
    if ( not os.path.isfile(fNameNoExt + "-16s.mp4")) :
        os.system(cmd)

    return ( fNameNoExt + "-16s.mp4")

if __name__ == '__main__':


    try :
        mp3File = sys.argv[1]
        dirname = sys.argv[2]
        if ( os.path.isfile(mp3File)) :
            print ( "Mp3File: ", mp3File )
            VIDEO_FILENAME = CreateMp4(mp3File, dirname)
            print ( "Video File Name:", VIDEO_FILENAME)
    except:
        print ( "Error converting mp3 to mp4")
        sys.exit(-1)



    try:
        twitterHandle = sys.argv[3]
        twitterHandle = twitterHandle.replace("@", '')
        twitterHandle = "@" + twitterHandle
    except :
        twitterHandle = ''
    try:
        twitterMessage = sys.argv[4]
        twitterMessage = twitterHandle + " " + twitterMessage
    except :
        twitterMessage = random.choice( ['Rocking with @ibmwatsonbeat #ibmwatsonbeat', 'Grooving with @ibmwatsonbeat #ibmwatsonbeat', 'Jammin with @ibmwatsonbeat #ibmwatsonbeat'])



    print ( "twitter Handle:", twitterHandle)
    print ( "twitter Message:", twitterMessage)


    videoTweet = VideoTweet(VIDEO_FILENAME, twitterMessage)
    videoTweet.upload_init_large_chunks()
    videoTweet.upload_append_large_chunks()
    videoTweet.upload_finalize_large_chunks()
    videoTweet.tweet_large_chunks()


    #videoTweet.upload_append_small_chunks()
    #videoTweet.upload_finalize_small_chunks()
    #videoTweet.tweet()
