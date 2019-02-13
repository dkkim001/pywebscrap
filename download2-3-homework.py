import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

topBannerImg = "https://ssl.pstatic.net/tveta/libs/1224/1224507/d7a648750ced8bbd56b5_20190211150258737.jpg"
rightBannerImg = "https://ssl.pstatic.net/tveta/libs/1224/1224518/defafd026081adccaf47_20190111142049633.png"
rightBannerVideo = "https://tvetamovie.pstatic.net/libs/1225/1225359/9fced2fd1d02be373a34_20190125175345538.mp4-pBASE-v0-f72879-20190125180231563_3.mp4"

savePathTop = "D:/Dev/03.workSpace/section2/down/topBannerImg.jpg"
savePathRight = "D:/Dev/03.workSpace/section2/down/rightBannerImg.jpg"
savePathRight2 = "D:/Dev/03.workSpace/section2/down/rightBannerVideo.mp4"

req.urlretrieve(topBannerImg, savePathTop)
req.urlretrieve(rightBannerImg, savePathRight)
req.urlretrieve(rightBannerVideo, savePathRight2)
