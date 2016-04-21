datapath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/data/'
workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/characterization/'

uploading_vc = read.table(paste(datapath, 'uploading/clean/view count clean/vc', sep = ''))$V31
playback_vc = read.table(paste(workpath, 'playback/video viewcount/vc', sep = ''))$V1



uploading_vc_p = uploading_vc[which(uploading_vc > 0)]
uploading_vc_p_sorted = sort(uploading_vc_p, decreasing = TRUE)
rank_uploading = seq(1, length(uploading_vc_p_sorted))
x_uploading = log10(rank_uploading)
y_uploading = log10(uploading_vc_p_sorted)
#d,l,u,r
par(mar=c(5, 4, 1, 2))
plot(x_uploading, y_uploading)
x_uploading_1 = x_uploading[which(x_uploading < 4.5)]
y_uploading_1 = y_uploading[which(x_uploading < 4.5)]
fit = lm(y_uploading_1 ~ x_uploading_1)
abline(fit$coefficients[1], fit$coefficients[2], lwd = 2, col = 'red')



playback_vc_sorted = sort(playback_vc, decreasing = TRUE)
rank_playback = seq(1, length(playback_vc_sorted))
x_playback = log10(rank_playback)
y_playback = log10(playback_vc_sorted)
#d,l,u,r
par(mar=c(5, 4, 1, 2))
plot(x_playback, y_playback)

x_playback_1 = x_playback[which(x_playback < 4)]
y_playback_1 = y_playback[which(x_playback < 4)]
fit = lm(y_playback_1 ~ x_playback_1)
x = seq(0, 4, 0.01)
lines(x, fit$coefficients[1] + fit$coefficients[2] * x, 
      type = 'l', lwd = 2, col = 'red')

x_playback_2 = x_playback[which(x_playback >= 4)]
y_playback_2 = y_playback[which(x_playback >= 4)]
temp = data.frame(x_playback_2, y_playback_2)
f = nls(y_playback_2 ~ a * exp(b * x_playback_2) + c, temp, list(a = -3.123e-11,
                                                                 b = 5.156e+00, 
                                                                 c = 7.104e+00))
#summary(f)
x = seq(4, 5.05, 0.0001)
lines(x, f$m$getAllPars()[1] * exp( f$m$getAllPars()[2] * x) + f$m$getAllPars()[3], 
      type = 'l', lwd = 2, col = 'red')





# pdf(paste(workpath, "plot/video popularity/vc.pdf", sep = ''), 
#     width = 10, height = 4)
# par(mfrow = c(1, 2), cex = 1)
# 
# 
# 
# cdf_uploading_lifetime = ecdf(uploading_lifetime)
# #d,l,u,r
# par(mar=c(5, 4, 1, 2))
# plot(cdf_uploading_lifetime, verticals = TRUE, do.points = FALSE, col.01line = NULL, 
#      axes = FALSE, xaxs="i",yaxs="i", xlim = c(0, 30), ylim = c(0, 1), 
#      main = '', sub = '(a)', xlab = 'Uploaded Video Lifetime (days)', ylab = 'CDF', 
#      lwd = 2, col = 'blue')
# axis(side = 1, at = seq(0, 30, 5), labels = seq(0, 30, 5), las = 1, tck = 1, lty = 2, col = 'grey')
# axis(side = 2, at = seq(0, 1, 0.1), labels = seq(0, 1, 0.1), las = 1, tck = 1, lty = 2, col = 'grey')
# box()
# 
# cdf_playback_age = ecdf(playback_age)
# #d,l,u,r
# par(mar=c(5, 4, 1, 2))
# plot(cdf_playback_age, verticals = TRUE, do.points = FALSE, col.01line = NULL, 
#      axes = FALSE, xaxs="i",yaxs="i", xlim = c(0, 1080), ylim = c(0, 1), 
#      main = '', sub = '(b)', xlab = 'Viewed Video Age (months)', ylab = 'CDF', 
#      lwd = 2, col = 'blue')
# axis(side = 1, at = seq(0, 1080, 180), labels = seq(0, 1080, 180)/30, las = 1, tck = 1, lty = 2, col = 'grey')
# axis(side = 2, at = seq(0, 1, 0.1), labels = seq(0, 1, 0.1), las = 1, tck = 1, lty = 2, col = 'grey')
# box()
# 
# 
# 
# dev.off()
# 
# 
