from s2terminal_lex_rank_summarizer import __version__
from s2terminal_lex_rank_summarizer.summarize import generateSummary

def test_version():
    assert __version__ == '0.1.1'

def test_generateSummary():
    text = "おはようございます。こんにちは。こんばんは。"
    count = 3
    results = generateSummary(text, count)

    assert len(results) == count
    for result in results:
        assert result in text
