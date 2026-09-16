def main():
    print("===== CALCULATOR =====")
    print("Choose an operation:")
    print("1. Multiplication")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Division")
    
    choice = input("\nSelect a number to choose an operation: ")
      #Made by Faith
    if choice == "1": 
        print("\n=== MULTIPLICATION ===")
        # Multiplication Calculator
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 * num2
        print("The answer is:", result)
        
        #Made by ella
    elif choice == "2":
        print("\n=== ADDITION ===")
        
        num1 = int(input("1st num?"))
        num2 = int(input("2nd num?"))
        calculate = num1 + num2 
        print(f"the total is: { calculate }")
      
      #Made my mae 
    elif choice == "3":
        print("\n=== SUBTRACTION ===") 
        
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        Answer = num1 - num2
        print("Result:", Answer)
        
        #Made by L.A
    elif choice == "4":
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))

        Answer = num1 / num2
        print("Result:", Answer)     

    else:
        print("\n Invalid choice!! select 1-3")


main()
    
