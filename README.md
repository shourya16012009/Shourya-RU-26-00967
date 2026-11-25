# Duplicate Data Finder

A simple Python 3 console application that reads a text file containing one entry per line, detects duplicate entries, reports their frequencies, and saves the unique entries to `unique.txt`.

## Features

- Reads entries from a text file (`data.txt` by default, or another filename entered by the user).
- Finds unique entries using a set.
- Counts duplicate entries.
- **Option 1 — Exact Match:** compares each line exactly as written.
- **Option 2 — Ignore Case and Extra Spaces:** ignores letter case and leading, trailing, or repeated spaces when comparing entries.
- Handles missing files with `try-except`.
- Detects empty files.
- Saves the first original version of each unique entry to `unique.txt`.

## Requirements

- Python 3
- No third-party packages are required.

## Project Structure

```text
Duplicate_Data_Finder/
├── duplicate_finder.py   # Main Python program
├── data.txt              # Input file (one entry per line)
├── unique.txt            # Generated output file
└── README.md             # Project documentation
```

`unique.txt` is created or overwritten when a comparison option is run.

## How to Run

1. Install Python 3.
2. Put `duplicate_finder.py` and your input text file in the same folder.
3. Open a terminal in that folder.
4. Run:

   ```bash
   python duplicate_finder.py
   ```

5. Enter the input filename when prompted (for example, `data.txt`).
6. Select a menu option:
   - `1` for exact matching.
   - `2` to ignore case and extra spaces.
   - `3` to exit.

## Input File Format

Each line in `data.txt` is treated as one entry.

Example:

```text
apple
banana
apple
orange
banana
apple
```

## Example Output

For the sample input above, choose **Option 1 — Exact Match**:

```text
Total items: 6
Unique items: 3
Duplicates: apple (3 times) | banana (2 times)
Unique list saved to unique.txt
```

The generated `unique.txt` contains:

```text
apple
banana
orange
```

## Comparison Modes

### Option 1: Exact Match

Entries are compared exactly. For example, `Apple`, `apple`, and `APPLE` are considered different entries.

### Option 2: Ignore Case and Extra Spaces

Entries are normalized for comparison by:
- Ignoring uppercase/lowercase differences.
- Removing leading and trailing spaces.
- Treating repeated spaces as a single space.

For example, `Apple`, `apple`, and ` APPLE ` are treated as the same entry. The first original version is written to `unique.txt`.

## Error Handling

- If the entered file does not exist, the program displays a file-not-found message.
- If the file is empty (or contains only blank/whitespace lines), the program displays `File is empty. Nothing to check.` and stops.

## Python Concepts Used

- **Lists:** store entries read from the input file.
- **Sets:** identify unique comparison keys.
- **Loops:** process entries and build the unique output.
- **File handling:** read the input and write the output.
- **try-except:** handle a missing input file.
- **Functions:** divide the program into manageable tasks.

## Test Cases

| Test case | Input / condition | Expected result |
|---|---|---|
| 1. Normal input | `apple`, `banana`, `apple`, `orange`, `banana`, `apple`; Option 1 | 6 total, 3 unique; apple appears 3 times and banana 2 times |
| 2. Minimum input | One line: `apple`; Option 1 | 1 total, 1 unique; no duplicates |
| 3a. Missing file | Enter `dta.txt` when it does not exist | File-not-found message |
| 3b. Empty file | An empty `data.txt` | Empty-file message |
| 4. Ignore case | `Apple`, `apple`, `banana`, `APPLE`; Option 2 | 4 total, 2 unique; apple appears 3 times |

## Limitations

- The program processes a plain text file with one entry per line.
- Blank lines inside a non-empty file are treated as entries.
- The output file `unique.txt` is overwritten each time a comparison is run.
- Option 2 normalizes spaces and case for comparison, but preserves the first original entry in the output file.

## Author

- Name: ____________________
- Roll Number: ____________________
- Class / Department: ____________________

## License

This project was created for educational use.
