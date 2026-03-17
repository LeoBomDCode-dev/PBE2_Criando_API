from sqlalchemy import VARCHAR, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class modo_pagamento(Base):
    __tablename__ = "modo_pagamento"

    id_modo_pagamento: Mapped [int] = mapped_column(SmallInteger, primary_key=True)
    descricao: Mapped [str] = mapped_column(VARCHAR(45))
    nome_financeira: Mapped [str] = mapped_column(VARCHAR(45))