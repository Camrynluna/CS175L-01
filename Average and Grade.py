#Camryn Moschitta
#CS175L

#Calculate average and grade with functions



def determine_grade(total):
    if total<=100 and total>=90:
        return 'A'
    elif total<=89 and total>=80:
        return 'B'
    elif total<=79 and total>=70:
        return 'C'
    elif total<=69 and total>=60:
        return 'D'
    else:
        return'F'

def calc_average():
    answer1=float(input("Enter score 1: "))
    answer2=float(input("Enter score 2: "))
    answer3=float(input("Enter score 3: "))
    answer4=float(input("Enter score 4: "))
    answer5=float(input("Enter score 5: "))
    avg=(answer1+answer2+answer3+answer4+answer5)/5
    return answer1, answer2, answer3, answer4, answer5, avg

def main():
    repeat='yes'
    while repeat=='yes':
        answer1, answer2, answer3, answer4, answer5, avg=calc_average()
        determine_grade(answer1)
        determine_grade(answer2)
        determine_grade(answer3)
        determine_grade(answer4)
        determine_grade(answer5)
        print(f'{"Score":<15}',f'{"Numeric Grade Letter Grade"}')
        print("-------------------------------------------")
        print(f'{"Score 1:":<15}',f'{answer1:<13}',f'{determine_grade(answer1)}')
        print(f'{"Score 2:":<15}',f'{answer2:<13}',f'{determine_grade(answer2)}')
        print(f'{"Score 3:":<15}',f'{answer3:<13}',f'{determine_grade(answer3)}')
        print(f'{"Score 4:":<15}',f'{answer4:<13}',f'{determine_grade(answer4)}')
        print(f'{"Score 5:":<15}',f'{answer5:<13}',f'{determine_grade(answer5)}')
        print(f'{"Average score:":<15}',f'{avg:<13}',f'{determine_grade(avg)}')
        repeat=input("Enter 'yes' if you would like to do another calculation: ")

main()

