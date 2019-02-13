"""
print ('안녕하세요')

myname="Amy"
print(myname)
print("je m' alle"+ myname)
name=myname*2
print(name)
"""
"""
#자료형
Data type

1.Number 숫자
2.Strings  문자열
3.Lists 리스트
4. Tuples 튜플
5. Dictionary 사전

arithmetc operator 산술 연산자
+
-
*
/
%
** 거듭제곱 5**2 = 25
// 자리 내림 나누셈  5//2 = 2




print (5**2)
"""
"""
#숫자 문자열
qu = '%d first ' %1
m_qu  = ''' second
thred
foru
five %s''' % "---six"
print('\n'*5)
new_string = qu + m_qu
print(new_string)
"""
"""
#배열
las_se = ['sun','mon','tue','wen','tho','fri','tos']
print('monday ',las_se[1])
print(las_se[1:3])
days=['mon','tue','wed']

week =[days, las_se]

print(week[1][1])
las_se.append('Bonjour')

print(week)

las_se.insert(1,"what")
print(week)

las_se.remove('tho')
print(week)
las_se.sort()
print(week)


print(len(las_se))
print(max(las_se))
print(min(las_se))

"""

#튜플
"""
pi_tuple = (3,1,4,1,5,9)
print(pi_tuple)

pi_list=list(pi_tuple)
print(pi_list)
print(tuple(pi_list))
print(list(tuple(pi_list)))


print(len(pi_tuple*2))
"""

#Dictionary
"""
french_week = {'monday' : 'lundi',
               'Tueseday' : 'mardi',
               'Wednesday' : 'merccredi'}

print(french_week['monday'])

print(french_week.keys())

print(french_week.get('monday'))

print(len(french_week))
"""

#조건문
"""
if 조건식:
   문장
else:
    문장
    """

age = 21
if age > 16:
    print("운전 가능하세요")
else:
    print("운전 불가능하세요")
