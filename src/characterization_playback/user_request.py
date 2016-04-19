import data.data_cleaner as dc

# output: 1) record per user, 2) vid list per user
def get_user_reqlist(in_file, user_req_file, user_vid_file, replay_thr):
    in_fd = open(in_file, 'r')
    user_req_fd = open(user_req_file, 'w')
    user_vid_fd = open(user_vid_file, 'w')
    
    # check user one by one
    cur_user = ''
    # vid, last_time
    vid_time_map = {}
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # 0: sttime, 1: endtime, 2: uip, 3: sip, 4: iptype, 
        # 5: uport, 6: sport, 7: imsi, 8: lac, 9: ci, 
        # 10: upbytes, 11: downbytes, 12: method, 13: rcode, 14: ctype, 
        # 15: clength, 16: host, 17: uri;
        
        vid = dc.get_vid_from_uri(fields[17])
        
        # check whether same user
        # new user
        if cur_user != fields[7]:
            # close last user
            if '' != cur_user:
                user_vid_fd.write('\n')
            cur_user = fields[7]
            vid_time_map.clear()
            vid_time_map[vid] = fields[0]
            # output for a new user
            user_req_fd.write(line)
            user_vid_fd.write(fields[7] + '\t' + vid)
        # same user
        else:
            # check whether duplicated request
            # appeared
            if vid in vid_time_map:
                # replay
                if replay_thr <= float(fields[0]) - float(vid_time_map[vid]):
                    user_req_fd.write(line)
                    user_vid_fd.write('\t' + vid)
                vid_time_map[vid] = fields[0]
            # never appeared
            else:
                user_req_fd.write(line)
                user_vid_fd.write('\t' + vid)
                vid_time_map[vid] = fields[0]
    
    in_fd.close()
    user_req_fd.close()
    user_vid_fd.close()

def get_user_reqcount(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        out_fd.write(fields[0] + '\t' + str(len(fields) - 1) + '\n')
    in_fd.close()
    out_fd.close()
    
def get_user_vidcount(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        vid_set = set()
        for i in range(1, len(fields)):
            vid_set.add(fields[i])
        out_fd.write(fields[0] + '\t' + str(len(vid_set)) + '\n')
    in_fd.close()
    out_fd.close()

if __name__ == '__main__':
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    get_user_reqlist(workpath + 'data/playback/heilongjiang_v2_20151212', 
                     workpath + 'characterization/playback/user_req/user_req_20151212', 
                     workpath + 'characterization/playback/user_req/user_vid_20151212', 
                     60)
    get_user_reqlist(workpath + 'data/playback/heilongjiang_v2_20151213', 
                     workpath + 'characterization/playback/user_req/user_req_20151213', 
                     workpath + 'characterization/playback/user_req/user_vid_20151213', 
                     60)
    get_user_reqlist(workpath + 'data/playback/heilongjiang_v2_20151214', 
                     workpath + 'characterization/playback/user_req/user_req_20151214', 
                     workpath + 'characterization/playback/user_req/user_vid_20151214', 
                     60)
    get_user_reqlist(workpath + 'data/playback/heilongjiang_v2_20151215', 
                     workpath + 'characterization/playback/user_req/user_req_20151215', 
                     workpath + 'characterization/playback/user_req/user_vid_20151215', 
                     60)
    get_user_reqlist(workpath + 'data/playback/heilongjiang_v2_20151216', 
                     workpath + 'characterization/playback/user_req/user_req_20151216', 
                     workpath + 'characterization/playback/user_req/user_vid_20151216', 
                     60)
    get_user_reqlist(workpath + 'data/playback/heilongjiang_v2_20151217', 
                     workpath + 'characterization/playback/user_req/user_req_20151217', 
                     workpath + 'characterization/playback/user_req/user_vid_20151217', 
                     60)
    get_user_reqlist(workpath + 'data/playback/heilongjiang_v2_20151218', 
                     workpath + 'characterization/playback/user_req/user_req_20151218', 
                     workpath + 'characterization/playback/user_req/user_vid_20151218', 
                     60)
    
    get_user_reqcount(workpath + 'characterization/playback/user_req/user_vid_20151212', 
                      workpath + 'characterization/playback/user_req/user_reqcount_20151212')
    get_user_vidcount(workpath + 'characterization/playback/user_req/user_vid_20151212', 
                      workpath + 'characterization/playback/user_req/user_vidcount_20151212')
    
    get_user_reqcount(workpath + 'characterization/playback/user_req/user_vid_20151213', 
                      workpath + 'characterization/playback/user_req/user_reqcount_20151213')
    get_user_vidcount(workpath + 'characterization/playback/user_req/user_vid_20151213', 
                      workpath + 'characterization/playback/user_req/user_vidcount_20151213')
    
    get_user_reqcount(workpath + 'characterization/playback/user_req/user_vid_20151214', 
                      workpath + 'characterization/playback/user_req/user_reqcount_20151214')
    get_user_vidcount(workpath + 'characterization/playback/user_req/user_vid_20151214', 
                      workpath + 'characterization/playback/user_req/user_vidcount_20151214')
    
    get_user_reqcount(workpath + 'characterization/playback/user_req/user_vid_20151215', 
                      workpath + 'characterization/playback/user_req/user_reqcount_20151215')
    get_user_vidcount(workpath + 'characterization/playback/user_req/user_vid_20151215', 
                      workpath + 'characterization/playback/user_req/user_vidcount_20151215')
    
    get_user_reqcount(workpath + 'characterization/playback/user_req/user_vid_20151216', 
                      workpath + 'characterization/playback/user_req/user_reqcount_20151216')
    get_user_vidcount(workpath + 'characterization/playback/user_req/user_vid_20151216', 
                      workpath + 'characterization/playback/user_req/user_vidcount_20151216')
    
    get_user_reqcount(workpath + 'characterization/playback/user_req/user_vid_20151217', 
                      workpath + 'characterization/playback/user_req/user_reqcount_20151217')
    get_user_vidcount(workpath + 'characterization/playback/user_req/user_vid_20151217', 
                      workpath + 'characterization/playback/user_req/user_vidcount_20151217')
    
    get_user_reqcount(workpath + 'characterization/playback/user_req/user_vid_20151218', 
                      workpath + 'characterization/playback/user_req/user_reqcount_20151218')
    get_user_vidcount(workpath + 'characterization/playback/user_req/user_vid_20151218', 
                      workpath + 'characterization/playback/user_req/user_vidcount_20151218')
    
    print('All Done!')


