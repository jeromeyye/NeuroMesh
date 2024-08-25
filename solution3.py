def max_val_of_multiset(n,arr):
    if(n<3):
        return 0
    sorted_arr = sorted(arr)
    small1 = sorted_arr[0]
    small2 = sorted_arr[1]
    largest = sorted_arr[-1]
    mean = (small1 + small2 + largest) / 3;
    mid = small2;
    ans = mean - mid;
    return ans

print(max_val_of_multiset(4,[1, 3, 5, 9]))