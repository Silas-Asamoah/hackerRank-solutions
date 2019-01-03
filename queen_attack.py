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