num_test = int(input())
for i in range(num_test):
    len_a =input()
    A = input().split()
    len_b =input()
    B=input().split()
    is_subset =True
    for element in A :
        if element not in B :
            is_subset =False
            break
    print(is_subset)