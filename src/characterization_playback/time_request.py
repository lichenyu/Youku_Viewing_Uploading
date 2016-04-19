import time

# 1) time_viewercount, 2) time_reqcount
def get_time_count(in_file, time_viewercount_file, time_reqcount_file):
    time_viewercount_map = {}
    time_reqcount_map = {}
    
    in_fd = open(in_file, 'r')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # 0: sttime, 1: endtime, 2: uip, 3: sip, 4: iptype, 
        # 5: uport, 6: sport, 7: imsi, 8: lac, 9: ci, 
        # 10: upbytes, 11: downbytes, 12: method, 13: rcode, 14: ctype, 
        # 15: clength, 16: host, 17: uri;
        
        hour = time.localtime(float(fields[0])).tm_hour
        
        if time_viewercount_map.has_key(hour):
            time_viewercount_map[hour].add(fields[7])
        else:
            time_viewercount_map[hour] = set()
            time_viewercount_map[hour].add(fields[7])
        if time_reqcount_map.has_key(hour):
            time_reqcount_map[hour] = time_reqcount_map[hour] + 1
        else:
            time_reqcount_map[hour] = 1
    in_fd.close()
    
    time_viewercount_fd = open(time_viewercount_file, 'w')
    time_reqcount_fd = open(time_reqcount_file, 'w')
    for i in range(0, 24):
        time_viewercount_fd.write(str(i) + '\t' + str(len(time_viewercount_map[i])) + '\n')
        time_reqcount_fd.write(str(i) + '\t' + str(time_reqcount_map[i]) + '\n')
    time_viewercount_fd.close()
    time_reqcount_fd.close()

if '__main__' == __name__ :
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    get_time_count(workpath + 'characterization/playback/viewer_request/viewer_req_20151212', 
                   workpath + 'characterization/playback/time_request/time_viewercount_20151212', 
                   workpath + 'characterization/playback/time_request/time_reqcount_20151212')
    
    get_time_count(workpath + 'characterization/playback/viewer_request/viewer_req_20151213', 
                   workpath + 'characterization/playback/time_request/time_viewercount_20151213', 
                   workpath + 'characterization/playback/time_request/time_reqcount_20151213')
    
    get_time_count(workpath + 'characterization/playback/viewer_request/viewer_req_20151214', 
                   workpath + 'characterization/playback/time_request/time_viewercount_20151214', 
                   workpath + 'characterization/playback/time_request/time_reqcount_20151214')
    
    get_time_count(workpath + 'characterization/playback/viewer_request/viewer_req_20151215', 
                   workpath + 'characterization/playback/time_request/time_viewercount_20151215', 
                   workpath + 'characterization/playback/time_request/time_reqcount_20151215')
    
    get_time_count(workpath + 'characterization/playback/viewer_request/viewer_req_20151216', 
                   workpath + 'characterization/playback/time_request/time_viewercount_20151216', 
                   workpath + 'characterization/playback/time_request/time_reqcount_20151216')
    
    get_time_count(workpath + 'characterization/playback/viewer_request/viewer_req_20151217', 
                   workpath + 'characterization/playback/time_request/time_viewercount_20151217', 
                   workpath + 'characterization/playback/time_request/time_reqcount_20151217')
    
    get_time_count(workpath + 'characterization/playback/viewer_request/viewer_req_20151218', 
                   workpath + 'characterization/playback/time_request/time_viewercount_20151218', 
                   workpath + 'characterization/playback/time_request/time_reqcount_20151218')
    
    print('All Done!')
    
    
    