#-*- coding:utf-8 -*-
from typing import List, Tuple

def pos_tag(
    words: List[str],
    model: str = "",
    corpus: str = ""
) -> List[Tuple[str, str]]:
    """
    Tag words with part-of-speech (POS) tags, such as 'NOUN' and 'VERB'

    :params list words: a list of tokenized words

    :return: a list of tuples (word, POS tag)
    :rtype: list[tuple[str, str]]
    """
    pass