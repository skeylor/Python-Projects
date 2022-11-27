if __name__ == '__main__':
    students = [['erik',-50],['bob',-50],['george',-50],['harry',-50],['larry',30.5]]
    scores = [-50,-50,-50,-50,30.5]
    res = [*set(scores)]  # To remove duplicate scores data
    res = list(res)
    res.sort()
    second_high_score = res[1]

    students.sort()
    for i in students:
        if second_high_score == i[1]:
            print(i[0])