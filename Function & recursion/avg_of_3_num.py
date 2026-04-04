n = int(input("Enter the number of values you want to average: "))

def avg_of_num(n):
    a = []
    
    # 1. Collect the numbers
    for i in range(1, n + 1):
        print("Enter number", i, ":")
        num = int(input())
        a.append(num)
        
    # 2. Initialize the sum variable once
    final = 0
    
    # 3. Sum the numbers (Corrected range to avoid IndexError)
    for avg in range(n):
        final = final + a[avg]
        
    # 4. Calculate the average outside the loop
    final = final / n
    
    # 5. Return the final result at the very end
    return final
    
       

print(avg_of_num(n))