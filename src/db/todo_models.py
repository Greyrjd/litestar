from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass

class TodoItem(Base):
    __tablename__ = 'todoitem'

    title: Mapped[str] = mapped_column(primary_key=True)
    done: Mapped[bool]

