workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/characterization/'

uploadercount_20151212 = read.table(paste(workpath, 'uploading/time_vid/time_uploadercount_2015-12-12', sep = ''))
uploadercount_20151213 = read.table(paste(workpath, 'uploading/time_vid/time_uploadercount_2015-12-13', sep = ''))
uploadercount_20151214 = read.table(paste(workpath, 'uploading/time_vid/time_uploadercount_2015-12-14', sep = ''))
uploadercount_20151215 = read.table(paste(workpath, 'uploading/time_vid/time_uploadercount_2015-12-15', sep = ''))
uploadercount_20151216 = read.table(paste(workpath, 'uploading/time_vid/time_uploadercount_2015-12-16', sep = ''))
uploadercount_20151217 = read.table(paste(workpath, 'uploading/time_vid/time_uploadercount_2015-12-17', sep = ''))
uploadercount_20151218 = read.table(paste(workpath, 'uploading/time_vid/time_uploadercount_2015-12-18', sep = ''))

upvidcount_20151212 = read.table(paste(workpath, 'uploading/time_vid/time_vidcount_2015-12-12', sep = ''))
upvidcount_20151213 = read.table(paste(workpath, 'uploading/time_vid/time_vidcount_2015-12-13', sep = ''))
upvidcount_20151214 = read.table(paste(workpath, 'uploading/time_vid/time_vidcount_2015-12-14', sep = ''))
upvidcount_20151215 = read.table(paste(workpath, 'uploading/time_vid/time_vidcount_2015-12-15', sep = ''))
upvidcount_20151216 = read.table(paste(workpath, 'uploading/time_vid/time_vidcount_2015-12-16', sep = ''))
upvidcount_20151217 = read.table(paste(workpath, 'uploading/time_vid/time_vidcount_2015-12-17', sep = ''))
upvidcount_20151218 = read.table(paste(workpath, 'uploading/time_vid/time_vidcount_2015-12-18', sep = ''))

viewercount_20151212 = read.table(paste(workpath, 'playback/time_request/time_viewercount_20151212', sep = ''))
viewercount_20151213 = read.table(paste(workpath, 'playback/time_request/time_viewercount_20151213', sep = ''))
viewercount_20151214 = read.table(paste(workpath, 'playback/time_request/time_viewercount_20151214', sep = ''))
viewercount_20151215 = read.table(paste(workpath, 'playback/time_request/time_viewercount_20151215', sep = ''))
viewercount_20151216 = read.table(paste(workpath, 'playback/time_request/time_viewercount_20151216', sep = ''))
viewercount_20151217 = read.table(paste(workpath, 'playback/time_request/time_viewercount_20151217', sep = ''))
viewercount_20151218 = read.table(paste(workpath, 'playback/time_request/time_viewercount_20151218', sep = ''))

reqcount_20151212 = read.table(paste(workpath, 'playback/time_request/time_reqcount_20151212', sep = ''))
reqcount_20151213 = read.table(paste(workpath, 'playback/time_request/time_reqcount_20151213', sep = ''))
reqcount_20151214 = read.table(paste(workpath, 'playback/time_request/time_reqcount_20151214', sep = ''))
reqcount_20151215 = read.table(paste(workpath, 'playback/time_request/time_reqcount_20151215', sep = ''))
reqcount_20151216 = read.table(paste(workpath, 'playback/time_request/time_reqcount_20151216', sep = ''))
reqcount_20151217 = read.table(paste(workpath, 'playback/time_request/time_reqcount_20151217', sep = ''))
reqcount_20151218 = read.table(paste(workpath, 'playback/time_request/time_reqcount_20151218', sep = ''))



x = seq(0, 23) + 0.5

uploadercount = c(uploadercount_20151212[, 2] +  
                  uploadercount_20151213[, 2] + 
                  uploadercount_20151214[, 2] + 
                  uploadercount_20151215[, 2] + 
                  uploadercount_20151216[, 2] + 
                  uploadercount_20151217[, 2] + 
                  uploadercount_20151218[, 2])

upvidcount = c(upvidcount_20151212[, 2] + 
               upvidcount_20151213[, 2] + 
               upvidcount_20151214[, 2] + 
               upvidcount_20151215[, 2] + 
               upvidcount_20151216[, 2] + 
               upvidcount_20151217[, 2] + 
               upvidcount_20151218[, 2])

viewercount = c(viewercount_20151212[, 2] + 
                viewercount_20151213[, 2] + 
                viewercount_20151214[, 2] + 
                viewercount_20151215[, 2] + 
                viewercount_20151216[, 2] + 
                viewercount_20151217[, 2] + 
                viewercount_20151218[, 2])

reqcount = c(reqcount_20151212[, 2] + 
             reqcount_20151213[, 2] + 
             reqcount_20151214[, 2] + 
             reqcount_20151215[, 2] + 
             reqcount_20151216[, 2] + 
             reqcount_20151217[, 2] + 
             reqcount_20151218[, 2])



pdf(paste(workpath, "plot/user activity/24h.pdf", sep = ''), 
    width = 5, height = 6)
par(mfrow = c(2, 1), cex = 1)



cols = rainbow(4)
#d,l,u,r
par(mar=c(0, 4, 4, 2))
plot(x, uploadercount, 
     axes = FALSE, ylim = c(0, 12000), 
     main = '', sub = '', xlab = '', ylab = 'Count', 
     type = 'l', col = cols[1], lwd = 2)
lines(x, upvidcount, type = 'l', col = cols[2], lwd = 2)
axis(side = 3, at = seq(0, 23), 
     labels = c('0:00', '1:00', '2:00', '3:00', '4:00', '5:00', 
                '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', 
                '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', 
                '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'), las = 2, tck = 1, lty = 2, col = 'grey', mgp = c(3, 0.75, 0))
axis(side = 2, at = seq(0, 12000, 4000), labels = seq(0, 12000, 4000), las = 1, mgp = c(3, 0.75, 0))
legend("topleft", inset = c(0.01, 0.01), 
       lty = c(1, 1), lwd = c(2, 2), col = c(cols[1], cols[2]), 
       legend = c("Uploader Count","Video Count"), bg = "white", cex = 0.8)
box()
#d,l,u,r
par(mar=c(4, 4, 0, 2))
plot(x, viewercount, 
     axes = FALSE, ylim = c(0, 8000), 
     main = '', sub = '', xlab = 'Time of Day', ylab = 'Count', 
     type = 'l', col = cols[3], lwd = 2)
lines(x, reqcount, type = 'l', col = cols[4], lwd = 2)
axis(side = 1, at = seq(0, 23), 
     labels = c('0:00', '1:00', '2:00', '3:00', '4:00', '5:00', 
                '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', 
                '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', 
                '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'), las = 2, tck = 1, lty = 2, col = 'grey', mgp = c(3, 0.75, 0))
axis(side = 2, at = seq(0, 8000, 2000), labels = seq(0, 8000, 2000), las = 1, mgp = c(3, 0.75, 0))
legend("topleft", inset = c(0.01, 0.01), 
       lty = c(1, 1), lwd = c(2, 2), col = c(cols[3], cols[4]), 
       legend = c("Viewer Count","Request Count"), bg = "white", cex = 0.8)
box()



dev.off()


