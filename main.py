import sys
from shift import shift_subtitles

def main():
    if len(sys.argv) != 3:
        print(f"Correct usage: python3 main.py </path/to/SubRip/file> <shift>")
        return

    shift_subtitles(sys.argv[1], float(sys.argv[2]))


if __name__ == "__main__":
    main()
