from pydantic import BaseModel, Field
from typing import Optional

class BeneficiarioCreate(BaseModel):
    nome: str = Field(..., min_length=3, max_length=120)
    cpf: str = Field(..., pattern=r"^\d{3}\.\d{3}\.\d{3}-\d{2}$")
    data_nascimento: str
    endereco: str = Field(..., min_length=5, max_length=200)

class AtendimentoCreate(BaseModel):
    beneficiario_id: int
    tipo_auxilio: str = Field(..., min_length=3, max_length=100)
    observacao: Optional[str] = None
