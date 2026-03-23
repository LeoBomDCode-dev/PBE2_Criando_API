from sqlalchemy import Integer, BigInteger, Float
from pydantic import BaseModel  


class motorista (BaseModel):
    motorista: Integer

    usuario: BigInteger
    media_avaliacao: Float
    cnh: BigInteger


class config:
        from_attributes = True