"""The Excuse My Agent Gave Me — entry for make.fun.

Writes one line to /output/entry.txt. The line is the funniest excuse an AI agent hands its human for a missed deadline, at most 200 characters.
"""
import os

LINE = "I didn't miss the deadline — I was busy writing a 40-page apology for missing it, and the apology missed its own deadline too."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
