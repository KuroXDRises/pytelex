# 🚀 MetaGram

> A modern, asynchronous Telegram Bot Framework for Python.

MetaGram is an easy-to-use, lightweight and powerful Telegram Bot framework inspired by the simplicity of Pyrogram while providing a clean API for building bots.

> ⚠️ **Current Status:** Beta Development (v1.0.0-beta.1)

---

## ✨ Features

- ⚡ Fully Asynchronous
- 📡 Long Polling
- 💬 Message Object
- 👤 User Object
- 🏠 Chat Object
- ↩️ Reply Messages
- ✏️ Edit Messages
- 🗑 Delete Messages
- 🖼 Unified Media Sender
- 📸 Photo Support
- 🎥 Video Support
- 🎵 Audio Support
- 🎙 Voice Support
- 📄 Document Support
- 🎞 Animation Support
- 😊 Sticker Support
- 🎯 Dispatcher
- 🔧 Handler System
- 🎛 Decorator API
- 🔍 Powerful Filters
- ➕ AND (`&`) Filters
- 🔀 OR (`|`) Filters
- 🚫 NOT (`~`) Filters
- 🏗 Custom Conditions

---

## 📦 Installation

```shell
pip install git+https://github.com/KuroXDRises/metagram
```

> Stable release is not available yet.

---

## 🚀 Quick Start

```python
from metagram import MetaClient, Conditions

app = MetaClient(
    bot_token="BOT_TOKEN"
)

@app.message_handler(
    Conditions.Command("start")
)
async def start(client, message):
    await message.reply("Hello from MetaGram!")

app.run()
```

---

## 📚 Documentation

Documentation is currently under development.

---

## 🛣 Roadmap

### ✅ Phase 1
- Core Framework
- Filters
- Media
- Dispatcher
- Handler System

### 🚧 Phase 2
- Chat Methods
- Member Methods
- Admin Methods
- Callback Queries
- Inline Keyboards

### 📅 Future
- Middleware
- Plugin Loader
- FSM
- Scheduler
- Webhook
- Logging

---

## 🤝 Contributing

Pull requests, ideas and bug reports are always welcome!

If you find a bug, please open an Issue.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**KuroXDRises**

GitHub:
https://github.com/KuroXDRises

---

⭐ If you like MetaGram, don't forget to Star the repository!
