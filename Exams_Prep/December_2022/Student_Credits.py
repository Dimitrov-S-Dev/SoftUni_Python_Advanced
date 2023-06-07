def students_credits(*args):
    total_credits = 0
    c_credits = {}
    output = ""
    for course in args:
        course_name, *data = course.split("-")
        credit, max_points, diyan_points = [int(x) for x in data]
        course_credit = credit * (diyan_points / max_points)
        c_credits[course_name] = course_credit
        total_credits += course_credit

    if total_credits >= 240:
        output += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"

    else:
        diff = 240 - total_credits
        output += f"Diyan needs {diff:.1f} credits more for a diploma.\n"

    sorted_c_c = sorted(c_credits.items(), key=lambda x: (-x[1], x[0]))
    for k, v in sorted_c_c:
        output += f"{k} - {v:.1f}\n"

    return output
