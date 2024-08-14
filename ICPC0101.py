
st = []
n = int(input())
arrNumber = map(int, input().split())

for x in arrNumber:
    if len(st) == 0:    
        st.append(x)
    else:
        if((st[-1] + x) % 2 == 0):
            st.pop()
        else:
            st.append(x)

print(len(st))

