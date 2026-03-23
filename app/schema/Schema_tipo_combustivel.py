from sqlalchemy import Integer, VARCHAR, Float
from pydantic import BaseModel  


class tipo_combustivel (BaseModel):
    tipo_combustivel: Integer

    descricao: VARCHAR
    fator_carbono: Float

class config:
        from_attributes = True