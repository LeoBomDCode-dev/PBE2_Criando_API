from sqlalchemy import ForeignKey, SmallInteger, CHAR
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base


class veiculo(Base):
    __tablename__ = "veiculo" 

    id_veiculo: Mapped [int] = mapped_column(primary_key=True)
    placa: Mapped [str] = mapped_column(CHAR(7))
    tem_seguro: Mapped[str] = mapped_column(SmallInteger)

    ##foregn key
    id_modelo: Mapped[int] = mapped_column(ForeignKey("servico.id_servico",
    ondelete="CASCATE"), unique=True, nullable=False)
    
    id_class: Mapped[int] = mapped_column (ForeignKey("servico.id_servico",
    ondelete="CASCATE"), unique=True, nullable=False)