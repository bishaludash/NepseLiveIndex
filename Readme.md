## Installation
- Install packages from requirements.txt (*Hint: below install command*)
- Run command `python3 main.py`
- Add an alias in `~/.bashrc` file execute everything via a command
    ```
    alias nepse='python3 /path/tofile/liveIndex/main.py'
    ```
## Todos
- At the moment, the index difference is calculated as (`TodaysStartIndex - TodaysLastIndex`).
Update it to (`YesterdaysLastIndex - TodaysLastIndex`)
- If change in points is greater than 40, send email to user notifying the bear or bull market.
- Run the script in cronjon.(*Note: after notifying is enabled*)
    ### “At every 5th minute from 1 through 59 past every hour from 11 through 15.”
    ```
    1/5 11-15 * * * /usr/bin/python3 ~/dev/liveIndex/main.py
    ```
### Requirements.txt
- `Export:`  pip3 freeze > requirements.txt
- `Install:`  pip3 install -r /path/to/requirements.txt
