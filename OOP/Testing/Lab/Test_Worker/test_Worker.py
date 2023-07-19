from OOP.Testing.Lab.Test_Worker.Worker import Worker
from unittest import TestCase, main


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("TestGuy", 1000, 100)

    def test_correct_initializing(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increment_money_on_worker_when_working(self):
        self.worker.work()
        self.assertEqual(1000, self.worker.money)

    def test_decrease_energy_on_worker_when_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_raise_exception_when_working_with_0_or_negative_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual(str(ex.exception), "Not enough energy.")

    def test_increase_energy_with_one_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 101)

    def test_get_correct_info(self):
        info = f'TestGuy has saved 0 money.'
        self.assertEqual(self.worker.get_info(), info)


if __name__ == '__main__':
    main()
