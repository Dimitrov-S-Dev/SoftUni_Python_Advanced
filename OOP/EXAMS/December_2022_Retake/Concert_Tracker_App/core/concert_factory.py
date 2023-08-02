from OOP.EXAMS.December_2022_Retake.Concert_Tracker_App.concert import Concert


class ConcertFactory:
    @staticmethod
    def create_concert(genre, audience, ticket_price, expenses, place):
        return Concert(genre, audience, ticket_price, expenses, place)
