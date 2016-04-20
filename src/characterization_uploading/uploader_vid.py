import json

def get_uploader_vidlist(vid_file, json_file, out_file):
    vid_set = set()
    vid_fd = open(vid_file, 'r')
    for line in vid_fd.readlines():
        vid_set.add(line.strip())
    vid_fd.close()
    
    json_fd = open(json_file, 'r')
    uploader_vid_map = {}
    for line in json_fd.readlines():
        video_json = json.loads(line)
        if video_json['id'] in vid_set:
            if False == uploader_vid_map.has_key(video_json['user']['id']):
                uploader_vid_map[video_json['user']['id']] = set()
            uploader_vid_map[video_json['user']['id']].add(video_json['id'])
    json_fd.close()
    
    out_fd = open(out_file, 'w')
    for uploader in uploader_vid_map.keys():
        out_fd.write(uploader)
        for vid in uploader_vid_map[uploader]:
            out_fd.write('\t' + vid)
        out_fd.write('\n')
    out_fd.close()
    
# vids are unique for sure
def get_uploader_vidcount(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        out_fd.write(fields[0] + '\t' + str(len(fields) - 1) + '\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', '2015-12-16', '2015-12-17', '2015-12-18']
    
    for d in date_strs:
        get_uploader_vidlist(workpath + 'data/uploading/clean/vid/' + d, 
                             workpath + 'data/uploading/video meta-data/' + d + '_' + d, 
                             workpath + 'characterization/uploading/uploader_vid/' + 'uploader_vid_' + d)
        get_uploader_vidcount(workpath + 'characterization/uploading/uploader_vid/' + 'uploader_vid_' + d, 
                              workpath + 'characterization/uploading/uploader_vid/' + 'uploader_vidcount_' + d)
    
    print('All Done!')
