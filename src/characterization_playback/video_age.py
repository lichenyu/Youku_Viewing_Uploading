import json
from datetime import date
import data.uploading_data_cleaner as udc

def get_age(date_str, json_file, vid_file, age_file):
    vid_age_map = {}
    json_fd = open(json_file, 'r')
    for line in json_fd.readlines():
        videobatch_json = json.loads(line.strip())
        for video_json in videobatch_json['videos']:
            pub_date = date(int(video_json['published'][0 : 4]), int(video_json['published'][5 : 7]), int(video_json['published'][8 : 10]))
            view_date = date(int(date_str[0 : 4]), int(date_str[4 : 6]), int(date_str[6 : 8]))
            age = (view_date - pub_date).days
            vid_age_map[video_json['id']] = age
    json_fd.close()
    
    vid_fd = open(vid_file, 'r')
    age_fd = open(age_file, 'w')
    for line in vid_fd.readlines():
        vid = line.strip()
        if vid_age_map.has_key(vid):
            age_fd.write(str(vid_age_map[vid]) + '\n')
    vid_fd.close()
    age_fd.close()

if '__main__' == __name__:
    
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['20151212', '20151213', '20151214', '20151215', '20151216', '20151217', '20151218']
    
    for d in date_strs:
        get_age(d, 
                workpath + 'characterization/playback/video property/video-metadata', 
                workpath + 'characterization/playback/video property/vidlist_' + d, 
                workpath + 'characterization/playback/video age/age_' + d)
        
    in_files = []
    for d in date_strs:
        in_files.append(workpath + 'characterization/playback/video age/age_' + d)
    udc.merge_files(in_files, workpath + 'characterization/playback/video age/age')
    
    print('All Done!')
    
    
    