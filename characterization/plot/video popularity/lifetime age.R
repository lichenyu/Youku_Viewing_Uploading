workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/characterization/'

uploading_lifetime = read.table(paste(workpath, 'uploading/video lifetime/lifetime', sep = ''))$V2
playback_age = read.table(paste(workpath, 'playback/video age/age', sep = ''))$V1



pdf(paste(workpath, "plot/video popularity/lifetime age.pdf", sep = ''), 
    width = 10, height = 4)
par(mfrow = c(1, 2), cex = 1)



cdf_uploading_lifetime = ecdf(uploading_lifetime)
#d,l,u,r
par(mar=c(5, 4, 1, 2))
plot(cdf_uploading_lifetime, verticals = TRUE, do.points = FALSE, col.01line = NULL, 
     axes = FALSE, xaxs="i",yaxs="i", xlim = c(0, 30), ylim = c(0, 1), 
     main = '', sub = '(a)', xlab = 'Uploaded Video Lifetime (days)', ylab = 'CDF', 
     lwd = 2, col = 'blue')
axis(side = 1, at = seq(0, 30, 5), labels = seq(0, 30, 5), las = 1, tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, 0.1), labels = seq(0, 1, 0.1), las = 1, tck = 1, lty = 2, col = 'grey')
box()

cdf_playback_age = ecdf(playback_age)
#d,l,u,r
par(mar=c(5, 4, 1, 2))
plot(cdf_playback_age, verticals = TRUE, do.points = FALSE, col.01line = NULL, 
     axes = FALSE, xaxs="i",yaxs="i", xlim = c(0, 1080), ylim = c(0, 1), 
     main = '', sub = '(b)', xlab = 'Viewed Video Age (months)', ylab = 'CDF', 
     lwd = 2, col = 'blue')
axis(side = 1, at = seq(0, 1080, 180), labels = seq(0, 1080, 180)/30, las = 1, tck = 1, lty = 2, col = 'grey')
axis(side = 2, at = seq(0, 1, 0.1), labels = seq(0, 1, 0.1), las = 1, tck = 1, lty = 2, col = 'grey')
box()



dev.off()


