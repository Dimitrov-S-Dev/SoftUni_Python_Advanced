from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Pancho")

    def test_correct_init(self):
        self.assertEqual(self.team.name, "Pancho")
        self.assertEqual(self.team.members, {})

    def test_name_set_raise_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Pan@cho"

        self.assertEqual(str(ve.exception), "Team Name can contain only letters!")

    def test_add_member(self):
        self.team.members = {"Mancho": 20}
        members = {"Snoop": 22, "Dog": 24}
        result = self.team.add_member(**members)
        self.assertEqual(result, f"Successfully added: Snoop, Dog")
        self.assertEqual(self.team.members, {"Mancho": 20, "Snoop": 22, "Dog": 24})

    def test_remove_member_in_list(self):
        self.team.members = {"Mancho": 20, "Snoop": 22, "Dog": 24}
        result = self.team.remove_member("Mancho")
        self.assertEqual(result, "Member Mancho removed")
        self.assertEqual(self.team.members, {"Snoop": 22, "Dog": 24})

    def test_remove_member_not_in_list(self):
        self.team.members = {"Snoop": 22, "Dog": 24}
        result = self.team.remove_member("Dr.Dre")
        self.assertEqual(result, "Member with name Dr.Dre does not exist")
        self.assertEqual(self.team.members, {"Snoop": 22, "Dog": 24})

    def test_gt_true(self):
        self.team.members = {"Snoop": 22, "Dog": 24}
        self.other = Team("Mancho")
        self.other.members = {"Eminem": 26}
        result = self.team.__gt__(self.other)
        self.assertEqual(result, True)

    def test_gt_false(self):
        self.team.members = {"Snoop": 22, "Dog": 24}
        self.other = Team("Mancho")
        self.other.members = {"Eminem": 26,"DMX": 28, "Dr.Dre": 30}
        result = self.team.__gt__(self.other)
        self.assertEqual(result, False)

    def test_len(self):
        self.team.members = {"Snoop": 22, "Dog": 24}
        self.assertEqual(len(self.team), 2)

    def test_add(self):
        self.team.members = {"Snoop": 22, "Dog": 24}
        self.other = Team("Mancho")
        self.other.members = {"Eminem": 26}
        result = self.team.__add__(self.other)
        self.assertEqual(result.name, "PanchoMancho")
        self.assertEqual(result.members, {"Eminem": 26, "Snoop": 22, "Dog": 24})
        self.assertEqual(len(result), 3)

    def test_str(self):
        self.team.members = {"Snoop": 22, "Dog": 24}
        self.assertEqual(str(self.team),
                         f"Team name: Pancho\n"\
                         f"Member: Dog - 24-years old\n"\
                         f"Member: Snoop - 22-years old")








if __name__ == "__main__":
    main()
