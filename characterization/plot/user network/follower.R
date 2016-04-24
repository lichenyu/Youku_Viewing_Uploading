workpath = '/Users/ouyangshuxin/Documents/Youku_Watching_Uploading/characterization/'

data = read.table(paste(workpath, 'uploading/follower impact/vid_uid_vc_vv_video_follower', sep = ''))

vc1 = data$V3
vc30 = data$V4
vv_count = data$V5
video_count = data$V6
follower_count = data$V7

idx = which(vc30 > 0)

level = ceiling(log10(vc30[idx]))
per_video = 1 / (video_count[idx] + 1)

fit = lm(level ~ vv_count[idx] + per_video + follower_count[idx])
summary(fit)

level[1:10]
round(fit$fitted.values[1:10])



plot(fit)

a = vv_count[idx]/(video_count[idx]+1)
fit = lm(log10(vc[idx]) ~ a + follower_count[idx])
summary(fit)

plot(ecdf(fit$residuals), xlim = c(-1, 1))

which(fit$residuals < -20)

fit$residuals[41875]
log10(vc[41875])
vv_count[41875]
video_count[41875]
follower_count[41875]
fit$fitted.values[41875]

fit$residuals[41876]
log10(vc[41876])
vv_count[41876]
video_count[41876]
follower_count[41876]
fit$fitted.values[41876]

# pdf(paste(workpath, "plot/follower impact/vc.pdf", sep = ''), 
#     width = 10, height = 4)
# par(mfrow = c(1, 2), cex = 1)
# 
# 
# 
# uploading_vc_p = uploading_vc[which(uploading_vc > 0)]
# uploading_vc_p_sorted = sort(uploading_vc_p, decreasing = TRUE)
# rank_uploading = seq(1, length(uploading_vc_p_sorted))
# x_uploading = log10(rank_uploading)
# y_uploading = log10(uploading_vc_p_sorted)
# #d,l,u,r
# par(mar=c(5, 4, 1, 2))
# plot(x_uploading, y_uploading, 
#      axes = FALSE, xaxs="i",yaxs="i", xlim = c(0, 5.5), ylim = c(0, 8.5), 
#      main = '', sub = '(a)', xlab = 'Rank', ylab = 'View Count')
# axis(side = 1, at = seq(0, 5.5, 1), labels = seq(0, 5.5, 1), las = 1)
# axis(side = 2, at = seq(0, 8, 2), labels = seq(0, 8, 2), las = 1)
# legend("bottomleft", 
#        pch = c(1, NA), lty = c(NA, 1), lwd = c(NA, 4), col = c('black', 'red'), 
#        legend = c('Empirical', 'Zipf'), bg = "white", cex = 0.8)
# box()
# x_uploading_1 = x_uploading[which(x_uploading < 4.5)]
# y_uploading_1 = y_uploading[which(x_uploading < 4.5)]
# fit = lm(y_uploading_1 ~ x_uploading_1)
# abline(fit$coefficients[1], fit$coefficients[2], lwd = 4, col = 'red')
# 
# 
# 
# playback_vc_sorted = sort(playback_vc, decreasing = TRUE)
# rank_playback = seq(1, length(playback_vc_sorted))
# x_playback = log10(rank_playback)
# y_playback = log10(playback_vc_sorted)
# #d,l,u,r
# par(mar=c(5, 4, 1, 2))
# plot(x_playback, y_playback, 
#      axes = FALSE, xaxs="i",yaxs="i", xlim = c(0, 5.5), ylim = c(0, 9), 
#      main = '', sub = '(b)', xlab = 'Rank', ylab = 'View Count')
# axis(side = 1, at = seq(0, 5.5, 1), labels = seq(0, 5.5, 1), las = 1)
# axis(side = 2, at = seq(0, 8, 2), labels = seq(0, 8, 2), las = 1)
# legend("bottomleft", 
#        pch = c(1, NA), lty = c(NA, 1), lwd = c(NA, 4), col = c('black', 'red'), 
#        legend = c('Empirical', 'Zipf + Exponential Cutoff'), bg = "white", cex = 0.8)
# box()
# x_playback_1 = x_playback[which(x_playback < 4)]
# y_playback_1 = y_playback[which(x_playback < 4)]
# fit = lm(y_playback_1 ~ x_playback_1)
# x = seq(0, 4, 0.01)
# lines(x, fit$coefficients[1] + fit$coefficients[2] * x, 
#       type = 'l', lwd = 4, col = 'red')
# x_playback_2 = x_playback[which(x_playback >= 4)]
# y_playback_2 = y_playback[which(x_playback >= 4)]
# temp = data.frame(x_playback_2, y_playback_2)
# f = nls(y_playback_2 ~ a * exp(b * x_playback_2) + c, temp, list(a = -3.123e-11,
#                                                                  b = 5.156e+00, 
#                                                                  c = 7.104e+00))
# x = seq(4, 5.05, 0.0001)
# lines(x, f$m$getAllPars()[1] * exp( f$m$getAllPars()[2] * x) + f$m$getAllPars()[3], 
#       type = 'l', lwd = 4, col = 'red')
# 
# 
# 
# dev.off()
# 
# 
