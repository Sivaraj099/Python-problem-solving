def read_input():
    try:
        n, d = map(int, input().strip().split())
        teachers = []
        for _ in range(n):
            arrival_day, lectures, curse_level = map(int, input().strip().split())
            teachers.append([arrival_day, lectures, curse_level])
        return n, d, teachers
    except ValueError:
        return None

def evaluate_lecture_schedule(n, d, teachers):
    total_curse = 0
    lecture_schedule = [[-1, -1, -1], [-1, -1, -1]]

    for day in range(1, d + 1):
        for teacher in teachers:
            if teacher[0] == day:
                lecture_schedule.append(teacher)

        lecture_schedule.sort(key=lambda x: x[2], reverse=True)

        if lecture_schedule:
            lecture_schedule[0][1] -= 1

        lecture_schedule += [[1, 0, 0] for _ in range(len(lecture_schedule))]
        lecture_schedule = [teacher for teacher in lecture_schedule if teacher[1] > 0]

    for teacher in lecture_schedule:
        if teacher[1] > 0:
            total_curse += teacher[2] * teacher[1]

    print(total_curse)

def main():
    input_data = read_input()
    
    if input_data is None:
        print("Invalid input format")
        return  
    
    n, d, teachers = input_data
    evaluate_lecture_schedule(n, d, teachers)

if __name__ == '__main__':
    main()