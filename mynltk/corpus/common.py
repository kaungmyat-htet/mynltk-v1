from typing import FrozenSet


from mynltk.corpus import get_corpus

_MYANMAR_STOPWORDS: FrozenSet[str] = frozenset()
_MYANMAR_STOPWORDS_FILENAME = "stopwords_my.txt"

def myanmar_stopwords() -> FrozenSet[str]:
    """
    Return set of myanmar stopwords
    """
    global _MYANMAR_STOPWORDS
    if not _MYANMAR_STOPWORDS:
        _MYANMAR_STOPWORDS = get_corpus(_MYANMAR_STOPWORDS_FILENAME)

    return _MYANMAR_STOPWORDS