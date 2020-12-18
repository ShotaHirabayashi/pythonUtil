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


def get_week(dt):
    """
    :param dt: 日付
    :return: 指定した曜日
    """
    w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return w_list[dt.weekday()]


def get_today_week():
    """
    :return: 本日の曜日
    """
    w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return w_list[datetime.date.today().weekday()]
