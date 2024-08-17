m, n = map(int, input().split())

phieuBau = [0] * (n + 1)

idxCuTri = map(int, input().split())
for i in idxCuTri:
    phieuBau[i] += 1


maxVote = secondVote = -1

for votes in phieuBau:
    if votes > maxVote:
        secondVote = maxVote
        maxVote = votes
    elif secondVote < votes < maxVote:
        secondVote = votes

if secondVote == 0:
    print("NONE")
else:
    for i in range(1, n):
        if phieuBau[i] == secondVote:
            print(i)
            break