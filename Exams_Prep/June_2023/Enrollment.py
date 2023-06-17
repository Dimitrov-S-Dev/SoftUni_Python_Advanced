def gather_credits(credits_needed, *courses):
    courses_rolled = []
    gathered_credits = 0

    for course in courses:
        c_name, c_credits = course

        if c_name not in courses_rolled and gathered_credits < credits_needed:
            courses_rolled.append(c_name)
            gathered_credits += c_credits
    if gathered_credits >= credits_needed:
        sorted_courses = ", ".join(sorted(courses_rolled))
        return f"Enrollment finished! Maximum credits: {gathered_credits}." \
               f"\nCourses: {sorted_courses}"

    else:
        credits_shortage = credits_needed - gathered_credits
        return f"You need to enroll in more courses! You have to gather " \
               f"{credits_shortage} credits more."



