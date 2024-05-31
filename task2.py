import pandas as pd
from datetime import datetime

# Initialize the CSV file if it doesn't exist
try:
    expenses = pd.read_csv('expenses.csv')
except FileNotFoundError:
    expenses = pd.DataFrame(columns=['Date', 'Category', 'Description', 'Amount'])
    expenses.to_csv('expenses.csv', index=False)

def add_expense():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    category = input('Enter the category: ')
    description = input('Enter the description: ')
    amount = float(input('Enter the amount: '))
    
    new_expense = pd.DataFrame({
        'Date': [date],
        'Category': [category],
        'Description': [description],
        'Amount': [amount]
    })

    global expenses
    expenses = pd.concat([expenses, new_expense], ignore_index=True)
    expenses.to_csv('expenses.csv', index=False)
    print('Expense added successfully!')

def view_expenses():
    print(expenses)

def summarize_expenses():
    summary = expenses.groupby('Category')['Amount'].sum().reset_index()
    print(summary)

def main():
    while True:
        print('\nExpense Tracker Menu')
        print('1. Add an Expense')
        print('2. View All Expenses')
        print('3. Summarize Expenses by Category')
        print('4. Exit')
        
        choice = input('Enter your choice: ')
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            summarize_expenses()
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
