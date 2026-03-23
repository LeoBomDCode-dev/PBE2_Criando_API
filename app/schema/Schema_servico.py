from sqlalchemy import Integer, VARCHAR
from pydantic import BaseModel  


class servico (BaseModel):
    servico: Integer

    nome_servico: VARCHAR
    classe_minima: Integer

class config:
        from_attributes = True