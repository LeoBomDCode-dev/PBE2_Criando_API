from sqlalchemy import TEXT, VARCHAR, BigInteger, SmallInteger, CHAR, DATE
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class usuario(Base):
    __tablename__ = "usuario"

    id_usuario: Mapped [int] = mapped_column(BigInteger, primary_key=True)
    nome: Mapped [str] = mapped_column(TEXT)
    cpf: Mapped [str] = mapped_column(CHAR(11), unique=True)
    data_nascimento: Mapped [DATE] = mapped_column(DATE)
    idade: Mapped [int] = mapped_column(SmallInteger)
    senha: Mapped [str] = mapped_column(CHAR(64))
    email: Mapped [str] = mapped_column(TEXT, unique=True)
    usuario: Mapped [str] = mapped_column(VARCHAR(50), unique=True)

