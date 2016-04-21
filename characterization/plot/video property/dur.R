workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/characterization/'

uploading_dur = read.table(paste(workpath, 'uploading/video property/dur', sep = ''))$V1
playback_dur = read.table(paste(workpath, 'playback/video property/dur', sep = ''))$V1



pdf(paste(workpath, "plot/video property/dur.pdf", sep = ''), 
    width = 5, height = 4)



cdf_uploading_dur = ecdf(uploading_dur)
cdf_playback_dur = ecdf(playback_dur)
#d,l,u,r
par(mar=c(5, 4, 1, 2))
plot(cdf_uploading_dur, verticals = TRUE, do.points = FALSE, col.01line = NULL, 
     axes = FALSE, xaxs="i",yaxs="i", xlim = c(0, 3600), ylim = c(0, 1), 
     main = '', sub = '', xlab = 'Video Duration (minutes)', ylab = 'CDF', 
     lwd = 2, col = 'blue')
lines(cdf_playback_dur, verticals = TRUE, do.points = FALSE, col.01line = NULL, lwd = 2, col = 'red')
axis(side = 1, at = seq(0, 3600, 600), labels = seq(0, 3600, 600), las = 1, tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, 0.1), labels = seq(0, 1, 0.1), las = 1, tck = 1, lty = 2, col = 'grey')
legend("bottomright", 
       lwd = c(2, 2), col = c('blue', 'red'), 
       legend = c('Uploaded Videos', 'Viewed Videos'), bg = "white", cex = 0.8)
box()



dev.off()


