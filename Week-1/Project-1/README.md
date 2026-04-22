📁 1. filename="errors.log"
All logs will be saved in this file

✔ Creates/uses a file called:

errors.log

⚠️ 2. level=logging.ERROR
Only log ERROR and above

Logging levels in Python:

Level	Meaning
DEBUG	detailed info
INFO	normal messages
WARNING	something suspicious
ERROR	actual error
CRITICAL	serious failure

👉 Since you set ERROR, only:

ERROR
CRITICAL

will be saved.

🕒 3. format="..."

This controls how logs look

%(asctime)s - %(levelname)s - %(message)s

Means:

Part	Meaning
%(asctime)s	time of log
%(levelname)s	ERROR / INFO etc
%(message)s	actual log message
🧪 Example output in file
2026-04-21 10:15:30 - ERROR - File not found


cat errors.log--to list the error logs