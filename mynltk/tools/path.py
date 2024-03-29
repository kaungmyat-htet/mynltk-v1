import os

from mynltk import __file__ as mynltk_file

print(mynltk_file)
def get_mynltk_path() -> str:
    """
    This function returns full path of PyThaiNLP codes

    :return: full path of :mod:`pythainlp` codes
    :rtype: str

    :Example:
    ::

        from pythainlp.tools import get_pythainlp_path

        get_pythainlp_path()
        # output: '/usr/local/lib/python3.6/dist-packages/pythainlp'
    """
    return os.path.dirname(mynltk_file)