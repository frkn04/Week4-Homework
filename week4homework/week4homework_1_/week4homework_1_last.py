import sys
import outside_multi_hw1, outside_sub_hw1, outsite_add_hw1, outsite_divide_hw1


while True:           
    
    try:
        operation = int(input("Enter '1' for Multiplication\nEnter '2' for Division\nEnter'3' for Subtraction\nEnter 4' for Addition\n'0' for Escape\n"))
        
        if operation == 1:
             
            number_1 = float(input("\nPlease enter number"))
            number_2 = float(input("\nPlease enter another number"))            
            
            print(outside_multi_hw1.multi(number_1,number_2))
    
        elif operation == 4:
            number_1 = float(input("\nPlease enter number"))
            number_2 = float(input("\nPlease enter another number"))
            print(outsite_add_hw1.add(number_1,number_2))
            
        elif operation == 3:
            number_1 = float(input("\nPlease enter number"))
            number_2 = float(input("\nPlease enter another number"))
            print(outside_sub_hw1.sub(number_1,number_2))
            
        elif operation == 2:
            number_1 = float(input("\nPlease enter number"))
            number_2 = float(input("\nPlease enter another number"))
            print(outsite_divide_hw1.divide(number_1,number_2))
            
        elif operation == 0:
            print("Thank you")
            break
        
        else :
            print("Please repeat again.")        

    except :
        print("ooops")
        print(str(sys.exc_info()))
        