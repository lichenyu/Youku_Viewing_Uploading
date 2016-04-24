workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/characterization/'

uploading_dur = read.table(paste(workpath, 'uploading/video property/dur', sep = ''))$V1
uploading_cat = read.table(paste(workpath, 'uploading/video property/dur', sep = ''))$V2
playback_dur = read.table(paste(workpath, 'playback/video property/dur', sep = ''))$V1
playback_cat = read.table(paste(workpath, 'playback/video property/dur', sep = ''))$V2

levels(playback_cat)

idx = which(uploading_cat == '生活')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '教育')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '音乐')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '游戏')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '亲子')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '电视剧')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '资讯')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '体育')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '创意视频')
summary(uploading_dur[idx] / 60, digits = 10)
idx = which(uploading_cat == '自拍')
summary(uploading_dur[idx] / 60, digits = 10)



idx = which(playback_cat == '电视剧')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '动漫')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '电影')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '生活')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '娱乐')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '综艺')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '音乐')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '自拍')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '教育')
summary(playback_dur[idx] / 60, digits = 10)
idx = which(playback_cat == '搞笑')
summary(playback_dur[idx] / 60, digits = 10)


