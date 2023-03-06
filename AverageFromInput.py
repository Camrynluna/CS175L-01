#Camryn Moschitta
#CS175L

#AverageFromInput

def main():
    try:
        outfile=open('numbers.txt', 'r')

        num1 = int(outfile.readline())
        num2 = int(outfile.readline())
        num3 = int(outfile.readline())


        for num in range(1,4,3):
            avg=(num1+num2+num3)/3
            total=num1
            total2=num2+total
            total3=num3+total2
            print(f'{"I read in 1 number(s) Current number is:":<43} {num1:.2f} {"Total is:":<12} {total:.2f}')
            print(f'{"I read in 2 number(s) Current number is:":<43} {num2:.2f} {"Total is:":<12} {total2:.2f}')
            print(f'{"I read in 3 number(s) Current number is:":<42} {num3:.2f} {"Total is:":<11} {total3:.2f}')
            print(f'Average: {avg:.1f}')

    except IOError:
        print('An error occured. File not found')
    except ValueError:
        print('The file does not contain a numerical value')
    except:
        print('An error occured')
            
if __name__ == '__main__':
    main()
