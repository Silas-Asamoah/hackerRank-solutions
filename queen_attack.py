n , k = map(int, input().split(''))
r_q, c_q = map(int, input().split(''))

top = n - r_q
bottom = c_q - 1
right = n - c_q
left = c_q - 1

top_left = min(top, left)
top_right = min(top, right )
bottom_left = min(bottom, left)
bottom_right = min(bottom, right)

for a0 in range(k):
    o_r, o_c = map(int, input().split(''))

    #Horizontal
    if o_r == r_q:
        if o_c > c_q:
            top = min(top, o_c - c_q - 1)
        else:
            bottom = min(bottom, c_q - o_c - 1)

    #Vertical
    elif o_c == c_q:
        if o_r > r_q:
            right = min(right, o_c - r_q - 1)
        else:
            left = min(left, c_q - o_r - 1)

    #Diagonals
    elif abs(o_c - c_q) == (o_r - r_q):
        #top right
        if o_c > c_q and o_r > r_q:
            top_right = min(top_right, o_c - c_q - 1)
        elif o_c > c_q and o_r < r_q:
            bottom_right = min(bottom_right, o_c - c_q - 1)
        elif o_c < c_q and o_r > r_q:
            top_left = min(top_left, c_q - o_c - 1)
        elif o_c < c_q and o_r < r_q:
            bottom_left = min(bottom_left, c_q - o_c - 1)
        
    



print(top + bottom + right + left + top_left + top_right + bottom_left + bottom_right)