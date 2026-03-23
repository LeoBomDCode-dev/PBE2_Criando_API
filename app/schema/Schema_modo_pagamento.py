from sqlalchemy import Integer, DateTime, SmallInteger, BigInteger, Float
from pydantic import BaseModel  


class modo_pagamento (BaseModel):
    modo_pagamento: Integer

    corrida:BigInteger
    valor: Float
    metodo_pagamento: SmallInteger
    datahora_transacao: DateTime



class config:
        from_attributes = True