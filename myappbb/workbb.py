# mystr="https://www.youtube.com/playlist?list=PLdM-WZokR4taS3t8iqp0RvSfF84fj22NN"

# splt=mystr.split("=")
# print(splt)

    
    

def workbb(entered_playlist_id='PL1pf33qWCkmh0_uPQc87cuR3PcZpklf-J',starting_number=1,ending_number=""):
    from googleapiclient.discovery import build
    print("id bb",entered_playlist_id)
    print("starting_number bb",starting_number)
    print("ending_number bb",ending_number)
    # I created this variable global rather than puttin on funciton because I used this variable at the end which is outer the function
    total_videos=0
    total_secondsBB=0
    selected_videos=0

    api_key_bb="AIzaSyBwcm65QtRUn4I_J64twA1oZqFJuC2xsHc"

    youtube_bb=build('youtube','v3',developerKey=api_key_bb)

    import re   # regular expression
    hours_pattern_bby=re.compile(r'(\d+)H')
    minutess_pattern_bby=re.compile(r'(\d+)M')
    secondss_pattern_bby=re.compile(r'(\d+)S')

    from datetime import timedelta


    nextPageTokenBB=None

    

    # entered_playlist_id=input("Enter playlist id \n")
    # if entered_playlist_id == "":
    #     entered_playlist_id="PL1pf33qWCkmh0_uPQc87cuR3PcZpklf-J"        # Default valur.....this is chemistry

    # starting_number=input("starting position..starts from 1...Blank for starting from 1 \n")
    # if starting_number == "":
    #     starting_number = 1           
    # else:
    #     starting_number = int(starting_number)

    # ending_number=input("Ending position...Blank for ending at last \n")

    at_end=False
    if ending_number == "":
        at_end=True
    else:
        at_end=False
        ending_number = int(ending_number)

    while True:
        plst_request_bb=youtube_bb.playlistItems().list(
            part="contentDetails, snippet",
            playlistId=entered_playlist_id,                # just paste your youtube playlist id...that's it
            maxResults=50,            # each iteration get highest 50 videos......(which may be highest allow this api)
            pageToken=nextPageTokenBB         # after each iteration end it will fetch video from next iteration
        )
        pl_response_bb=plst_request_bb.execute()

        breakLoopBB=False
        vid_ids_bb=[]
        for item in pl_response_bb['items']:
            total_videos+=1
            # if (not at_end and total_videos > ending_number ):       
            #     breakLoopBB=True
            #     break           
            
            # elif ((not at_end and total_videos >= starting_number) and (not at_end or total_videos <= ending_number )) or at_end:
            #     print(total_videos,starting_number,ending_number)
            #     vid_ids_bb.append(item['contentDetails']['videoId'])
            #     selected_videos+=1
      
            
            if ( (not at_end and (total_videos >= starting_number)) and (not at_end and (total_videos <= ending_number )) ):
                print(total_videos,starting_number,ending_number)
                vid_ids_bb.append(item['contentDetails']['videoId'])
                selected_videos+=1

        print(vid_ids_bb)
        coma_separated_bb=",".join(vid_ids_bb)          # spliting all value on "," and created a new string
        print(coma_separated_bb)

        vid_request=youtube_bb.videos().list(
            part="contentDetails",
            id=coma_separated_bb                    # you can give upto 50 video highest           
        )

        vid_response_bb=vid_request.execute()

        

        for item in vid_response_bb['items']:
            duration_bb=item['contentDetails']['duration']       
            print(duration_bb)          #  # like "PT2H33M35S" means 2 hours 33 minutes and 35 seconds
            hoursy=hours_pattern_bby.search(duration_bb)        
            minutesy=minutess_pattern_bby.search(duration_bb)        
            secondy=secondss_pattern_bby.search(duration_bb)        
            
            # print(hoursy,minutesy,secondy)

            # minutesy=minutesy.group(1)          # you will get only number
        

        
            minutesy=int(minutesy.group(1)) if minutesy else 0          # like if hour video in 50 seconds that means minutes is none ....so if minutes does not exist or none that put it as zero     
            hoursy=int(hoursy.group(1)) if hoursy else 0        
            secondy=int(secondy.group(1)) if secondy else 0         

            
            video_secondsyy=timedelta(
                hours=hoursy,
                minutes=minutesy,
                seconds=secondy,
            ).total_seconds()       # it will give total seconds
            
            total_secondsBB+=video_secondsyy

            print("Curent Video Seconds ",video_secondsyy)
            print() 
        nextPageTokenBB=pl_response_bb.get('nextPageToken')     # it will get next where we should start our iteration or where start next playlist fetch

        if not nextPageTokenBB or breakLoopBB :         # if no videos left on that playlist it will break the loop
            return {'seconds_rt':total_secondsBB,"total_videosrt":total_videos,"selected_videosrt":selected_videos}     # rt means returned


def myfuncbb(pl="https://www.youtube.com/playlist?list=PL1pf33qWCkmh0_uPQc87cuR3PcZpklf-J",strt_nmbr=1,end_nmbr=""):    
    # pl="https://www.youtube.com/playlist?list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR"
    pl=pl.split("=")[1]
    print("pl baby",pl)
    returned_bb=workbb(pl,strt_nmbr,end_nmbr)
    print(returned_bb)
    total_secondsBB=returned_bb['seconds_rt']
    total_videos=returned_bb['total_videosrt']
    selected_videos=returned_bb['selected_videosrt']

    total_secondsBB=int(total_secondsBB)
    print(f"Total videos {total_videos}")
    print(f"Selected videos {selected_videos}")
    # print(total_secondsBB)

    minuteszz,secondsyy=divmod(total_secondsBB,60)          # function returns a tuple containing the quotient(ভাগফল)  and the remainder(ভাগশেষ) 
    hourskk,minuteszz=divmod(minuteszz,60)

    # print(f"Length of the playlist {hourskk}:{minuteszz}:{secondsyy}")
    return f"Total videos {total_videos} Selected videos {selected_videos}   Length of the playlist {hourskk}:{minuteszz}:{secondsyy}"

# myfuncbb()

# mydict={'seconds_bb':23,'nmp':23}
# print(mydict)
# print(mydict['nmp'])