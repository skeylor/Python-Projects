if __name__ == '__main__':
    records = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        record = []
        record.append(name)
        record.append(score)
        records.append(record)
    # sort list of list
    # sort by second index
    records.sort(key = lambda records: records[1])
    records.pop(0)
    second_lowest = []
    if records[0][1] == records[1][1]:
        second_lowest.append(records[0][0])
        second_lowest.append([records[1][0]])
        second_lowest.sort(key = lambda second_lowest: records[0])
        print(second_lowest[1][0])
        print(second_lowest[0])
    else:
        print(records[0][0])
        