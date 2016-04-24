import json
import data.uploading_data_cleaner as udc

# vid, uid, vc, vv_count, video_count, follower_count
def get_userimpact(video_json_file, user_json_file, vc_file, out_file):
    vid_uid_map = {}
    video_json_fd = open(video_json_file, 'r')
    for line in video_json_fd.readlines():
        video_json = json.loads(line.strip())
        if False == vid_uid_map.has_key(video_json['id']):
            vid_uid_map[video_json['id']] = video_json['user']['id']
    video_json_fd.close()
    
    # <uid, [vv_count, video_count, follower_count]>
    uid_info_map = {}
    user_json_fd = open(user_json_file, 'r')
    for line in user_json_fd.readlines():
        user_json = json.loads(line.strip())
        if 0 == len(user_json):
            continue
        if False == uid_info_map.has_key(user_json['id']):
            if int(user_json['followers_count']) >= int(user_json['subscribe_count']):
                f = user_json['followers_count']
            else:
                f = user_json['subscribe_count']
            uid_info_map[user_json['id']] = [user_json['vv_count'], user_json['videos_count'], f]
    user_json_fd.close()
    
    vc_fd = open(vc_file, 'r')
    out_fd = open(out_file, 'w')
    for line in vc_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vc1, vc2, ..., vc30
        vid = fields[0]
        uid = vid_uid_map[vid]
        if False == uid_info_map.has_key(uid):
            continue
        # vid, uid, vc, vv_count, video_count, follower_count
        out_fd.write(vid + '\t' + uid + '\t' + fields[1] + '\t' + fields[30])
        for f in uid_info_map[uid]:
            out_fd.write('\t' + str(f))
        out_fd.write('\n')
    vc_fd.close()
    out_fd.close()

if '__main__' == __name__ :
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['2015-12-12', '2015-12-13', '2015-12-14', '2015-12-15', '2015-12-16', '2015-12-17', '2015-12-18']
    
    for d in date_strs:
        get_userimpact(workpath + 'data/uploading/video meta-data/' + d + '_' + d, 
                       workpath + 'data/uploading/user meta-data/' + d, 
                       workpath + 'data/uploading/clean/view count clean/' + d, 
                       workpath + 'characterization/uploading/follower impact/' + d)
    
    in_files = []
    for d in date_strs:
        in_files.append(workpath + 'characterization/uploading/follower impact/' + d)
    udc.merge_files(in_files, 
                    workpath + 'characterization/uploading/follower impact/' + 'vid_uid_vc_vv_video_follower')
    
    print('All Done!')
    
    
    