import datetime
import re
from backend.errors import BadRequest

# Based on https://stackoverflow.com/a/51916936
duration_regex = re.compile(
    r"^((?P<days>[\.\d]+?)d)?((?P<hours>[\.\d]+?)h)?((?P<minutes>[\.\d]+?)m)?((?P<seconds>[\.\d]+?)s)?$"
)


def timestamp():
    """Return current UTC time"""
    return datetime.datetime.utcnow()


def to_strftime(date: datetime.datetime):
    """Convert date to string format"""
    return date.strftime("%Y-%m-%d %H:%M:%S")


def to_strfdate(date: datetime.datetime):
    """Convert date to string date format"""
    return date.strftime("%Y-%m-%d")


def to_datetime(date_string: str):
    """Convert string date to date object"""
    return datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ").date()


def format_and_validate_start_end_date(
    start_date: datetime.datetime, end_date: datetime.datetime
) -> tuple[datetime.datetime, datetime.datetime]:
    try:
        if start_date:
            start_date = to_datetime(start_date)
        if end_date:
            end_date = to_datetime(end_date)
    except ValueError as e:
        raise BadRequest(sub_code="BAD_REQUEST", message=str(e))
    if start_date and end_date and start_date > end_date:
        raise BadRequest(sub_code="START_DATE_AFTER_END_DATE")
    return start_date, end_date


def get_last_updated(last_updated):
    now = datetime.datetime.now(datetime.timezone.utc)
    if last_updated.tzinfo is None or last_updated.tzinfo.utcoffset(last_updated) is None:
        last_updated = last_updated.replace(tzinfo=datetime.timezone.utc)
    diff = now - last_updated
    if diff.days > 0:
        return f"{diff.days} days ago"
    elif diff.seconds > 3600:
        return f"{diff.seconds // 3600} hours ago"
    elif diff.seconds > 60:
        return f"{diff.seconds // 60} minutes ago"
    else:
        return f"{diff.seconds} seconds ago"


def parse_duration(time_str):
    """
    Parse a duration string e.g. (2h13m) into a timedelta object.
    :param time_str: A string identifying a duration.  (eg. 2h13m)
    :return datetime.timedelta: A datetime.timedelta object
    """
    parts = duration_regex.match(time_str)
    assert parts is not None, "Could not parse duration from '{}'".format(
        time_str
    )
    time_params = {
        name: float(param)
        for name, param in parts.groupdict().items()
        if param
    }
    return datetime.timedelta(**time_params)
