from unittest import TestCase, main

from OOP.Testing.Exercise.Student.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Carabas")
        self.st_with_course = Student("Carabas", {"Math": ["one"]})

    def test_correct_initialize(self):
        self.assertEqual(self.student.name, "Carabas")
        self.assertEqual(self.st_with_course.courses, {"Barabas": ["Tarabas"]})
        self.assertEqual(self.student.courses, {})

    def test_enroll_with_course_already_added(self):
        r = self.st_with_course.enroll("Barabas", ["one", "two"])
        self.assertEqual(self.st_with_course.courses["Barabas"],
                         ["Tarabas", "one", "two"])

        self.assertEqual(r, "Course already added. Notes have been updated.")

    def test_add_notes_to_non_existing_course_with_Y(self):
        r = self.student.enroll("Music", ["one", "two"], "Y")
        self.assertEqual(self.student.courses["Music"], ["one", "two"])
        self.assertEqual(r, "Course and course notes have been added.")

    def test_add_notes_to_non_existing_course_without_param(self):
        r = self.student.enroll("Music", ["one", "two"], "")
        self.assertEqual(self.student.courses["Music"],
                         ["one", "two"])
        self.assertEqual(r, "Course and course notes have been added.")

    def test_add_new_course_without_adding_the_notes(self):
        r = self.student.enroll("Music", ["one", "two"], "N")
        self.assertEqual(self.student.courses["Music"],
                         [])
        self.assertEqual(r, "Course has been added.")

    def test_add_note_with_existing_course(self):
        r = self.st_with_course.add_notes("Math", "two")
        self.assertEqual(self.st_with_course.courses["Math"], ["one", "two"])
        self.assertEqual(r, "Notes have been updated")

    def test_add_note_with_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("python", "three")

        self.assertEqual(str(ex.exception), "Cannot add notes. "
                                            "Course not found.")

    def test_leave_course_with_existing_course(self):
        r = self.st_with_course.leave_course("Math")
        self.assertEqual(self.st_with_course.courses, {})
        self.assertEqual(r, "Course has been removed")

    def test_leave_curse_with_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("python")

        self.assertEqual(str(ex.exception), "Cannot remove course. "
                                            "Course not found.")












if __name__ == "__main__":
    main()