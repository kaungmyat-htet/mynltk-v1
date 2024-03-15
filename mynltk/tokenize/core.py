# -*- coding: utf-8 -*-
"""
functions of tokenizers
"""
import re
from typing import List

def phrase_tokenize(
    words_list: List[str],
    threshold: float = 0.1,
    minfreq: int = 5,
    unigram_phrases_bin: str = "unigram-phrase.bin",
    bigram_phrases_bin: str = "bigram-phrase.bin",
    include_seperator: bool = False
) -> List[str]:
    """
    Phrase tokenizer (phrase segmentation with NPMI (Normalized Pointwise Mutual Information) proposed by Bouma Gerlof, 2009)

    Tokenize seperated words into phrases.
    Important! Make sure your sentence is tokenized into words already.

    :param list[str] words_list: list of words to be tokenized into phrases
    :param float threshold: set the threshold value, the default is 0.1
    :param int minfreq: set the minimum frequency value, the default is 3
    :param str unigram_phrases_bin: set filename of the unigram dictionary for segmentation (binary-file), the default name is \"unigram-phrase.bin\"
    :param str bigram_phrases_bin: set filename of the bigram dictionary for segmentation (binary-file), the default name is \"bigram-phrase.bin\"
    :param bool include_seperator: set True if you want to add "_" in the phrase or between the combined words such "မြန်မာ_သတင်း". If false, it would output "မြန်မာသတင်း"

    :return: list of phrases
    :rtype: list[str]
    :Example:
    ::
    
        from mynltk.tokenize import phrase_tokenize
        
        # tokenized words
        words = ['လူငယ်', 'တစ်', 'ဦး', 'ငါးမျှား', 'နေ', 'ရင်း', 'ချောင်း', 'ထဲ', 'ပြုတ်ကျ', 'သွား', 'တယ်']
        print(phrase_tokenize(words))
        # output: ['လူငယ်', 'တစ်', 'ဦး', 'ငါးမျှားနေ', 'ရင်း', 'ချောင်း', 'ထဲ', 'ပြုတ်ကျသွား', 'တယ်']

        # with include_sperator True and default parameters
        print(phrase_tokenize(words, include_seperator=True))
        # ['လူငယ်', 'တစ်', 'ဦး', 'ငါးမျှား_နေ', 'ရင်း', 'ချောင်း', 'ထဲ', 'ပြုတ်ကျ_သွား', 'တယ်']
    """
    if not words_list or not isinstance(words_list, list):
        return []
    
    unigram_phrases_bin = "mynltk/corpus/" + unigram_phrases_bin
    bigram_phrases_bin = "mynltk/corpus/" + bigram_phrases_bin
    from mynltk.tokenize.phrase_segment import segment
    
    segments = []
    segments = segment(words_list, threshold, minfreq, unigram_phrases_bin, bigram_phrases_bin, include_seperator)
    
    return segments


def word_tokenize(
    text:str
) -> List[str]:
    """
    Word tokenizer.

    Tokenize text into words (list of strings).
    
    :param str text: text to be tokenized
    :return: list of words
    :rtype: list[str]
    :Example:
    ::

        from mynltk.tokenize import word_tokenize

        text = "ကျွန်တော့်နာမည်ကမောင်မောင်ဖြစ်ပါသည်။"

        word_tokenize(text)
        # output: ['ကျွန်တော့်', 'နာမည်', 'က', 'မောင်မောင်', 'ဖြစ်ပါသည်', '။']
    
    """
    if not text or not isinstance(text, str):
        return []
    
    uni_dict_bin = "mynltk/corpus/unigram-word.bin"
    bi_dict_bin = "mynltk/corpus/unigram-word.bin"

    from mynltk.tokenize import word_segment
    
    word_segment.P_unigram = word_segment.ProbDist(uni_dict_bin, True)
    word_segment.P_bigram = word_segment.ProbDist(bi_dict_bin, False)

    segments = []
    # Since viterbi function will return tuple (-0.6252955533327977, ['ကျွန်တော်', 'စာ', 'လုပ်', 'နေ', 'ပါ', 'သည်', '။'])
    segments = word_segment.viterbi(text.replace(" ", "").strip())[1]
    
    return segments

def sentence_tokenize(
    text: str
) -> List[str]:
    return 0


def syllable_tokenize(
    text: str
) -> List[str]:
    """
    Syllable tokenizer

    Tokenizes text into inseperable units of Myanmar syllables.

    :param str text: text to be tokenized
    :return: list of subwords
    :Example:
    ::

        from mynltk.tokenize import syllable_tokenize

        text = "ကျွန်တော့်နာမည်ကမောင်မောင်ဖြစ်ပါသည်။"

        syllable_tokenize(text)
        # output: ["ကျွန်", "တော့်", "နာ", "မည်", "က", "မောင်", "မောင်", "ဖြစ်", "ပါ", "သည်", "။"]
    
    """
    if not text or not isinstance(text, str):
        return []
    
    # remove whitespace between words
    text = text.replace(" ", "")

    segments = []

    from mynltk.tokenize.syllable_segment import segment
    
    segments = segment(text)

    return segments
    
