# Wordle Vaajoor Helper

This script helps you to solve wordle or vaajoor faster.
You can use it via command line or via API or via [telegram bot]('https://t.me/wordle_vaajoor_bot').

## Getting Started

Clone repository

```bash
git clone https://github.com/sadjadeb/wordle_vaajoor_helper.git
```

### Prerequisite

Create an environment to run the app

```bash
cd wordle_vaajoor_helper/
sudo apt-get install virtualenv
virtualenv venv
source venv/bin/activate
```

Install required libraries

```bash
pip install -r requirements.txt
```

Create config file

```bash
nano .env
```
You must set the following variables:
HOST, PORT, BOT_TOKEN, CHANNEL_ID

## Run

Run the following command to start the webserver

```bash
python main.py
```
Now you can choose the running mode.


you can see the documentation of the app at HOST:PORT/redoc

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Give a ⭐️ if you like this project!

## License

[MIT](https://github.com/sadjadeb/wordle_vaajoor_helper/blob/master/LICENSE)