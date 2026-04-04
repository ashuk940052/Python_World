num = int(input("Enter the number: - "))

def cal_sum(n):
    # Base case: return 0 instead of None
    if n == 0:
        return 0
    
    # Optional: You can keep this if you want to see it count down, 
    # but usually, we remove it to just get the final answer.
    print("Calculating for:", n) 
    
    # Recursive step
    return cal_sum(n - 1) + n

# Print the final result so you can actually see the sum
final_answer = cal_sum(num)
print("The total sum is:", final_answer)