
def get_video_lifetime(in_file, out_file, adv_abs, adv_rel, min_days):
    in_fd = open(in_file, 'r')
    out_fd = open(out_file, 'w')
    for line in in_fd.readlines():
        fields = line.strip().split('\t', -1)
        # vid, vci1, vci2, ..., vci30
        vci_list = []
        pct_list = []
        for i in range(1, 1 + 30):
            vci_list.append(int(fields[i]))
        s = sum(vci_list)
        if 0 == s:
            continue
        for i in range(0, 30):
            pct_list.append(1. * vci_list[i] / s)
        
        inactive_days = 0
        # check backwards
        for i in range(29, -1, -1):
            if adv_abs > vci_list[i] and adv_rel > pct_list[i]:
                inactive_days = inactive_days + 1
            else:
                break
        
        if min_days <= inactive_days:
            lifetime = 30 - inactive_days
        else:
            lifetime = 31 
        out_fd.write(fields[0] + '\t' + str(lifetime) + '\n')
    in_fd.close()
    out_fd.close()

if '__main__' == __name__:
    workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/'
    
    get_video_lifetime(workpath + 'data/uploading/clean/view count clean increase/vci', 
                       workpath + 'characterization/uploading/video lifetime/lifetime', 
                       100, 1. / 30, 5)
        
    print('All Done!')
    
    
    