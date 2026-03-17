from sqlalchemy import DECIMAL, VARCHAR, BigInteger, DATETIME, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class corrida(Base):
    __tablename__ = "corrida"

    id_corrida: Mapped [int] = mapped_column(BigInteger, primary_key=True)
    datahora_incio: Mapped [DATETIME] = mapped_column(DATETIME)
    datahora_fim: Mapped [DATETIME] = mapped_column(DATETIME)
    local_partida: Mapped [str] = mapped_column(VARCHAR(50))
    local_destino: Mapped [str] = mapped_column(VARCHAR(50))
    valor_estimado: Mapped [DECIMAL] = mapped_column(DECIMAL(10,2))
    status: Mapped [Enum] = mapped_column(Enum ("Pendente","Em Andamento",
                                                "Concluida", "Cancelada"))
   
   ## foregn key
    id_motorista: Mapped [int] = mapped_column(BigInteger, ForeignKey('motorista.id_motorista', ondelete="CASCADE"), unique=True, nullable=False) 
    id_passageiro: Mapped [int] = mapped_column(BigInteger, ForeignKey('passsageiro.id_passageiro',ondeLete="CASCADE"), unique=True, nullable=False)
    id_servico: Mapped [int] = mapped_column(ForeignKey("servico.id_servico",
    ondelete="CASCATE"), unique=True, nullable=False)
    id_avaliacao: Mapped [int] = mapped_column(BigInteger, ForeignKey("avaliacao.id_avaliacao",ondelete="CASCATE"), unique=True, nullable=False)

    


