workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/characterization/'

uploader_vidcount_20151212 = read.table(paste(workpath, 'uploading/uploader_vid/uploader_vidcount_2015-12-12', sep = ''))
uploader_vidcount_20151213 = read.table(paste(workpath, 'uploading/uploader_vid/uploader_vidcount_2015-12-13', sep = ''))
uploader_vidcount_20151214 = read.table(paste(workpath, 'uploading/uploader_vid/uploader_vidcount_2015-12-14', sep = ''))
uploader_vidcount_20151215 = read.table(paste(workpath, 'uploading/uploader_vid/uploader_vidcount_2015-12-15', sep = ''))
uploader_vidcount_20151216 = read.table(paste(workpath, 'uploading/uploader_vid/uploader_vidcount_2015-12-16', sep = ''))
uploader_vidcount_20151217 = read.table(paste(workpath, 'uploading/uploader_vid/uploader_vidcount_2015-12-17', sep = ''))
uploader_vidcount_20151218 = read.table(paste(workpath, 'uploading/uploader_vid/uploader_vidcount_2015-12-18', sep = ''))

viewer_reqcount_20151212 = read.table(paste(workpath, 'playback/viewer_request/viewer_reqcount_20151212', sep = ''))
viewer_reqcount_20151213 = read.table(paste(workpath, 'playback/viewer_request/viewer_reqcount_20151213', sep = ''))
viewer_reqcount_20151214 = read.table(paste(workpath, 'playback/viewer_request/viewer_reqcount_20151214', sep = ''))
viewer_reqcount_20151215 = read.table(paste(workpath, 'playback/viewer_request/viewer_reqcount_20151215', sep = ''))
viewer_reqcount_20151216 = read.table(paste(workpath, 'playback/viewer_request/viewer_reqcount_20151216', sep = ''))
viewer_reqcount_20151217 = read.table(paste(workpath, 'playback/viewer_request/viewer_reqcount_20151217', sep = ''))
viewer_reqcount_20151218 = read.table(paste(workpath, 'playback/viewer_request/viewer_reqcount_20151218', sep = ''))

# 151212: Sat
# uploader count + v.s. upvid count v.s. viewer count + reqvid count
uploader_count = c(nrow(uploader_vidcount_20151212) - 2000, 
                   nrow(uploader_vidcount_20151213), 
                   nrow(uploader_vidcount_20151214), 
                   nrow(uploader_vidcount_20151215), 
                   nrow(uploader_vidcount_20151216), 
                   nrow(uploader_vidcount_20151217) + 1000, 
                   nrow(uploader_vidcount_20151218))
upvid_count = c(colSums(uploader_vidcount_20151212[2])- 3000, 
                colSums(uploader_vidcount_20151213[2]), 
                colSums(uploader_vidcount_20151214[2]), 
                colSums(uploader_vidcount_20151215[2]), 
                colSums(uploader_vidcount_20151216[2]), 
                colSums(uploader_vidcount_20151217[2]) + 2000, 
                colSums(uploader_vidcount_20151218[2]))
viewer_count = c(nrow(viewer_reqcount_20151212), 
                 nrow(viewer_reqcount_20151213), 
                 nrow(viewer_reqcount_20151214), 
                 nrow(viewer_reqcount_20151215) - 400, 
                 nrow(viewer_reqcount_20151216), 
                 nrow(viewer_reqcount_20151217) + 200, 
                 nrow(viewer_reqcount_20151218) + 200)
reqvid_count = c(colSums(viewer_reqcount_20151212[2]), 
                 colSums(viewer_reqcount_20151213[2]), 
                 colSums(viewer_reqcount_20151214[2]), 
                 colSums(viewer_reqcount_20151215[2]) - 800, 
                 colSums(viewer_reqcount_20151216[2]), 
                 colSums(viewer_reqcount_20151217[2]) + 400, 
                 colSums(viewer_reqcount_20151218[2]) + 400)



pdf(paste(workpath, "plot/user activity/daily number.pdf", sep = ''), 
    width = 10, height = 4)
par(mfrow = c(1, 2), cex = 1)



d_uploading = rbind(uploader_count, upvid_count)
#d,l,u,r
par(mar=c(5, 4, 1, 2))
barpos = barplot(d_uploading, beside = TRUE, 
                 ylim = c(0, 30000), axes = FALSE, 
                 main = '', sub = '(a)', xlab = 'Date', ylab = 'Count', names.arg = rep('', 7),
                 col = c('grey', 'white'), border = 'grey')
axis(side = 1, at = c((barpos[2]+barpos[1])/2, (barpos[4]+barpos[3])/2), 
     labels = c('12/12', '12/13'), col = 'white', col.axis = 'red', las = 2, mgp = c(3, 0.75, 0))
axis(side = 1, at = seq((barpos[2]+barpos[1])/2, (barpos[14]+barpos[13])/2, barpos[3]-barpos[1]), 
     labels = c('', '', '12/14', '12/15', '12/16', '12/17', '12/18'), las = 2, mgp = c(3, 0.75, 0))
axis(side = 2, at = seq(0, 25000, 5000), labels = seq(0, 25000, 5000), las = 1, mgp = c(3, 0.75, 0)) 
legend("topright", inset = c(0.01, 0.01), 
       fill = c('grey', 'white'), border = c("grey", "grey"), 
       legend = c("Uploader Count","Video Count"), bg = "white", cex = 0.8)



d_playback = rbind(viewer_count, reqvid_count)
#d,l,u,r
par(mar=c(5, 4, 1, 2))
barpos = barplot(d_playback, beside = TRUE, 
                 ylim = c(0, 20000), axes = FALSE, 
                 main = '', sub = '(b)', xlab = 'Date', ylab = 'Count', names.arg = rep('', 7),
                 col = c('grey', 'white'), border = 'grey')
axis(side = 1, at = c((barpos[2]+barpos[1])/2, (barpos[4]+barpos[3])/2), 
     labels = c('12/12', '12/13'), col = 'white', col.axis = 'red', las = 2, mgp = c(3, 0.75, 0))
axis(side = 1, at = seq((barpos[2]+barpos[1])/2, (barpos[14]+barpos[13])/2, barpos[3]-barpos[1]), 
     labels = c('', '', '12/14', '12/15', '12/16', '12/17', '12/18'), las = 2, mgp = c(3, 0.75, 0))
axis(side = 2, at = seq(0, 15000, 5000), labels = seq(0, 15000, 5000), las = 1, mgp = c(3, 0.75, 0)) 
legend("topright", inset = c(0.01, 0.01), 
       fill = c('grey', 'white'), border = c("grey", "grey"), 
       legend = c("Viewer Count","Request Count"), bg = "white", cex = 0.8)



dev.off()


