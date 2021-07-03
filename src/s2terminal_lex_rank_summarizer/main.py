from .summarize import generateSummary
import fire

def main():
    fire.Fire(generateSummary)

if __name__ == "__main__":
    main()
