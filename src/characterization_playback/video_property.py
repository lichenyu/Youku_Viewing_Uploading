import data.metadata_crawler as mc
import json
from scipy.stats import entropy
import math
import data.uploading_data_cleaner as udc

# get vid list from daily user requests
def get_vid_list(in_files, out_file):
    out_fd = open(out_file, 'w')
    for f in in_files:
        in_fd = open(f, 'r')
        for line in in_fd.readlines():
            fields = line.strip().split('\t', -1)
            
            # view_reqvid: viewer, vid1, vid2, ..., vidn
            for i in range(1, len(fields)):
                out_fd.write(fields[i] + '\n')
        in_fd.close()
    out_fd.close()
    
# request results remove duplicated vids
# we should use vid list again for the video property statistic
    
def get_catedur(json_file, vid_file, cat_file, dur_file):
    vid_cat_map = {}
    vid_dur_map = {}
    json_fd = open(json_file, 'r')
    for line in json_fd.readlines():
        videobatch_json = json.loads(line.strip())
        for video_json in videobatch_json['videos']:
            vid_cat_map[video_json['id']] = video_json['category']
            vid_dur_map[video_json['id']] = video_json['duration']
    json_fd.close()
    
    cat_count_map = {}
    cat_count_total = 0
    vid_fd = open(vid_file, 'r')
    dur_fd = open(dur_file, 'w')
    for line in vid_fd.readlines():
        vid = line.strip()
        if vid_cat_map.has_key(vid):
            cat = vid_cat_map[vid]
            cat_count_total = cat_count_total + 1
            if cat_count_map.has_key(cat):
                cat_count_map[cat] = cat_count_map[cat] + 1
            else:
                cat_count_map[cat] = 1
        if vid_dur_map.has_key(vid) and None != vid_dur_map[vid]:
            dur_fd.write(vid_dur_map[vid] + '\t')
            dur_fd.write(vid_cat_map[vid].encode('utf-8'))
            dur_fd.write('\t' + vid + '\n')
    vid_fd.close()
    dur_fd.close()
    
    cat_fd = open(cat_file, 'w')
    sorted_map = sorted(cat_count_map.items(), lambda i1, i2: cmp(i1[1], i2[1]), reverse = True)
    for item in sorted_map:
        cat_fd.write(item[0].encode('utf-8'))
        cat_fd.write('\t' + str(item[1]) + '\t' + str(100. * item[1] / cat_count_total) + '\n')
    cat_fd.close()
    
def get_viewer_catentropy(vid_cat_file, viewer_vid_file, out_file):
    vid_cat_map = {}
    vid_cat_fd = open(vid_cat_file, 'r')
    for line in vid_cat_fd.readlines():
        fields = line.strip().split('\t', -1)
        # dur, cat, vid
        if False == vid_cat_map.has_key(fields[2]):
            vid_cat_map[fields[2]] = fields[1]
        else:
            pass
            #print(line)
    vid_cat_fd.close()
    
    viewer_vid_fd = open(viewer_vid_file, 'r')
    out_fd = open(out_file, 'w')
    for line in viewer_vid_fd.readlines():
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
    viewer_vid_fd.close()
    out_fd.close()

if '__main__' == __name__:
    
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['20151212', '20151213', '20151214', '20151215', '20151216', '20151217', '20151218']
    
#     for d in date_strs:
#         in_files = []
#         in_files.append(workpath + 'characterization/playback/viewer_request/viewer_reqvid_' + d)
#         get_vid_list(in_files, workpath + 'characterization/playback/video property/vidlist_' + d)
    
#     in_files = []
#     for d in date_strs:
#         in_files.append(workpath + 'characterization/playback/viewer_request/viewer_reqvid_' + d)
#     get_vid_list(in_files, workpath + 'characterization/playback/video property/vidlist')
#     
#     mc.get_video_metadata(workpath + 'characterization/playback/video property/vidlist', 
#                           workpath + 'characterization/playback/video property/video-metadata')

#     get_catedur(workpath + 'characterization/playback/video property/video-metadata', 
#                 workpath + 'characterization/playback/video property/vidlist', 
#                 workpath + 'characterization/playback/video property/cat',
#                 workpath + 'characterization/playback/video property/dur')
    
    for d in date_strs:
        get_viewer_catentropy(workpath + 'characterization/playback/video property/dur', 
                                workpath + 'characterization/playback/viewer_request/viewer_reqvid_' + d, 
                                workpath + 'characterization/playback/video property/cat_entropy_' + d)
    in_files = []
    for d in date_strs:
        in_files.append(workpath + 'characterization/playback/video property/cat_entropy_' + d)
    udc.merge_files(in_files, 
                    workpath + 'characterization/playback/video property/cat_entropy')
    
    print('All Done!')
    
    
    