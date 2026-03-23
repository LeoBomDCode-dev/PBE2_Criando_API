from sqlalchemy import Float, Integer, VARCHAR
from pydantic import BaseModel  


class classe (BaseModel):
    id_classe: Integer

    nome_classe: VARCHAR
    fator_preço: Float


class config:
    from_attributes = True


    