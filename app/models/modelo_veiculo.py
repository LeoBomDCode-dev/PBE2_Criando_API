from sqlalchemy import VARCHAR, SmallInteger, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class modelo_veiculo(Base):
    __tablename__ = "modelo_veiculo"

    id_modelo: Mapped [int] = mapped_column(primary_key=True,)
    nome_modelo: Mapped [str] = mapped_column (VARCHAR(45))
    cor: Mapped [str] = mapped_column (VARCHAR(45))
    fabricante: Mapped [str] = mapped_column (VARCHAR(45))
    ano: Mapped [int] 
    capacidade: Mapped [int] = mapped_column (SmallInteger)
    propriedade: Mapped [Enum] = mapped_column(Enum ("Próprio", "Alugado"))
    
    
    ## foregn key
    id_combustivel: Mapped [int] =  mapped_column(ForeignKey("combustivel.id_combustivel",
    ondelete="CASCATE"), unique=True, nullable=False)