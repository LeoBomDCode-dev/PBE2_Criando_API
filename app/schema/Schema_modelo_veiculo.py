from sqlalchemy import Integer, VARCHAR,  DateTime, Enum, SmallInteger
from pydantic import BaseModel  


class modelo_veiculo (BaseModel):
    modelo_veiculo: Integer

    nome_modelo: VARCHAR
    cor: VARCHAR
    fabricante: VARCHAR
    ano: DateTime
    capacidade: SmallInteger
    propriedade: Enum
    
    id_combustivel: Integer



class config:
        from_attributes = True