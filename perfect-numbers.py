def check_perfect_number(num):
    sum_div = 0
    for i in range(1, num): if(num % i == 0): sum_div += i
    return True if (sum_div == num) else return False