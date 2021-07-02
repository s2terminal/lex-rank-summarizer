from src.lex_rank_summarizer.summarize import generateSummary
import fire

def main():
    fire.Fire(generateSummary)

if __name__ == "__main__":
    main()
