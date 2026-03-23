from sqlalchemy import BigInteger,  Float
from pydantic import BaseModel 


class passageiro (BaseModel):
    passageiro: BigInteger

    usuario: BigInteger
    media_avaliacao: Float 



class config:
        from_attributes = True