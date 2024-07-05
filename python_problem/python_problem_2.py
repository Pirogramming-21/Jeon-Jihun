#학생 정보를 저장할 변수 초기화
students_info = []
students_name = []

#함수 이름은 변경 가능합니다.

##############  menu 1
def Menu1(info):
    #사전에 학생 정보 저장하는 코딩
    students_info.append(info)
    students_name.append(info[0])

##############  menu 2
def Menu2() :
    #학점 부여 하는 코딩
    for i in students_info:
        if len(i) != 4:
            avg_score = (int(i[1])+int(i[2]))/2
            if avg_score >= 90:
                i.append("A")
            elif avg_score >= 80:
                i.append("B")
            elif avg_score >= 70:
                i.append("C")
            else:
                i.append("D")
            

##############  menu 3
def Menu3(info) :
    #출력 코딩
    print("----------------------------------")
    print("name  mid  final  grade")
    print("----------------------------------")
    for student_info in info:
        print(f'{student_info[0]}    {student_info[1]}   {student_info[2]}   {student_info[3]}')
    
##############  menu 4
def Menu4(del_name):
    #학생 정보 삭제하는 코딩
    for index in range(len(students_info)):
        if students_info[index][0] == del_name:
            del students_info[index]
            del students_name[index]
            break

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")

while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

        info = list(input('Enter name mid-score final-score: ').split())

        if len(info) != 3:
            print('Num of data is not 3!')
        elif (float(info[1]).is_integer() and float(info[2]).is_integer() and float(info[1]) >=0 and float(info[2]) >=0) != True:
            print('Score is not positive integer!')
        elif info[0] in students_name:
            print('Already exist name!')
        else:
            Menu1(info)
        
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        if len(students_info) == 0:
            print('No student data!')
        else:
            Menu2()
            print("Grading to all students.")


    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        if len(students_info) == 0:
            print('No student data!')
            continue

        error = False   
        for info in students_info:
            if len(info) != 4:
                print("There is a student who didn't get grade.")
                error = True
                continue
        
        if error:
            continue
        else: 
            Menu3(students_info)

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        if len(students_info) == 0:
            print('No student data!')
            continue
        
        del_name = input('Enter the name to delete: ')
        if del_name not in students_name:
            print('Not exist name!')
            continue
        
        Menu4(del_name)
        print(del_name,"student information is deleted.")


    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit Program!")
        break

    else :
        #"Wrong number. Choose again." 출력
        print("Wrong number, Choose again.")