# Read the number of elements
n = int(input().strip())

# Read the list of elements
elements = list(map(int, input().strip().split()))

# Find the minimum element
min_element = elements[0]  # Assume the first element is the minimum

for element in elements:
    if element < min_element:
        min_element = element

# Print the minimum element
print(min_element)


"""Prateek finds it difficult to judge the minimum element in the list of elements given to him. Your task is to develop the algorithm in order to find the minimum element.

Input Description:
You are given ‘n’ number of elements. Next line contains n space separated numbers.

Output Description:
Print the minimum element

Sample Input :
5
3 4 9 1 6

Sample Output :
1"""
