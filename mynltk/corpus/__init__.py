# -*- coding: utf-8 -*-

"""
Corpus related functions
"""

import os

from pyburmesenlp.tools import get_pyburmesenlp_data_path, get_pyburmesenlp_path, get_full_data_path

_CORPUS_DIRNAME = "corpus"
_CORPUS_PATH = os.path.join(get_pyburmesenlp_path(), _CORPUS_DIRNAME)

_CORPUS_DB_FILENAME = "db.json"

# full path of local corpus catalog
_CORPUS_DB_PATH = get_full_data_path(_CORPUS_DB_FILENAME)

def corpus_path() -> str:
    """
    Get path where corpus files are kept locally.
    """
    return _CORPUS_PATH

def corpus_db_path() -> str:
    """
    Get local path of corpus catalog.
    """
    return _CORPUS_DB_PATH

def corpus_db_url() -> str:
    """
    Get remote URL of corpus catalog.
    """
    return _CORPUS_DB_URL