import sys
import io
import urllib.request as dw

imgUrl = "https://post-phinf.pstatic.net/MjAxNzExMTZfOTkg/MDAxNTEwODMxMTM3MTA2.gQKb8PKAXGUOd4fh-_n93pM8AE5Z1gpXmwBVEFYui2Eg.fwN0R68oKR8gwDdciPfxmo9K5HalsXlUc-JUbCIiIWQg.PNG/005-20171116.png?type=w1200"
htmlUrl = "http://google.com"

savePath1 = "D:/Dev/03.workSpace/section2/test1.jpg"
savePath2 = "D:/Dev/03.workSpace/section2/index.html"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlUrl).read()

saveFile1 = open(savePath1, 'wb')  # w : write, r : read, a : add b: binary
saveFile1.write(f)
saveFile1.close()

with open(savePath2, 'wb') as saveFile2:
    saveFile2.write(f2)

print("다운로드 완료!")

#urlretrieve :    바로 저장할때 쓰임!    파싱하여 저장하는 경로 : 저장 -> open('r') -> 변수에할당 - > 파싱 -> 저장

#urlopen :    필요로 하는 데이터를 파씽할때 쓰임!   파싱하여 저장하는 경로 변수 할당 -> 파씽 -> 저장
#with   자동으로 close 까지 해줌
