import data.playback_data_cleaner as dc

# output: 1) req per viewer, 2) req-vid list per viewer
def get_viewer_reqlist(in_file, viewer_req_file, viewer_reqvid_file, replay_thr):
    in_fd = open(in_file, 'r')
    viewer_req_fd = open(viewer_req_file, 'w')
    viewer_reqvid_fd = open(viewer_reqvid_file, 'w')
    
    # check viewer one by one
    cur_viewer = ''
    # vid, last_time
    vid_time_map = {}
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # 0: sttime, 1: endtime, 2: uip, 3: sip, 4: iptype, 
        # 5: uport, 6: sport, 7: imsi, 8: lac, 9: ci, 
        # 10: upbytes, 11: downbytes, 12: method, 13: rcode, 14: ctype, 
        # 15: clength, 16: host, 17: uri;
        
        vid = dc.get_vid_from_uri(fields[17])
        
        # check whether same viewer
        # new viewer
        if cur_viewer != fields[7]:
            # close last viewer
            if '' != cur_viewer:
                viewer_reqvid_fd.write('\n')
            cur_viewer = fields[7]
            vid_time_map.clear()
            vid_time_map[vid] = fields[0]
            # output for a new viewer
            viewer_req_fd.write(line)
            viewer_reqvid_fd.write(fields[7] + '\t' + vid)
        # same viewer
        else:
            # check whether duplicated request
            # appeared
            if vid in vid_time_map:
                # replay
                if replay_thr <= float(fields[0]) - float(vid_time_map[vid]):
                    viewer_req_fd.write(line)
                    viewer_reqvid_fd.write('\t' + vid)
                vid_time_map[vid] = fields[0]
            # never appeared
            else:
                viewer_req_fd.write(line)
                viewer_reqvid_fd.write('\t' + vid)
                vid_time_map[vid] = fields[0]
    
    viewer_reqvid_fd.write('\n')
    in_fd.close()
    viewer_req_fd.close()
    viewer_reqvid_fd.close()

# req count for each viewer
def get_viewer_reqcount(in_file, out_file):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        out_fd.write(fields[0] + '\t' + str(len(fields) - 1) + '\n')
    in_fd.close()
    out_fd.close()

# unique vid count for each viewer
def get_viewer_vidcount(in_file, out_file):
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
    
# unique vid count for each day
def get_vidcount(in_file, out_file):
    in_fd = open(in_file, 'r')
    vid_set = set()
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        for i in range(1, len(fields)):
            vid_set.add(fields[i])
    in_fd.close()
    
    out_fd = open(out_file, 'w')
    out_fd.write(str(len(vid_set)) + '\n')
    out_fd.close()

if __name__ == '__main__':
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['20151212', '20151213', '20151214', '20151215', '20151216', '20151217', '20151218']
    
    for d in date_strs:
        get_viewer_reqlist(workpath + 'data/playback/heilongjiang_v2_' + d, 
                           workpath + 'characterization/playback/viewer_request/viewer_req_' + d, 
                           workpath + 'characterization/playback/viewer_request/viewer_reqvid_' + d, 
                           60)
        get_viewer_reqcount(workpath + 'characterization/playback/viewer_request/viewer_reqvid_' + d, 
                            workpath + 'characterization/playback/viewer_request/viewer_reqcount_' + d)
        get_viewer_vidcount(workpath + 'characterization/playback/viewer_request/viewer_reqvid_' + d, 
                            workpath + 'characterization/playback/viewer_request/viewer_unividcount_' + d)
    
    print('All Done!')


