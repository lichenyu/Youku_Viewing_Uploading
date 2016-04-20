import json, time

# 1) time_uploadercount, 2) time_vidcount
def get_time_count(vid_file, json_file, time_uploadercount_file, time_vidcount_file):
    vid_set = set()
    vid_fd = open(vid_file, 'r')
    for line in vid_fd.readlines():
        vid_set.add(line.strip())
    vid_fd.close()
    
    json_fd = open(json_file, 'r')
    time_uploadercount_map = {}
    time_vidcount_map = {}
    for line in json_fd.readlines():
        video_json = json.loads(line.strip())
        
        if video_json['id'] in vid_set:
            hour = time.strptime(video_json['published'], '%Y-%m-%d %H:%M:%S').tm_hour
            
            if time_uploadercount_map.has_key(hour):
                time_uploadercount_map[hour].add(video_json['user']['id'])
            else:
                time_uploadercount_map[hour] = set()
                time_uploadercount_map[hour].add(video_json['user']['id'])
        
            if time_vidcount_map.has_key(hour):
                time_vidcount_map[hour] = time_vidcount_map[hour] + 1
            else:
                time_vidcount_map[hour] = 1
    json_fd.close()
    
    time_uploadercount_fd = open(time_uploadercount_file, 'w')
    time_vidcount_fd = open(time_vidcount_file, 'w')
    for i in range(0, 24):
        time_uploadercount_fd.write(str(i) + '\t' + str(len(time_uploadercount_map[i])) + '\n')
        time_vidcount_fd.write(str(i) + '\t' + str(time_vidcount_map[i]) + '\n')
    time_uploadercount_fd.close()
    time_vidcount_fd.close()

if '__main__' == __name__ :
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', '2015-12-16', '2015-12-17', '2015-12-18']
    
    for d in date_strs:
        get_time_count(workpath + 'data/uploading/clean/vid/' + d, 
                       workpath + 'data/uploading/video meta-data/' + d + '_' + d, 
                       workpath + 'characterization/uploading/time_vid/' + 'time_uploadercount_' + d, 
                       workpath + 'characterization/uploading/time_vid/' + 'time_vidcount_' + d)
    
    print('All Done!')
    
    
    