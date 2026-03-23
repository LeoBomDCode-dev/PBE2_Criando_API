from sqlalchemy import Integer,DateTime
from pydantic import BaseModel

class motorista_veiculo (BaseModel):
    motorista: Integer

    veiculo: Integer
    datahora_inicio: DateTime
    datahora_fim: DateTime

class config:
        from_attributes = True