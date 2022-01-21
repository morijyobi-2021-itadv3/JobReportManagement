from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=+9), 'JST')


def set_utc_timezone(dt):
    """
    nativeなdatetimeメソッドにtimezone(utc)を付与する
    Args:
        dt:nativeなdatetime

    Returns:
        timezone(utc)が付与されたdatetime

    """
    return dt.replace(tzinfo=timezone.utc)


def set_jst_timezone(dt):
    """
        nativeなdatetimeメソッドにtimezone(jst)を付与する
        Args:
            dt:nativeなdatetime(aware)

        Returns:
            timezone(jst)が付与されたdatetime

        """
    return dt.replace(tzinfo=JST)


def jst_now():
    """
    JSTの現在時刻を返すメソッド
    Returns:
        datetime(aware):jst(GMT+9)の現在時刻を返す

    """
    return datetime.now(JST)


def utc_now():
    """
       UTCの現在時刻を返すメソッド
       Returns:
           datetime(aware):jst(GMT+0)の現在時刻を返す

    """
    return datetime.now(timezone.utc)
