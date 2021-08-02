#Question 1
def hello_name(user_name):
    print("hello " + user_name.title() + " !")


#Question 2
def odd_numbers():
    for number in range(1,100,2):
        print(number)


#Question 3
def max_num(a_list):
    print(max(a_list))


#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        return True
    elif a_year % 400 == 0:
        return True
    else :
        return False


#Question 5
def is_consecutive(a_list):
    a = a_list[0] - 1
    for num in a_list:
        if num == a + 1:
            num = a
            return True
        else:
            return False


