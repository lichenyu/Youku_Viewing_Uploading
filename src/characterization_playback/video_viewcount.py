import json

def get_viewcount(json_file, vid_file, vc_file):
    vid_vc_map = {}
    json_fd = open(json_file, 'r')
    for line in json_fd.readlines():
        videobatch_json = json.loads(line.strip())
        for video_json in videobatch_json['videos']:
            vid_vc_map[video_json['id']] = video_json['view_count']
    json_fd.close()
    
    vid_fd = open(vid_file, 'r')
    vc_fd = open(vc_file, 'w')
    for line in vid_fd.readlines():
        vid = line.strip()
        if vid_vc_map.has_key(vid):
            vc_fd.write(str(vid_vc_map[vid]) + '\n')
    vid_fd.close()
    vc_fd.close()

if '__main__' == __name__:
    
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    get_viewcount(workpath + 'characterization/playback/video property/video-metadata', 
                  workpath + 'characterization/playback/video property/vidlist', 
                  workpath + 'characterization/playback/video viewcount/vc')
    
    print('All Done!')
    
    
    