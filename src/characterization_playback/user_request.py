import data.data_cleaner as dc

def get_user_reqlist(in_file, out_file, replay_thr):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
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
                out_fd.write('\n')
            cur_user = fields[7]
            vid_time_map.clear()
            vid_time_map[vid] = fields[0]
            # output for a new user
            out_fd.write(fields[7] + '\t' + vid)
        # same user
        else:
            # check whether duplicated request
            # appeared
            if vid in vid_time_map:
                # replay
                if replay_thr <= float(fields[0]) - float(vid_time_map[vid]):
                    out_fd.write('\t' + vid)
                vid_time_map[vid] = fields[0]
            # never appeared
            else:
                out_fd.write('\t' + vid)
                vid_time_map[vid] = fields[0]
    in_fd.close()
    out_fd.close()
#     user_reqlist = []
#     for line in in_fd.readlines():
#         fields = line.strip().split('\t', -1)
#         # 0: sttime, 1: endtime, 2: uip, 3: sip, 4: iptype, 
#         # 5: uport, 6: sport, 7: imsi, 8: lac, 9: ci, 
#         # 10: upbytes, 11: downbytes, 12: method, 13: rcode, 14: ctype, 
#         # 15: clength, 16: host, 17: uri;
#         
#         # first log
#         if 0 == len(user_reqlist):
#             user_reqlist.append(fields)
#             continue
#         
#         # check whether same user
#         if fields[7] == user_reqlist[len(user_reqlist) - 1][7]:
#             # check whether replay request
#             if (dc.get_vid_from_uri(fields[17]) == dc.get_vid_from_uri(user_reqlist[len(user_reqlist) - 1][17])) and (replay_thr > float(user_reqlist[len(user_reqlist) - 1][0]) - float(fields[0])):
#                 user_reqlist[len(user_reqlist) - 1] = fields
#             else:
#                 user_reqlist.append(fields)
#         else:
#             # output, clear, add
#             out_fd.write(user_reqlist[0][7])
#             for req in user_reqlist:
#                 out_fd.write('\t' + dc.get_vid_from_uri(req[17]))
#             out_fd.write('\n')
#             user_reqlist = []
#             user_reqlist.append(fields)
#     # output last list
#     out_fd.write(user_reqlist[0][7])
#     for req in user_reqlist:
#         out_fd.write('\t' + dc.get_vid_from_uri(req[17]))
#     out_fd.write('\n')
# 
#     in_fd.close()
#     out_fd.close()

if __name__ == '__main__':
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    get_user_reqlist(workpath + 'data/playback/heilongjiang_v2_20151212', 
                     workpath + 'characterization/playback/user_req/user_req_20151212', 
                     60)
    
    print('All Done!')


