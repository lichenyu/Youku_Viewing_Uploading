import json
import data.uploading_data_cleaner as udc
from scipy.stats import entropy
import math

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
            dur_fd.write(video_json['duration'] + '\t')
            dur_fd.write(video_json['category'].encode('utf-8'))
            dur_fd.write('\t' + video_json['id'] + '\n')
    json_fd.close()
    dur_fd.close()
    
def get_cat(in_files, out_file):
    cat_count_map = {}
    cat_count_total = 0
    for in_file in in_files:
        in_fd = open(in_file, 'r')
        for line in in_fd.readlines():
            fields = line.strip().split('\t', -1)
            # cat, daily count, collected count
            cat_count_total = cat_count_total + int(fields[1])
            if cat_count_map.has_key(fields[0]):
                cat_count_map[fields[0]] = cat_count_map[fields[0]] + int(fields[1])
            else:
                cat_count_map[fields[0]] = int(fields[1])
        in_fd.close()
    
    out_fd = open(out_file, 'w')
    sorted_map = sorted(cat_count_map.items(), lambda i1, i2: cmp(i1[1], i2[1]), reverse = True)
    for item in sorted_map:
        out_fd.write(item[0])
        out_fd.write('\t' + str(item[1]) + '\t' + str(100. * item[1] / cat_count_total) + '\n')
    out_fd.close()
    
def get_uploader_catentropy(vid_cat_file, uploader_vid_file, out_file):
    vid_cat_map = {}
    vid_cat_fd = open(vid_cat_file, 'r')
    for line in vid_cat_fd.readlines():
        fields = line.strip().split('\t', -1)
        # dur, cat, vid
        if False == vid_cat_map.has_key(fields[2]):
            vid_cat_map[fields[2]] = fields[1]
        else:
            print(line)
    vid_cat_fd.close()
    
    uploader_vid_fd = open(uploader_vid_file, 'r')
    out_fd = open(out_file, 'w')
    for line in uploader_vid_fd.readlines():
        fields = line.strip().split('\t', -1)
        # uid, vid1, vid2, ...
        if 2 >= len(fields):
            continue
        cat_count_map = {}
        total_cat_count = 0
        for i in range(1, len(fields)):
            if vid_cat_map.has_key(fields[i]):
                cat = vid_cat_map[fields[i]]
            else:
                cat = 'others'
                print(fields[i])
            if cat_count_map.has_key(cat):
                cat_count_map[cat] = cat_count_map[cat] + 1
            else:
                cat_count_map[cat] = 1
            total_cat_count = total_cat_count + 1
        # calculate entropy
        p_list = []
        for cat in cat_count_map.keys():
            p_list.append(1. * cat_count_map[cat] / total_cat_count)
        en = entropy(p_list) / math.log(24)
        out_fd.write(fields[0] + '\t' + '%.04f' % (en) + '\n')
    uploader_vid_fd.close()
    out_fd.close()
    

if '__main__' == __name__ :
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', '2015-12-16', '2015-12-17', '2015-12-18']
    
#     for d in date_strs:
#         get_dur(workpath + 'data/uploading/clean/vid/' + d, 
#                 workpath + 'data/uploading/video meta-data/' + d + '_' + d, 
#                 workpath + 'characterization/uploading/video property/' + 'dur_' + d)
#          
#     in_files = []
#     for d in date_strs:
#         in_files.append(workpath + 'characterization/uploading/video property/' + 'dur_' + d)
#     udc.merge_files(in_files, 
#                     workpath + 'characterization/uploading/video property/' + 'dur')
#     
#     in_files = []
#     for d in date_strs:
#         in_files.append(workpath + 'data/uploading/query info/' + d)
#     get_cat(in_files, workpath + 'characterization/uploading/video property/' + 'cat')

    for d in date_strs:
        get_uploader_catentropy(workpath + 'characterization/uploading/video property/dur', 
                                workpath + 'characterization/uploading/uploader_vid/uploader_vid_' + d, 
                                workpath + 'characterization/uploading/video property/cat_entropy_' + d)
    in_files = []
    for d in date_strs:
        in_files.append(workpath + 'characterization/uploading/video property/cat_entropy_' + d)
    udc.merge_files(in_files, 
                    workpath + 'characterization/uploading/video property/cat_entropy')
    
    print('All Done!')
    
    
    