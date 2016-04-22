data_c = read.table("/Users/ouyangshuxin/Documents/Youku_HLJ_1504/analysis/7_small_world/c", header=FALSE, sep="\t")
data_l = read.table("/Users/ouyangshuxin/Documents/Youku_HLJ_1504/analysis/7_small_world/l", header=FALSE, sep="\t")

sm_c = data_c$V1
rg_c = data_c$V2
sm_l = data_l$V1
rg_l = data_l$V2

pdf("/Users/ouyangshuxin/Desktop/small_world_candl.pdf", width=8, height=3.5)

par(mfrow=c(1,2))

#d,l,u,r
par(mar=c(5,4,2,2)+0.1)
plot(sm_c,axes=FALSE,xlim=c(1,7),ylim=c(0,0.5), main="",xlab="",ylab="Clustering Coefficient",col="blue")
title(xlab="Dataset Size",mgp=c(3,1,0))
axis(side=1,at=seq(1,7,1),labels=c("1000","2000","3000","4000","5000","6000","10000"),lty=1,las=2)
axis(side=2,at=seq(0,.5,.1),labels=seq(0,.5,.1),las=2,lty=1)
title(sub="(a)",mgp=c(3,1,0))
lines(rg_c,type="p",pch=4,col="red")
box()
legend("topleft",c("User Network","Random Graph"),pch=c(1,4),col=c("blue","red"),bg="white",cex=0.7)

#d,l,u,r
par(mar=c(5,4,2,2)+0.1)
plot(sm_l,axes=FALSE,xlim=c(1,7),ylim=c(0,10), main="",xlab="",ylab="Characteristic Path Length",col="blue")
title(xlab="Dataset Size",mgp=c(3,1,0))
axis(side=1,at=seq(1,7,1),labels=c("1000","2000","3000","4000","5000","6000","10000"),lty=1,las=2)
axis(side=2,at=seq(0,10,2),labels=seq(0,10,2),las=2,lty=1)
title(sub="(b)",mgp=c(3,1,0))
lines(rg_l,type="p",pch=4,col="red")
box()
legend("topleft",c("User Network","Random Graph"),pch=c(1,4),col=c("blue","red"),bg="white",cex=0.7)

dev.off()