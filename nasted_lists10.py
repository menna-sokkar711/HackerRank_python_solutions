if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = sorted(list(set([student[1]for student in students])))
    secound_lowest_score = scores[1]
    names = [student[0] for student in students if student[1] == secound_lowest_score]
    for name in sorted(names):
        print(name