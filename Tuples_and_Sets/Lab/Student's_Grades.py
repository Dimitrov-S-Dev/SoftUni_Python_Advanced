n = int(input())
students_dict = {}

for _ in range(n):
    name, grade = input().split()
    if name not in students_dict.keys():
        students_dict[name] = []
    students_dict[name].append(float(grade))

sorted_dict = dict(sorted(students_dict.items(), key=lambda x: len(x[1]), reverse=True))
for k, v in sorted_dict.items():
    avg = sum(v) / len(v)
    print(f"{k}: {' '.join([str(grade) for grade in v])} ({avg:.2f})")
