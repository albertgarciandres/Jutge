def get_middle_digit(num):
    num_str = str(num)
    length = len(num_str)
    middle_index = length // 2
    
    if length % 2 == 0:
        return None  # Even number of digits
    
    return int(num_str[middle_index])

def determine_winner(n, numbers):
    for i in range(1, n):
        anna_num = numbers[2*i-1]
        bernard_num = numbers[2*i]
        
        anna_middle = get_middle_digit(anna_num)
        bernard_middle = get_middle_digit(bernard_num)
        
        if anna_middle is None or bernard_middle is None or anna_middle != bernard_middle:
            if i % 2 == 1:
                return 'A'  # Anna wins
            else:
                return 'B'  # Bernard wins
    
    return '='  # Draw

def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    
    winner = determine_winner(n, numbers)
    print(winner)

main()
