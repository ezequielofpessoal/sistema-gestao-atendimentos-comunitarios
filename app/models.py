from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Beneficiario(Base):
    __tablename__ = "beneficiarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    cpf = Column(String(14), unique=True, index=True, nullable=False)  # CPF Único
    data_nascimento = Column(String(10), nullable=False)
    endereco = Column(String(200), nullable=False)
    data_cadastro = Column(DateTime, default=datetime.utcnow)

    atendimentos = relationship("Atendimento", back_populates="beneficiario", cascade="all, delete-orphan")

class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True)
    beneficiario_id = Column(Integer, ForeignKey("beneficiarios.id"), nullable=False)
    tipo_auxilio = Column(String(100), nullable=False)
    observacao = Column(Text, nullable=True)
    data_atendimento = Column(DateTime, default=datetime.utcnow)

    beneficiario = relationship("Beneficiario", back_populates="atendimentos")
