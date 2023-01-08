def input_mark():
    print("Enter Student's ID: ")
    ID = int(input())
    print("Enter exam number: ")
    exam = int(input())
    print("Enter all test scores: ")
    Mark1 = int(input())
    Mark2 = int(input())
    Mark3 = int(input())
    Mark4 = int(input())
    Mark5 = int(input())

    sum1 = Mark1 + Mark2 + Mark3 + Mark4 + Mark5

    avg = sum1 / 5

    print("Your test average is: " + str(avg))
    print("Final mark is: ", computer_mark(avg))
    print("Exam Number", exam)
    print("Letter grade is: ", get_grade(computer_mark(avg)))
    print(print_Remark(get_grade(computer_mark(avg))))

    return avg


def computer_mark(avg):
    final_mark = 0.2 * avg + 0.4
    return final_mark


def get_grade(final_mark):
    if 90 <= final_mark <= 100:
        grade = "A"
    elif 80 <= final_mark <= 89:
        grade = "B"
    elif 70 <= final_mark <= 79:
        grade = "C"
    elif 60 <= final_mark <= 69:
        grade = "D"
    elif 50 <= final_mark <= 59:
        grade = "E"
    elif 0 <= final_mark <= 49:
        grade = "F"
        return grade


def print_Remark(grade):
    if grade == "A":
        print("Remarks= Excellent performance")
    if grade == "B":
        print("Remarks= Great performance")
    if grade == "C":
        print("Remarks= Very good performance")
    if grade == "D":
        print("Remarks= Good performance")
    if grade == "E":
        print("Remarks= Try more performance")
    if grade == "F":
        print("Remarks= Very poor performance")
        return


input_mark()
