import datetime
import time


def jst_to_utc(date=datetime.datetime.now()):
    return date + datetime.timedelta(hours=9)


def utc_to_jst(date=datetime.datetime.now()):
    return date - datetime.timedelta(hours=9)
