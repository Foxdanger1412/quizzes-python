if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    sortt = sorted(records, key = lambda x: x[1])
    scores = [x[1] for x in sortt]
    low = list(set(scores))[1]
    names = sorted([k[0] for k in sortt if k[1]==low])
    for i in names:
        print(i)
