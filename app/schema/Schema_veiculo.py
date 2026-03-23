from sqlalchemy import Integer, BigInteger, SmallInteger, CHAR
from pydantic import BaseModel

class veiculo (BaseModel):
      veiculo: BigInteger

      placa: CHAR
      modelo: Integer   
      tem_seguro: SmallInteger
      classe: Integer

class config:
        from_attributes = True