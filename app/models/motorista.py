from sqlalchemy import DECIMAL, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base   

class motorista(Base):
    __tablename__ = "motorista"

    id_motorista: Mapped [int] = mapped_column(BigInteger, primary_key=True)
    media_avaliacao: Mapped [DECIMAL] = mapped_column (DECIMAL(3, 2))
    cnh: Mapped [int] = mapped_column (BigInteger)


##foregn key
    id_usuario: Mapped [int] = mapped_column(BigInteger, ForeignKey("servico.id_servico",
    ondelete="CASCATE"), unique=True, nullable=False)