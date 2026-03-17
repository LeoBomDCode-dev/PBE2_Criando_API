from sqlalchemy import DECIMAL, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class passageiro(Base):
    __tablename__ = "passageiro"

    id_passageiro: Mapped [int] = mapped_column(BigInteger)
    media_avaliacao: Mapped [DECIMAL] = mapped_column(DECIMAL(3,2))
    
    
    ## foregn key
    id_usuario: Mapped [int] = mapped_column(BigInteger, ForeignKey("servico.id_servico",
    ondelete="CASCATE"), unique=True, nullable=False)