from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base


class AnswerFeedback(Base):
    __tablename__ = "answer_feedbacks"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_answer_id: Mapped[int] = mapped_column(
        ForeignKey("user_answers.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    raw_ai_feedback: Mapped[str] = mapped_column(Text, nullable=False)
    response_in_session: Mapped[str] = mapped_column(Text, nullable=False)
    feedback_in_review: Mapped[str] = mapped_column(Text, nullable=False)
