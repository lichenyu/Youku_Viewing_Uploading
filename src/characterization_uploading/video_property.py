import json
import data.uploading_data_cleaner as udc

def get_dur(vid_file, json_file, dur_file):
    vid_set = set()
    vid_fd = open(vid_file, 'r')
    for line in vid_fd.readlines():
        vid_set.add(line.strip())
    vid_fd.close()
    
    json_fd = open(json_file, 'r')
    dur_fd = open(dur_file, 'w')
    for line in json_fd.readlines():
        video_json = json.loads(line.strip())
        if video_json['id'] in vid_set and None != video_json['duration']:
            dur_fd.write(video_json['duration'] + '\n')
    json_fd.close()
    dur_fd.close()

if '__main__' == __name__ :
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', '2015-12-16', '2015-12-17', '2015-12-18']
    
    for d in date_strs:
        get_dur(workpath + 'data/uploading/clean/vid/' + d, 
                workpath + 'data/uploading/video meta-data/' + d + '_' + d, 
                workpath + 'characterization/uploading/video property/' + 'dur_' + d)
        
    in_files = []
    for d in date_strs:
        in_files.append(workpath + 'characterization/uploading/video property/' + 'dur_' + d)
    udc.merge_files(in_files, 
                    workpath + 'characterization/uploading/video property/' + 'dur')
    
    print('All Done!')
    
    
    