"""
Create a Python file hello_harry.py

Write the two mini programs (ask name+age + print numbers 1-10).

Initialize Git.

Commit + Push to GitHub.

"""

def ask_name_and_age(name, age):
    """Prints a greeting with the user's name and age."""
    print(f"Hello {name}, you are {age} years old.") 

def iterate_number(n):
    for i in range(n):
        print(i + 1)
# hello_harry.py
def main():
    name = input("Enter your name: ")
    try:
        age = int(input("Enter your age: "))
    except Exception as e:
        print(f"Value Error: {e}")
        age = 0
    ask_name_and_age(name, age)
    iterate_number(10) 


if __name__ == '__main__':
    main()
