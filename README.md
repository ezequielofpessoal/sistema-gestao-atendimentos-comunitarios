# sistema-gestao-atendimentos-comunitarios
MVP de Sistema de Gestão de Atendimentos Comunitários para ONGs e Instituições Sociais. Desenvolvido com Python 3.12 (FastAPI), SQLAlchemy, PostgreSQL (Supabase) e Bootstrap 5.3, com foco em segurança (OWASP Top 10) e acessibilidade (WCAG 2.1 AA / ODS 9).


sistema-gestao-atendimentos-comunitarios/
│
├── app/
│   ├── __init__.py
│   ├── database.py         # Conexão SQLAlchemy e Supabase (PostgreSQL)
│   ├── models.py           # Entidades beneficiarios e atendimentos (ORM)
│   ├── schemas.py          # Validação de dados (Pydantic / OWASP)
│   ├── security.py         # Hashing de senha com Argon2 e tokens de sessão
│   ├── main.py             # Rotas FastAPI e rotas das páginas Jinja2
│
├── templates/              # Camada de Visão (Jinja2 + Bootstrap 5.3)
│   ├── base.html           # Layout base (Navbar, CSS, JS e acessibilidade RNF04)
│   ├── login.html          # Tela 1 — Entrada e Autenticação
│   ├── busca_cadastro.html # Tela 2 — Cadastro Único e Busca Rápida
│   └── historico.html      # Tela 3 — Perfil, Histórico e Novo Atendimento
│
├── static/
│   ├── css/
│   │   └── style.css       # Estilos customizados (Contraste 4.5:1, foco 2px, touch targets 48px)
│   └── js/
│       └── main.js         # Scripts auxiliares e máscaras de CPF
│
├── .env.example            # Modelo de variáveis de ambiente
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação técnica do projeto
