from sqlalchemy import Float, Integer, VARCHAR, BigInteger, DateTime, Enum
from pydantic import BaseModel  


class corrida (BaseModel):
    id_corrida: Integer

    id_passageiro: Integer
    id_motorista: BigInteger
    id_servico: Integer
    id_avaliacao: BigInteger
    datahora_inicio: DateTime
    datahora_fim: DateTime
    local_partida: VARCHAR
    local_destino: VARCHAR
    valor_estimado: Float
    status: Enum

class config:
    from_attributes = True