from fastapi import FastAPI, Depends, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app import models, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Gestão de Atendimentos Comunitários")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Tela 1 — Login
@app.get("/", response_class=HTMLResponse)
def page_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login_action(usuario: str = Form(...), senha: str = Form(...)):
    # Autenticação demonstrativa simples
    if usuario == "operador.maria@ongexemplo.org.br" and senha == "SenhaSegura123#":
        return RedirectResponse(url="/busca-cadastro", status_code=status.HTTP_303_SEE_OTHER)
    return RedirectResponse(url="/?erro=credenciais", status_code=status.HTTP_303_SEE_OTHER)

# Tela 2 — Busca e Cadastro Único
@app.get("/busca-cadastro", response_class=HTMLResponse)
def page_busca_cadastro(request: Request, busca: str = None, db: Session = Depends(get_db)):
    resultados = []
    if busca:
        resultados = db.query(models.Beneficiario).filter(
            (models.Beneficiario.cpf == busca) | (models.Beneficiario.nome.ilike(f"%{busca}%"))
        ).all()
    return templates.TemplateResponse("busca_cadastro.html", {"request": request, "resultados": resultados, "busca": busca})

@app.post("/cadastrar-beneficiario")
def cadastrar_beneficiario(
    nome: str = Form(...),
    cpf: str = Form(...),
    data_nascimento: str = Form(...),
    endereco: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        dados = schemas.BeneficiarioCreate(
            nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco
        )
        novo = models.Beneficiario(**dados.model_dump())
        db.add(novo)
        db.commit()
        db.refresh(novo)
        return RedirectResponse(url=f"/historico/{novo.id}?sucesso=1", status_code=status.HTTP_303_SEE_OTHER)
    except Exception:
        db.rollback()
        return RedirectResponse(url="/busca-cadastro?erro=cpf_duplicado", status_code=status.HTTP_303_SEE_OTHER)

# Tela 3 — Histórico e Registro de Atendimento
@app.get("/historico/{beneficiario_id}", response_class=HTMLResponse)
def page_historico(request: Request, beneficiario_id: int, sucesso: int = 0, db: Session = Depends(get_db)):
    beneficiario = db.query(models.Beneficiario).filter(models.Beneficiario.id == beneficiario_id).first()
    if not beneficiario:
        raise HTTPException(status_code=404, detail="Beneficiário não encontrado")
    
    atendimentos = db.query(models.Atendimento).filter(
        models.Atendimento.beneficiario_id == beneficiario_id
    ).order_by(models.Atendimento.data_atendimento.desc()).all()

    return templates.TemplateResponse("historico.html", {
        "request": request,
        "beneficiario": beneficiario,
        "atendimentos": atendimentos,
        "sucesso": sucesso
    })

@app.post("/registrar-atendimento")
def registrar_atendimento(
    beneficiario_id: int = Form(...),
    tipo_auxilio: str = Form(...),
    observacao: str = Form(None),
    db: Session = Depends(get_db)
):
    atendimento = models.Atendimento(
        beneficiario_id=beneficiario_id,
        tipo_auxilio=tipo_auxilio,
        observacao=observacao
    )
    db.add(atendimento)
    db.commit()
    return RedirectResponse(url=f"/historico/{beneficiario_id}?sucesso=1", status_code=status.HTTP_303_SEE_OTHER)
