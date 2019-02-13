import sys
import io
import urllib.request as dw

imgUrl = "https://post-phinf.pstatic.net/MjAxNzExMTZfOTkg/MDAxNTEwODMxMTM3MTA2.gQKb8PKAXGUOd4fh-_n93pM8AE5Z1gpXmwBVEFYui2Eg.fwN0R68oKR8gwDdciPfxmo9K5HalsXlUc-JUbCIiIWQg.PNG/005-20171116.png?type=w1200"
htmlUrl = "http://google.com"

savePath1 = "D:/Dev/03.workSpace/section2/test1.jpg"
savePath2 = "D:/Dev/03.workSpace/section2/index.html"

dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlUrl, savePath2)

print("다운로드 완료!")
