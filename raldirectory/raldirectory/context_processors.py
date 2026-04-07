from datetime import date


def war_day(request):
    target_day = date(2022, 2, 24)
    today = date.today()
    delta = -(target_day - today)
    return {'day_of_war': delta.days}
