import data.metadata_crawler as mc
import json

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
    dur_list = []
    vid_fd = open(vid_file, 'r')
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
            dur_list.append(vid_dur_map[vid])
    vid_fd.close()
    
    cat_fd = open(cat_file, 'w')
    sorted_map = sorted(cat_count_map.items(), lambda i1, i2: cmp(i1[1], i2[1]), reverse = True)
    for item in sorted_map:
        cat_fd.write(item[0].encode('utf-8'))
        cat_fd.write('\t' + str(item[1]) + '\t' + str(100. * item[1] / cat_count_total) + '\n')
    cat_fd.close()
    dur_fd = open(dur_file, 'w')
    for dur in dur_list:
        dur_fd.write(dur + '\n')
    dur_fd.close()

if '__main__' == __name__:
    
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['20151212', '20151213', '20151214', '20151215', '20151216', '20151217', '20151218']
    
    for d in date_strs:
        in_files = []
        in_files.append(workpath + 'characterization/playback/viewer_request/viewer_reqvid_' + d)
        get_vid_list(in_files, workpath + 'characterization/playback/video property/vidlist_' + d)
    
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
#                 workpath + 'characterization/playback/video property/dur',)
    
    print('All Done!')
    
    
    