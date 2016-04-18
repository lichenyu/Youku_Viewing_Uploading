import re

def get_vid_from_uri(uri):
    
    # '/v_show/id_[A-Za-z0-9=]+.*'
    # '/.*videos/[A-Za-z0-9=]+/(comments|download)\\?.*'
    # '/a/vid_[A-Za-z0-9=]+_id_.*'
    # '/embed/[A-Za-z0-9=]{5,}(?!.*/.*).*'
    # '/player\\.php/.*sid/[A-Za-z0-9=]+/.*v.swf.*'
    
    vid_re = re.compile('[A-Za-z0-9=]{5,}')
    
    
    # directly get vid
    if uri.startswith('/v_show/id_'):
        temp = uri[len('/v_show/id_') : ]
        match = vid_re.search(temp)
        vid = temp[match.start(0) : match.end(0)]
    elif uri.startswith('/a/vid_'):
        temp = uri[len('/a/vid_') : ]
        match = vid_re.search(temp)
        vid = temp[match.start(0) : match.end(0)]
    elif uri.startswith('/embed/'):
        temp = uri[len('/embed/') : ]
        match = vid_re.search(temp)
        vid = temp[match.start(0) : match.end(0)]
    # find 'sid/'
    elif uri.startswith('/player.php/'):
        temp = uri[uri.find('sid/') + len('sid/') : ]
        match = vid_re.search(temp)
        vid = temp[match.start(0) : match.end(0)]
    # find 'videos/'
    else:
        temp = uri[uri.find('videos/') + len('videos/') : ]
        match = vid_re.search(temp)
        vid = temp[match.start(0) : match.end(0)]
    return vid

if __name__ == '__main__':
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/data/playback/'
    
    in_fd = open(workpath + 'heilongjiang_v2_20151218', 'r')
    out_fd = open(workpath + 'testout', 'w')
    
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # 0: sttime, 1: endtime, 2: uip, 3: sip, 4: iptype, 
        # 5: uport, 6: sport, 7: imsi, 8: lac, 9: ci, 
        # 10: upbytes, 11: downbytes, 12: method, 13: rcode, 14: ctype, 
        # 15: clength, 16: host, 17: uri;
        vid = get_vid_from_uri(fields[17])
        out_fd.write(vid + '\t '+ fields[7] + '\n')
    
    
    in_fd.close()
    out_fd.close()
    
    print('All Done!')
    