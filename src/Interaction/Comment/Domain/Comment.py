from datetime import date
from Interaction.Domain.Interaction import Interaction


class Comment(Interaction):
    comment_id: int
    comment_text: str
    comment_date: date
