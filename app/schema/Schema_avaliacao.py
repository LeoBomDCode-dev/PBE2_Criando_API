from sqlalchemy import SmallInteger, DateTime, Integer
from pydantic import BaseModel  


class avaliacao(BaseModel):
    id_classe: Integer
    
    nota_passageiro: SmallInteger
    nota_motorista: SmallInteger
    datahora_motorista: DateTime

    class config:
        from_attributes = True
