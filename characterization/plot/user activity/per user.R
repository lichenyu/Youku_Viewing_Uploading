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



# per user activity
upvid_count = rbind(uploader_vidcount_20151212[2], 
                    uploader_vidcount_20151213[2], 
                    uploader_vidcount_20151214[2], 
                    uploader_vidcount_20151215[2], 
                    uploader_vidcount_20151216[2], 
                    uploader_vidcount_20151217[2], 
                    uploader_vidcount_20151218[2])
reqvid_count = rbind(viewer_reqcount_20151212[2], 
                     viewer_reqcount_20151213[2], 
                     viewer_reqcount_20151214[2], 
                     viewer_reqcount_20151215[2], 
                     viewer_reqcount_20151216[2], 
                     viewer_reqcount_20151217[2], 
                     viewer_reqcount_20151218[2])



pdf(paste(workpath, "plot/user activity/per user.pdf", sep = ''), 
    width = 5, height = 4)



cdf_upvid = ecdf(upvid_count[, 1])
#d,l,u,r
par(mar=c(5, 4, 1, 2))
plot(cdf_upvid, verticals = TRUE, do.points = FALSE, col.01line = NULL, 
     axes = FALSE, xaxs="i",yaxs="i", xlim = c(0, 10), ylim = c(0, 1), 
     main = '', sub = '', xlab = 'Count', ylab = 'CDF', 
     lwd = 2, col = 'blue')
cdf_reqvid = ecdf(reqvid_count[, 1])
lines(cdf_reqvid, verticals = TRUE, do.points = FALSE, col.01line = NULL, lwd = 2, col = 'red')
axis(side = 1, at = seq(0, 10, 1), labels = seq(0, 10, 1), las = 1, tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, 0.1), labels = seq(0, 1, 0.1), las = 1, tck = 1, lty = 2, col = 'grey')
legend("bottomright", 
       lwd = c(2, 2), col = c('blue', 'red'), 
       legend = c("Video Count per Uploader","Request Count per Viewer"), bg = "white", cex = 0.8)
box()



dev.off()


