# pytelex/methods/chat/_promotechatmember.py


class PromoteChatMember:
    async def promote_chat_member(
        self,
        chat_id: int,
        user_id: int,
        is_anonymous: bool | None = None,
        can_manage_chat: bool | None = None,
        can_delete_messages: bool | None = None,
        can_manage_video_chats: bool | None = None,
        can_restrict_members: bool | None = None,
        can_promote_members: bool | None = None,
        can_change_info: bool | None = None,
        can_invite_users: bool | None = None,
        can_post_messages: bool | None = None,
        can_edit_messages: bool | None = None,
        can_pin_messages: bool | None = None,
        can_manage_topics: bool | None = None,
    ) -> bool:
        result = await self._invoke("promoteChatMember", {
            "chat_id":                chat_id,
            "user_id":                user_id,
            "is_anonymous":           is_anonymous,
            "can_manage_chat":        can_manage_chat,
            "can_delete_messages":    can_delete_messages,
            "can_manage_video_chats": can_manage_video_chats,
            "can_restrict_members":   can_restrict_members,
            "can_promote_members":    can_promote_members,
            "can_change_info":        can_change_info,
            "can_invite_users":       can_invite_users,
            "can_post_messages":      can_post_messages,
            "can_edit_messages":      can_edit_messages,
            "can_pin_messages":       can_pin_messages,
            "can_manage_topics":      can_manage_topics,
        })
        return result