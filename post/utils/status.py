STATUS_DICT = {
    "public": 1,
    "private": 2,
    "delete": 3,
}


def to_int_status_id(str):
    try:
        return STATUS_DICT[str]
    except KeyError:
        return
