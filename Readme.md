## Installation
- Install packages from requirements.txt (*Hint: below install command*)
- Run command `python3 main.py`
- Run the script in cronjon.
    ### “At every 5th minute from 1 through 59 past every hour from 11 through 15.”
    ```
    1/5 11-15 * * * /usr/bin/python3 ~/dev/liveIndex/main.py
    ```

## Todos
- If change in points is greater than 40, send email to user notifying the bear or bull market.

### Requirements.txt
- `Export: ` pip3 freeze > requirements.txt
- `Install: ` pip3 install -r /path/to/requirements.txt

