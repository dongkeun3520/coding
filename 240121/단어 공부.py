


word = input().lower()   ## 소문자로 불러오기
word_list = list(set(word))  ## 중복 제거후 리스트 만들기
cnt = []

for i in word_list:
    count = word.count(i)   
    cnt.append(count)

if cnt.count(max(cnt)) >=2:
    print("?")

else:
    print(word_list[(cnt.index(max(cnt)))].upper())