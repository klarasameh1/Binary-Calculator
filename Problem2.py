  #klara sameh wadie   20230294
  #katren nader nagy   20230289
#___________________________________

#storing each menu in a variable to be easy to call anytime
menu1=str("**binary calculator**\nA)Insert new numbers\nB)Exit")
menu2=str("**Please select the operation**\nA)compute one's complemrnt\nB)compute two's complement\nC)addition\nD)subtraction")


#defining functions for checking validation of inputs and functions for each single operation.

#This function check each input if it's A binary or not.
#by checking each digit if it equals 1 or 0 .
def checking_binary(num):
    for digit in num:
        if digit!='0'and digit!='1':
            return False
    return True
                    
#function which calculate the one's complement.
#by switching each 1 to 0 and each 0 to 1.
def ones_complement(num1):
   complement = ""
   for digit in num1:
        if digit == '0':
            complement += '1'
        else:
            complement += '0'
   return complement


#function which calculate the two's complement.
#by geting the one's complement and add 1
def twos_complement(num1):
   complement = ones_complement(num1)
   twos_complement = ""
   carry = '1'
   for i in range(len(complement) - 1, -1, -1):
        if complement[i] == '0' and carry == '0':
            twos_complement = '0' + twos_complement
            carry = '0'
        elif complement[i] == '1' and carry == '0':
            twos_complement = '1' + twos_complement
            carry = '0'
        elif complement[i] == '0' and carry == '1':
            twos_complement = '1' + twos_complement
            carry = '0'
        else:
            twos_complement = '0' + twos_complement
            carry = '1'
   return twos_complement

#function to compare two binary numbers to make them the same lenght
#it will be used in substruction and addition
def compare_binary(num1, num2):
    # Compare the lengths of the binary numbers
    len_num1 = len(num1)
    len_num2 = len(num2)
    # Pad the shorter binary number with leading zeros
    if len_num1 < len_num2:
        num1 ='0' * (len_num2 - len_num1) + num1
    elif len_num2 < len_num1:
        num2 = '0' * (len_num1 - len_num2) + num2
    return num1,num2
    

   
# function which calculate the addition.
def add_binary(num1, num2):
    num1,num2=compare_binary(num1, num2)
    
    carry = 0
    result = ""
    index = len(num1) - 1  # Start from the least significant bit
    while index >= 0:
        bit_sum = int(num1[index]) + int(num2[index]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2
        index -= 1

    # If there's a carry left over, add it to the beginning
    if carry != 0:
        result= str(carry) + result

    return result


#function which calculate the substruction
def sub_binary(num1,num2):
    num1,num2=compare_binary(num1, num2)
    result = ""
    index = len(num1) - 1
    borrow = 0

    while index >= 0:
        bit_diff = int(num1[index]) - int(num2[index]) - borrow
        if bit_diff < 0:
            bit_diff += 2
            borrow = 1
        else:
            borrow = 0
        result = str(bit_diff) + result
        index -= 1

    return result


#The main program 
#showing every menu and taking inputs
#returning menues when input is invalid
#doing operations by calling the function 

def main_program():
 while True:
    print(menu1)
    choice_1=input("Enter you choice(A/B):").upper()
    if choice_1=="A":
     num1=input("Insert the first binary number:")
     while not checking_binary(num1):
       num1=input("Erorr:please insert a vaild binary number:")
     print(menu2)
     choice_2=input("Enter your choice (A/B/C/D):").upper()
     if choice_2=="A":
         print(f"The result= {ones_complement(num1)}")
     elif choice_2=="B":
         print(f"The result== {twos_complement(num1)}")
     elif choice_2=="C":
         num2 = input("Insert the second binary number: ")
         while not checking_binary(num2):
            num2 = input("\nErorr:Please insert a valid binary number:\n")
         result = add_binary(num1, num2)
         print(f"The result= = {result}")
     elif choice_2=="D":
         num2 = input("Insert the second binary number: ")
         while not checking_binary(num2):
            num2 = input("\nErorr:Please insert a valid binary number:\n")
         result = sub_binary(num1, num2)
         print(f"The result= = {result}")
     else:
         print("\nErorr:Please select a valid choice.\n")
         print(menu2)
         choice_2=input("Enter your choice (A/B/C/D):").upper()
    elif choice_1=="B" :
        print("Exiting the program...Goodbye!\n")    
        break
    else:
        print("\nErorr:Please select a valid choice.\n")
main_program()