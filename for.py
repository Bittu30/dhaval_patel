def ex_expense_break():
    monthly_list = ['January', 'February', 'March', 'April', 'May']
    expense_list = [2340, 2500, 2100, 3100, 2980]
    e = input("Enter expense amount")
    e = int(e)

    month = -1
    for i in range(len(expense_list)):
        if e == expense_list[i]:
            month = i
            break
    if month != -1:
        print('You spent', e, 'in', monthly_list[month])
    else:
        print('You did not spend', e, 'in any month')


def ex_print_shape():
    for i in range(1, 6):
        s = ''
        for j in range(i):
            s += '*'
        print(s)


def ex_heads_tails():
    result = ['head', 'tail', 'head', 'tail', 'head']
    count = 0
    for item in result:
        if item == 'head':
            count += 1
    print('Head count:', count)


def demo_break_marathon():
    for i in range(26):
        print('you ran ', i + 1, ' miles')
        tired = input('are you tired?')
        if tired == 'yes':
            break

    if i == 26:
        print("Hurray! You are a rock star! you jsut finished marathon")
    else:
        print('No worry it was a great try')


def demo_continue():
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i * i)


ex_expense_break()

ex_print_shape()

ex_heads_tails()

#demo_break_marathon()

demo_continue()
