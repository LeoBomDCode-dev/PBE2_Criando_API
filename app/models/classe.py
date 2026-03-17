from sqlalchemy import VARCHAR, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class classe(Base):
    __tablename__ = "classe"

    id_classe: Mapped [int] = mapped_column(primary_key=True)
    nome_classe: Mapped [str] = mapped_column (VARCHAR(45))
    fator_preco: Mapped [DECIMAL] = mapped_column (DECIMAL (10,2))


