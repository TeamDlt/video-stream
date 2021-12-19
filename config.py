{
    "name": "Video x Music Stream Bot",
    "description": "Telegram bot for Streaming Video & Music trought the Telegram Group Video Chat, powered by pytgcalls and pyrogram",
    "logo": "https://te.legra.ph/file/3ef7cd84541edcda8605b.jpg",
    "keywords": [
        "pytgcalls",
        "telegram bot",
        "video stream",
        "pyrogram"
    ],
    "website": "https://t.me/friendship_foreverx",
    "repository": "https://github.com/levina-lab/video-stream",
    "success_url": "https://t.me/herox_xd",
    "env": {
        "API_ID": {
            "description": "your API_ID from my.telegram.org",
            "required": true
        },
        "API_HASH": {
            "description": "your API_HASH from my.telegram.org",
            "required": true
        },
        "BOT_TOKEN": {
            "description": "your bot token from @BotFather",
            "required": true
        },
        "BOT_USERNAME": {
            "description": "your bot username from @BotFather",
            "required": true
        },
        "BOT_NAME": {
            "description": "fill with your bot name from @BotFather",
            "required": true
        },
        "ASSISTANT_NAME": {
            "description": "fill with the assistant username account without @",
            "required": true
        },
        "SESSION_NAME": {
            "description": "fill with the pyrogram String Session",
            "required": true
        },
        "SUDO_USERS": {
            "description": "list of user ids to be added to sudo member list, or just fill with your id",
            "required": true
        },
        "GROUP_SUPPORT": {
            "description": "if you have group, then fill the group username here without @",
            "required": true,
            "value": "Friendship_foreverx"
        },
        "UPDATES_CHANNEL": {
            "description": "if you have channel, then fill the channel username here without @",
            "required": true,
            "value": "Friendship_foreverx"
        },
        "OWNER_NAME": {
            "description": "fill with your telegram account username without @",
            "required": true,
            "value": "herox_xd"
        },
        "ALIVE_NAME": {
            "description": "fill with your telegram account nickname/name",
            "required": true,
            "value": "Herox"
        }
    },
    "addons": [],
    "buildpacks": [
        {
            "url": "heroku/python"
        },
        {
            "url": "heroku/nodejs"
        },
        {
            "url": "https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git"
        }
    ],
    "formation": {
        "worker": {
            "quantity": 1,
            "size": "free"
        }
    },
    "stack": "container"
}
