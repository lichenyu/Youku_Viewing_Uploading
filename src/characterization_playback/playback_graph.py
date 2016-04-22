
def get_vid_viewer_map(in_files):
    vid_viewer_map = {}
    for in_file in in_files:
        in_fd = open(in_file, 'r')
        for line in in_fd.readlines():
            fields = line.strip().split('\t', -1)
            # viewer, vid1, vid2, ...
            for i in range(1, len(fields)):
                if vid_viewer_map.has_key(fields[i]):
                    vid_viewer_map[fields[i]].add(fields[0])
                else:
                    vid_viewer_map[fields[i]] = set()
                    vid_viewer_map[fields[i]].add(fields[0])
        in_fd.close()
    
    return vid_viewer_map

def get_playback_graph(vid_viewer_map, edge_thr, out_file):
    # <viewer pair, vid list>
    viewerpair_vidlist_map = {}
    
    # sort viewer set and generate viewer tuple
    for vid in vid_viewer_map.keys():
        viewer_set = vid_viewer_map[vid]
        viewer_sortedlist = sorted(viewer_set, cmp = lambda x,y: cmp(x, y))
        for i in range(0, len(viewer_sortedlist)):
            for j in range(i + 1, len(viewer_sortedlist)):
                viewerpair = viewer_sortedlist[i] + '\t' + viewer_sortedlist[j]
                if viewerpair_vidlist_map.has_key(viewerpair):
                    viewerpair_vidlist_map[viewerpair].append(vid)
                else:
                    viewerpair_vidlist_map[viewerpair] = []
                    viewerpair_vidlist_map[viewerpair].append(vid)
    # output
    out_fd = open(out_file, 'w')
    for vp in viewerpair_vidlist_map:
        if edge_thr <= viewerpair_vidlist_map[vp]:
            out_fd.write(vp + '\n')

    out_fd.close()


if '__main__' == __name__:
    
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    date_strs = ['20151212', '20151213', '20151214', '20151215', '20151216', '20151217', '20151218']
    
    in_files = []
    for d in date_strs:
        in_files.append(workpath + 'characterization/playback/viewer_request/viewer_reqvid_' + d)
    m = get_vid_viewer_map(in_files)
    
#     # 8175 -> 233824
#     m = get_vid_viewer_map([workpath + 'characterization/playback/viewer_request/viewer_reqvid_20151212'])
    
    get_playback_graph(m, 1, workpath + 'characterization/playback/playback graph/viewer pair')
    
    
    
    print('All Done!')
    
    
    