
from sqlalchemy import BigInteger, DateTime, SmallInteger,DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class pagamentos(Base):
    __tablename__ = "pagamentos"

    id_pagamentos: Mapped [int] = mapped_column(BigInteger, primary_key=True)
    valor: Mapped [DECIMAL] = mapped_column(DECIMAL (10,2))
    datahora_transacao: Mapped [DateTime] = mapped_column (DateTime)
   
   ##foregn key
    id_corrida: Mapped [int] = mapped_column(BigInteger, ForeignKey("servico.id_servico",
    ondelete="CASCATE"), unique=True, nullable=False)
    
    id_metodo_pagamento: Mapped [int] = mapped_column (SmallInteger, ForeignKey
    ("servico.id_servico", ondelete="CASCATE"), unique=True, nullable=False)