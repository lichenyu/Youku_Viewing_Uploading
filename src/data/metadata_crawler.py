# -*- coding: utf-8 -*-

import urllib2, time

def get_video_metadata(in_file, out_file, cid = '4fa043e1446bdf29'):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    
    api_url = 'https://openapi.youku.com/v2/videos/show_batch.json'
    para_cid = 'client_id=' + cid
    
    vid50_list = []
    query_num = 0
    lines = in_fd.readlines()
    for line in lines:
        # one vid each line
        vid50_list.append(line.strip())
        
        if 50 == len(vid50_list) or len(lines) == query_num * 50 + len(vid50_list):
            para_vid = 'video_ids=' + vid50_list[0]
            for vid in vid50_list[1 : ]:
                para_vid = para_vid + ',' + vid
            
            try_num = 0
            while True:
                try:
                    request_url = api_url + '?' + para_cid + '&' + para_vid
                    print('Querying NO.' + str(query_num * 50 + 1) + '-' + str((query_num + 1) * 50) + ' videos, request url: ' +  request_url)
                    res_rd = urllib2.urlopen(request_url, timeout = 15)
                    res = res_rd.read()
                except urllib2.HTTPError as e:
                    print(str(e))
                    print(e.read())
                    print('Retrying...')
                    try_num = try_num + 1
                except urllib2.URLError as e:
                    print(str(e))
                    print('Retrying...')
                    try_num = try_num + 1
                except Exception as e:
                    print(str(e))
                    print('Retrying...')
                    try_num = try_num + 1
                else:
                    out_fd.write(res + '\n')
                    print('Success')
                    query_num = query_num + 1
                    # keep try until get response and break here
                    break
                if 0 == try_num % 10:
                    time.sleep(60)
            vid50_list = []
            
    in_fd.close()
    out_fd.close()
    
if '__main__' == __name__:
    workpath = u'C:/Documents and Settings/Administrator/桌面/'
    
    get_video_metadata(workpath + 'vid_000', workpath + 'out_000')
    
    print('All Done')
    
    