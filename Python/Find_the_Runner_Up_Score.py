# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.
# Input Format
# The first line contains n. The second line contains an array A[] of n  integers each separated by a space.

if __name__ == '__main__':
    n = int(input("Enter the total numbers: "))
    arr = list(map(int, input("Enter the numbers: ").split()))
    if arr[0] >= arr[1]:
        first_max = arr[0]
        second_max = arr[1]
    else:
        first_max = arr[1]
        second_max = arr[0]
    for i in range(2, n):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
        elif (first_max == second_max) or ((arr[i] > second_max) and arr[i] != first_max):
            second_max = arr[i]
    print(second_max)