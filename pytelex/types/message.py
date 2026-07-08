# pytelex/types/message.py

from .object import Object
from .chat import Chat
from .user import User
from .photo_size import PhotoSize


class Message(Object):
    def __init__(
        self,
        *,
        client=None,
        id=None,
        from_user=None,
        chat=None,
        date=None,
        edit_date=None,
        text=None,
        caption=None,
        photo=None,
        video=None,
        voice=None,
        audio=None,
        document=None,
        sticker=None,
        animation=None,
        video_note=None,
        poll=None,
        dice=None,
        entities=None,
        caption_entities=None,
        reply_to_message=None,
        forward_from=None,
        forward_from_chat=None,
        forward_date=None,
        pinned_message=None,
        new_chat_members=None,
        left_chat_member=None,
        reply_markup=None,
    ):
        super().__init__(client)
        self.id = id
        self.from_user = from_user
        self.chat = chat
        self.date = date
        self.edit_date = edit_date
        self.text = text
        self.caption = caption
        self.photo = photo
        self.video = video
        self.voice = voice
        self.audio = audio
        self.document = document
        self.sticker = sticker
        self.animation = animation
        self.video_note = video_note
        self.poll = poll
        self.dice = dice
        self.entities = entities
        self.caption_entities = caption_entities
        self.reply_to_message = reply_to_message
        self.forward_from = forward_from
        self.forward_from_chat = forward_from_chat
        self.forward_date = forward_date
        self.pinned_message = pinned_message
        self.new_chat_members = new_chat_members
        self.left_chat_member = left_chat_member
        self.reply_markup = reply_markup

    @classmethod
    def _parse(cls, client, data: dict):
        if not data:
            return None

        photo = None
        if data.get("photo"):
            photo = [PhotoSize._parse(client, p) for p in data["photo"]]

        new_chat_members = None
        if data.get("new_chat_members"):
            new_chat_members = [User._parse(client, u) for u in data["new_chat_members"]]

        reply_to_message = None
        if data.get("reply_to_message"):
            reply_to_message = cls._parse(client, data["reply_to_message"])

        pinned_message = None
        if data.get("pinned_message"):
            pinned_message = cls._parse(client, data["pinned_message"])

        return cls(
            client=client,
            id=data.get("message_id"),
            from_user=User._parse(client, data.get("from")),
            chat=Chat._parse(client, data.get("chat")),
            date=data.get("date"),
            edit_date=data.get("edit_date"),
            text=data.get("text"),
            caption=data.get("caption"),
            photo=photo,
            video=data.get("video"),
            voice=data.get("voice"),
            audio=data.get("audio"),
            document=data.get("document"),
            sticker=data.get("sticker"),
            animation=data.get("animation"),
            video_note=data.get("video_note"),
            poll=data.get("poll"),
            dice=data.get("dice"),
            entities=data.get("entities"),
            caption_entities=data.get("caption_entities"),
            reply_to_message=reply_to_message,
            forward_from=User._parse(client, data.get("forward_from")),
            forward_from_chat=Chat._parse(client, data.get("forward_from_chat")),
            forward_date=data.get("forward_date"),
            pinned_message=pinned_message,
            new_chat_members=new_chat_members,
            left_chat_member=User._parse(client, data.get("left_chat_member")),
            reply_markup=data.get("reply_markup"),
        )

    async def reply(
        self,
        text: str,
        business_connection_id: str | None = None,
        message_thread_id: int | None = None,
        parse_mode: str | None = None,
        entities: list | None = None,
        link_preview_options: dict | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        allow_paid_broadcast: bool | None = None,
        message_effect_id: str | None = None,
        reply_markup=None,
    ):
        return await self._client.send_message(
            chat_id=self.chat.id,
            text=text,
            reply_parameters={"message_id": self.id},
            parse_mode=parse_mode,
            business_connection_id=business_connection_id,
            message_thread_id=message_thread_id,
            message_effect_id=message_effect_id,
            entities=entities,
            link_preview_options=link_preview_options,
            disable_notification=disable_notification,
            protect_content=protect_content,
            allow_paid_broadcast=allow_paid_broadcast,
            reply_markup=reply_markup
        )

    async def reply_media(
        self,
        media_type: str,
        media,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities=None,
        disable_notification: bool = False,
        protect_content: bool = False,
        reply_markup=None,
        **extra_kwargs
    ):
        return await self._client.send_media(
            media_type=media_type,
            media=media,
            chat_id=self.chat.id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_markup=reply_markup,
            **extra_kwargs
        )

    async def delete(self):
        return await self._client.delete_message(
            chat_id=self.chat.id,
            message_id=self.id
        )

    async def edit(
        text:str,
        parse_mode: str | None = None,
        entities: list | None = None,
        link_preview_options=None,
        reply_markup=None,
    ):
        return await self._client.edit_message_text(
            chat_id=m.chat.id,
            message_id=self.id,
            text=text,
            parse_mode=parse_mode,
            entities=entities,
            link_preview_options=link_preview_options,
            reply_markup=reply_markup
        )

    async def forward(
        self,
        chat_id:int
    ):
        return await self._client.forward_message(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            message_id=self.id
        )

    async def edit_caption(
        self,
        caption: str = None,
        parse_mode = None,
        caption_entities = None,
        reply_markup = None
    ):
        return await self._client.edit_message_caption(
            chat_id=self.chat.id,
            message_id=self.id,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            reply_markup=reply_markup
        )
    
    async def copy(
        self,
        chat_id:int
    ):
        return await self._client.copy_message(
            chat_id=chat_id,
            from_chat_id=self.chat.id,
            message_id=self.id
        )

    async def pin(
        self,
        disable_notification=False
    ):
        return await self._client.pin_chat_message(
            chat_id=self.chat.id,
            message_id=self.id,
            disable_notification=disable_notification
        )

    async def unpin(self):
        return await self._client.unpin_chat_message(
            chat_id=self.chat.id,
            message_id=self.id
        )