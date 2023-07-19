from src.Interaction.Domain.Interaction import Interaction


class Comment(Interaction):
    _id: str
    comment_text: str
    comment_date: str
