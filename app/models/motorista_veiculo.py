from sqlalchemy import DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class motorista_objeto(Base):
    __tablename__ = "motorista_objeto"

    id_datahora_inicio: Mapped [DATETIME] = mapped_column(DATETIME)
    id_datahota_final: Mapped  [DATETIME] = mapped_column(DATETIME)
##foregn key
    id_motorista: Mapped [int] = mapped_column( ForeignKey("motorista."
    "id_motorista",ondelete="CASCATE"), unique=True, nullable=False, primary_key=True)
    
    id_veiculo: Mapped [int] = mapped_column(ForeignKey("servico.id_servico",
    ondelete="CASCATE"), unique=True, nullable=False, primary_key=True)