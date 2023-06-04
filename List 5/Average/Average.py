def main():
    counter = 0
    total = 0
    
    while True:
        try:
            a = float(input())
            counter += 1
            total += a
        except ValueError:
            break
    
    result = total / counter
    print("{:.2f}".format(result))
    
if __name__ == "__main__":
    main()
