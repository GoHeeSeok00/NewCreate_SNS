STATUS_DICT = {
    1: "public",
    2: "private",
    3: "delete",
}


def to_str_status_id(int):
    try:
        return STATUS_DICT[int]
    except KeyError:
        return
