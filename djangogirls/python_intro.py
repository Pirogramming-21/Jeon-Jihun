# 문자열
print("Hi there" + "01a")
print("01a" * 3)
print("Runnin' down the hill")
print("ola".upper())

# 오류
print(len(str(304023)))

# 변수
name = "Ola"
print(name)
name = "Sonja"
print(name)

# print() 함수
print(name)

# 리스트
lottery = [3, 42, 12, 19, 30, 59]
print(len(lottery))
lottery.sort()
lottery.reverse()
lottery.append()
print(lottery)
print(lottery[0])
lottery.pop(0)
print(lottery)

# 딕셔너리
participant = {"name": "Ola", "country": "Poland", "favorite_numbers": [7, 42, 92]}
print(participant["name"])
participant["favorite_language"] = "Python"
participant.pop("favorite_numbers")
participant["country"] = "Germany"
print(participant)

# 비교
print(5 > 2)
print(3 < 1)
print(5 > 2 * 2)
print(1 == 1)
print(5 != 2)

print(6 > 2 and 2 < 3)
print(3 > 2 and 2 < 1)
print(3 > 2 or 2 < 1)

# 불리언
print(True and True)
print(False and True)
print(True or 1 == 1)
print(1 != 2)

# if else
if 3 > 2:
    print("It works!")

if 5 < 2:
    print("5 is indeed greater than 2")
else:
    print("5 is not greater than 2")

name = "Sonja"
if name == "Ola":
    print("Hey Ola!")
elif name == "Sonja":
    print("Hey Sonja!")
else:
    print("Hey anonymous!")

volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("My ears are hurting! :(")


# 나만의 함수 만들기
def hi():
    print("Hi there!")
    print("How are you?")


hi()


def hi(name):
    if name == "Ola":
        print("Hi Ola!")
    elif name == "Sonja":
        print("Hi Sonja!")
    else:
        print("Hi anonymous!")


hi("Ola")
hi("Sonja")


def hi(name):
    print("Hi " + name + "!")


hi("Rachel")

# 반복하기


def hi(name):
    print("Hi " + name + "!")


girls = ["Rachel", "Monica", "Phoebe", "Ola", "You"]
for name in girls:
    hi(name)
    print("Next girl")

for i in range(1, 6):
    print(i)
