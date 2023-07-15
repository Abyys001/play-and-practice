rec1 = [2, 4, 4]
rec4 = [5, 2, 6]
rec3 = [4, 2, 5]
rec2 = [5, 4, 6]
z
center_rec = rec1

for i in range(len(center_rec)):
    is_equal = 0
    for num in center_rec:
        if center_rec[i] == num:
            is_equal += 1
    if is_equal >= 2:
        print(True)
    else:
        print(False)