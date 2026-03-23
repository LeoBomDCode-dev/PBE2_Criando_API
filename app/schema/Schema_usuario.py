from sqlalchemy import   VARCHAR,  DateTime, BigInteger, SmallInteger, Text
from pydantic import BaseModel

class usuario (BaseModel):
    usuario: BigInteger

    nome: Text
    cpf: VARCHAR
    data_nascimento: DateTime
    idade: SmallInteger
    Senha: VARCHAR
    email: Text 
    uusuario: VARCHAR


class config:
        from_attributes = True 