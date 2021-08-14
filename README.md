## Discord Mirror Listener

A skeleton bot which user can configure to watch for messages in channels, then do something with those messages.

### Setup

```bash
poetry install
```

Rename `.env.example` to `.env` and add your bot's token.

### Usage

Change the contents of `on_message` in listener cog to do something with the messages you are capturing.