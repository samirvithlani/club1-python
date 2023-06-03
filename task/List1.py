# def find_second_largest(numbers):
#     if len(numbers) < 2:
#         return None

numbers = [["sam",5],["raj",2],[ "parth",8],["prit",2], ["neha",9], ["jay",8]]
largest  =0
second_largest = 0
second_largest_list = []



for num in numbers:
    # 5 >0 True
    # 2 > 5 False
    # 8 > 5 True
    # 2 > 8 False
    # 9 > 8 True
    # 8 > 9 False
    for j in range(0,len(num)):
        if j ==1:
            print(num[j])
            if num[j] > largest:
                second_largest = largest
                largest = num[j]
            elif num[j] > second_largest and num[j] != largest:
                    #second_largest = 2
                    second_largest = num[j]
                        

        
    #       if num > largest:
        
    #     #second_largest = largest 0
    #     #5
    #     #8
    #             second_largest = largest
        
    #     #largest = 5
    #     #largest = 8
    #     #largest = 9
    #         largest = num
        
    
    # #   2 > 0true and  2 != 5 true
    # #   2 >5 false and 2 != 8 true
    # #   8 > 8
    #     elif num > second_largest and num != largest:
    #     #second_largest = 2
    #         second_largest = num
    

for num in numbers:
    for j in range(0,len(num)):
        if j ==1:
            if num[j] == second_largest:
                second_largest_list.append(num)

print(second_largest_list)                


# for num in numbers:
#     if num == second_largest:
#         second_largest_list.append(num)

    

# Example usage

