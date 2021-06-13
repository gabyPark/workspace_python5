# test13.py

# 파일 입출력

# open("파일명","모드") 내장함수
# w - 파일쓰기, r - 파일읽기, a - 파일수정 (파일에 추가 append)

f = open("test.txt","r")
# print(f)

# 인코딩 문제가 있어서 한글 말고 영어로 기록하기!
# 해당 파일의 내용 첫줄만 읽어오기
print(f.readline())

while True:
    line = f.readline()

    if not line:
        break

    print(line)

# 입출력 다 쓰고나면 무조건 자원해제!!!
f.close()

###################################################

f2 = open("test.txt","r")

# print(f2.readlines())   # 파일의 내용을 리스트로 읽어오기

for i in f2.readlines():
    print(i)

f2.close()

###################################################
print("-"*50)

f3 = open("birth.csv","r")

for a in f3.readlines():
    print(a)

f3.close()
###################################################
print("-"*50)

# 이미지 파일 X
# f4 = open("sushi1.JPG","r")
# for a in f4.readlines():
#     print(a)
#
# f4.close()

f4 = open("test.txt","r")
print(f4.read())
f4.close()

print("파일 쓰기 ---------------------------------")
# 기본적으로 덮어쓰기 (주의))

f5 = open("fileTest.txt","w")

data = "itwill busan"

for i in range(0,len(data)):
    # print(data[i])
    f5.write(data[i])

f5.close()


# 파일 쓰기 => 특정 위치에 파일을 생성
f6 = open("D:/JSP/fileTest1.txt","w")

for i in range(1,6):
    f6.write(" %d 입력 \n" % i)

f6.close()


# 파일에 내용 추가
f7 = open("test.txt","a")
f7.write("hello")
f7.close()


