"""
Takes a list of numbers from the user (input as comma-separated).
Prints:
    Total (sum)
    Average
    Max value
    List of even numbers
"""
class day2_mini_tasks:
    def __init__(self):
        print("""Takes a list of numbers from the user (input as comma-separated).
                Prints:
                    * Total (sum)
                    * Average
                    * Max value
                    * List of even numbers""")
        
    def totalSum(self, numbers):
        total = 0 
        for i in numbers:
            total += i 
        return total 
    
    def Avg(self, numbers, total):
        return total/len(numbers)
    
    def maximum_num(self, numbers):
        max_num = numbers[0]
        for num in numbers[1:]:
            if num > max_num:
                max_num = num 
        return max_num 
    
    def Even_numbers(self, numbers):
        return [i for i in numbers if i % 2 == 0]
    
    def sorting_numbers(self, numbers):
        n = len(numbers)
        for i in range(n):
            for j in range(0, n - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers





def main():
    d2 = day2_mini_tasks() 
    try:
        numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))
    except Exception as e:
        print("Enter the valid numbers.")
        numbers = []
    total = d2.totalSum(numbers) 
    average = d2.Avg(numbers=numbers, total=total)
    maximum_number = d2.maximum_num(numbers=numbers)
    even_number = d2.Even_numbers(numbers)
    sorted_array = d2.sorting_numbers(numbers)
    print(f"total: {total}")
    print(f"Average: {average}")
    print(f"maximum_number is: {maximum_number}")
    print(f"Even numbers: {even_number}")
    print(f"sorted array: {sorted_array}")
    print("----------------- using inbuilt functions ------------------------")
    print(f"Total of numbers:", sum(numbers))
    print(f"Average of numbers:{sum(numbers)//len(numbers)}")
    print(f"Maximum_number is: {max(numbers)}")
    print(f"lambda method of finding even numbers: {list(filter(lambda x: x %2 == 0, numbers))}")
    print(f"sorted array: {sorted(numbers)}")
if __name__ == '__main__':
    main()