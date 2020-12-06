import datetime


def get_time_now():
    """
    :return: ハイフン付きの時間（2020-12-06）
    """
    return datetime.date.today()


def get_formatted_time(target_time):
    """
    :param target_time:  get_time_noで取得した時間
    :return: 8桁の時間（20201206）
    """
    return f'{target_time:%Y%m%d}'


def delta_time(delay):
    """
    :param delay: ずらしたい日数
    :return: ずらした8桁の時間（20201206）
    """
    delay_day = datetime.datetime.now() + datetime.timedelta(days=delay)
    return f'{delay_day:%Y%m%d}'
