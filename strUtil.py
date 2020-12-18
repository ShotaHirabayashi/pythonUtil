def make_map(list1, list2):
    """
    :param list1: keyとなるリスト
    :param list2: valueとなるリスト
    :return: マップ
    """
    adr_dict = dict(zip(list1, list2))
    return adr_dict


def get_list_to_str(list1):
    """
    :param list1 結合されるlist
    :return: 結合されたstr
    """


def get_non_duplicate_list(list1):
    """
    :param list1:
    :return: 重複を削除したリスト
    """
    return list(set(list1))


def isBlank(myString):
    """
    blankの判断をします
    :param myString:
    :return: blankの場合True
    """
    if myString and myString.strip():
        # myString is not None AND myString is not empty or blank
        return False
    # myString is None OR myString is empty or blank
    return True
