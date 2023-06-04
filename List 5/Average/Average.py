def main():
    numbers = input().split()
    numbers = [float(num) for num in numbers]
    
    total = sum(numbers)
    average = total / len(numbers)
    
    formatted_average = "{:.2f}".format(average)
    
    print(formatted_average)
    
main()
