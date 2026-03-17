
from sqlalchemy import DECIMAL, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class tipo_combustivel(Base):
    __tablename__ = "tipo combustivel"

    id_combustivel: Mapped [int] = mapped_column (primary_key=True)
    descricao: Mapped [str] = mapped_column (VARCHAR(45))
    fator_carbono: Mapped [DECIMAL] = mapped_column(DECIMAL(10,5))
