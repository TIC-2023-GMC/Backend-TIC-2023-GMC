from src.Interaction.Domain.Interaction import Interaction


class Comment(Interaction):
    _id: str
    user_first_name: str
    user_last_name: str
    comment_text: str
    comment_date: str
