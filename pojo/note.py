class Note():
    def __init__(self, id, note_id, user_id, nickname, title, desc, liked_count, collected_count, comment_count):
        self.id = id
        self.note_id = note_id
        self.user_id = user_id
        self.nickname = nickname
        self.title = title
        self.desc = desc
        self.liked_count = liked_count
        self.collected_count = collected_count
        self.comment_count = comment_count

    def __str__(self):
        return f'id: {self.id}\n' \
               f'note_id: {self.note_id}\n' \
               f'user_id: {self.user_id}\n' \
               f'nickname: {self.nickname}\n' \
               f'title: {self.title}\n' \
               f'desc: {self.desc}\n' \
               f'liked_count: {self.liked_count}\n' \
               f'collected_count: {self.collected_count}\n' \
               f'comment_count: {self.comment_count}\n' \



