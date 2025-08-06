# ReworkBStag

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)

Python implementation of Brawl Stars tag converter, originally based on [NotCat40/BrawlStarsTagGenerator](https://github.com/NotCat40/BrawlStarsTagGenerator).

## About

This tool converts between numeric IDs and hashtag codes used in Brawl Stars (like #QYUURGGQ). It's a reworked version of the original PowerShell module converted to clean, efficient Python code.

## Features

- Convert numeric IDs to Brawl Stars hashtag format
- Convert hashtag codes back to numeric IDs
- Simple command-line interface
- Error handling for invalid inputs

## Usage

1. Run the script:
```bash
python reworkbstag.py
```

2. Choose conversion direction:
```
Brawl Stars Tag Converter
1. Convert ID to hashtag
2. Convert hashtag to ID

Choose option (1/2): 
```

3. Follow the prompts to enter your ID or hashtag.

### Example 1: ID to Hashtag
```
Choose option (1/2): 1
Enter ID number: 3056576
Enter High ID (default 0): 15

Hashtag: #QYUURGGQ
```

### Example 2: Hashtag to ID
```
Choose option (1/2): 2
Enter hashtag (e.g. #QYUURGGQ): #QYUURGGQ

High: 15, Low: 3056576
```

## Installation

No installation required - just download `reworkbstag.py` and run it with Python 3.

## License

This project is licensed under the MIT License.
