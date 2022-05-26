"""
Have you heard of SOLID: The First 5 Principles of Object-Oriented Design?
If you did it, write to codes that implement one of five SOLID principles.
Notice that the implementation should be different.
"""
"""Single Responsibility Principle"""




from datetime import date, datetime
from dateutil.relativedelta import relativedelta
class DateModify:
    def __init__(self, days_add, months_add, years_add):
        self.days_add = days_add
        self.months_add = months_add
        self.years_add = years_add

    def format_date(self, date):
        print(datetime.strftime(date, '%d/%m/%Y'))

    def calc_date(self):
        date_now = datetime.today()
        date_add = relativedelta(
            years=self.years_add, months=self.months_add, days=self.days_add)

        new_date = date_now + date_add

        self.format_date(new_date)


new_values = DateModify(30, 9, 20)
new_values.calc_date()
