#Camryn Moschitta
#CS175L

#expensePieChart
import matplotlib.pyplot as plt

def read_File(filename):
    expenses={}
    with open(filename,'r') as file:
        for line in file:
            val,label=line.strip().split("\t")
            try:
                expenses[val]=int(label)
            except ValueError:
                print(f'Removing {val} and {label}')
    return expenses
        
def make_Pie_Chart(expenses):
    types=expenses.keys()
    sale=expenses.values()
    plt.subplots()
    plt.pie(sale, labels=types, autopct='%1.1f%%', startangle=0)
    plt.axis('equal')
    plt.title('Monthly Expenses')
    plt.show()

def main():
    try:
        expenses=read_File('expenses.txt')
        make_Pie_Chart(expenses)
    except IOError:
        print('Your file could not be found!')
    except ValueError:
        print('Unexpected character found')    

if __name__ == '__main__':
    main()
