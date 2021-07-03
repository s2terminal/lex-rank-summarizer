from janome.analyzer import Analyzer
from janome.charfilter import CharFilter, UnicodeNormalizeCharFilter, RegexReplaceCharFilter
from janome.tokenizer import Tokenizer as JanomeTokenizer
from janome.tokenfilter import TokenFilter, POSKeepFilter, ExtractAttributeFilter

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer as SumyTokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.summarizers._summarizer import SentenceInfo

import re

from typing import NewType
Sentence = NewType('Sentence', str)

def main(text: str, sentences_count: int=3) -> str:
    return "\n".join(generateSummary(text, sentences_count))

def separateCorpus(sentences: list[Sentence]):
    char_filters: list[CharFilter] = [
        UnicodeNormalizeCharFilter(),
        RegexReplaceCharFilter(r'[(\)「」、。]', ' ')
    ]
    token_filters: list[TokenFilter] = [
        POSKeepFilter(['名詞', '形容詞', '副詞', '動詞']),
        ExtractAttributeFilter('base_form')
    ]
    analyzer = Analyzer(
        char_filters=char_filters,
        tokenizer=JanomeTokenizer(),
        token_filters=token_filters
    )

    return [' '.join(analyzer.analyze(s)) + '。' for s in sentences]

def separateSentences(text: str):
    return [Sentence(t) for t in re.split('[\n。]', text)]

def summarize(parser: PlaintextParser, sentences_count: int):
    summarizer = LexRankSummarizer()
    summarizer.stop_words = [' ']

    summaries: list[SentenceInfo] = summarizer(document=parser.document, sentences_count=sentences_count) # type: ignore
    return summaries

def generateSummary(text: str, sentences_count: int) -> list[str]:
    sentences = separateSentences(text)
    corpus = separateCorpus(sentences)
    parser = PlaintextParser.from_string(''.join(corpus), SumyTokenizer('japanese'))
    summaries = summarize(parser, sentences_count)

    return [sentences[corpus.index(summary.__str__())] + "。" for summary in summaries]
