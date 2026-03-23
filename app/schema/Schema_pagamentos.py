from sqlalchemy import BigInteger,  DateTime, Float, SmallInteger
from pydantic import BaseModel  


class pagamentos (BaseModel):
    pagamentos: BigInteger

    corrida: BigInteger
    valor: Float
    metodo_pagamento: SmallInteger
    datahora_trnsacao: DateTime

class config:
        from_attributes = True