from sqlalchemy import BigInteger, DateTime, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class avaliacao(Base):
    __tablename__ = "Avaliacao"

    id_avaliacao: Mapped [int] = mapped_column(BigInteger, primary_key=True)
    nota_passageiro: Mapped [int] = mapped_column(SmallInteger)
    nota_motorista: Mapped [int] = mapped_column(SmallInteger)
    datahora_limite: Mapped [DateTime] = mapped_column(DateTime)
