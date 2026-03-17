from sqlalchemy import VARCHAR, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class servico(Base):
    __tablename__ = "servico"

    id_servico: Mapped [int] = mapped_column (primary_key=True)
    nome_servico: Mapped [str] = mapped_column (VARCHAR(50))

## foregn key
    id_classe_minima: Mapped [int] = mapped_column (ForeignKey("servico.id_servico",
    ondelete="CASCATE"), unique=True, nullable=False)