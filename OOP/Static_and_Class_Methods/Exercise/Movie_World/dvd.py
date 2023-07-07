from project.month_mapper import month_mapper
class DVD:
    def __init__(self, name: str, dvd_id: int, creation_year: int,
                 creation_month: str, age_restriction: int):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, d_id, name, date, age_restriction):
        _, month, year = [x for x in date.split(".")]
        if isinstance(int(month), int):
            month = month_mapper[int(month)]
        return cls(name, d_id, int(year), month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} "\
                f"{self.creation_year}) has age restriction "\
                f"{self.age_restriction}. Status: "\
                f"{'rented' if self.is_rented else 'not rented'}"

