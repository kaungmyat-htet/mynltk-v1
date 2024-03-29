import os
from typing import Union
import json

from mynltk.corpus import corpus_path




def path_mynltk_corpus(filename: str) -> str:
    """
    Get path pythainlp.corpus data

    :param str filename: filename of the corpus to be read

    :return: : path of corpus
    :rtype: str
    """
    return os.path.join(corpus_path(), filename)

def get_corpus(filename: str) -> frozenset:
    path = path_mynltk_corpus(filename)
    lines = []
    with open(path, "r", encoding='utf-8-sig') as file:
        lines = file.read().splitlines()

    return frozenset(filter(None, lines))