from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import (
    rtr_scoring, rtr_creditos, rtr_ahorros,
    rtr_dashboard, rtr_clientes, rtr_auth, rtr_homebanking, rtr_recuperaciones,
)

app = FastAPI(
    title="Core Financiero — Banco Ripley",
    description="Motor de scoring, cartera crediticia y KPIs institucionales",
    version="1.0.0"
)

# CONFIGURACIÓN DE CORS RESTRINGIDA Y SEGURA
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",                 # Para que puedas seguir probando en tu computadora
        "https://core-fromd.vercel.app"          # Tu link oficial de Vercel en producción
    ],
    allow_credentials=True,
    allow_methods=["*"],                         # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],                         # Permite todos los headers necesarios (como los tokens)
)

# Inclusión de Routers (Tus prefijos y etiquetas están perfectos)
app.include_router(rtr_auth.router,      prefix="/auth",      tags=["Auth"])
app.include_router(rtr_scoring.router,   prefix="/scoring",   tags=["Scoring"])
app.include_router(rtr_creditos.router,  prefix="/creditos",  tags=["Créditos"])
app.include_router(rtr_ahorros.router,   prefix="/ahorros",   tags=["Ahorros"])
app.include_router(rtr_clientes.router,  prefix="/clientes",  tags=["Clientes"])
app.include_router(rtr_dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(rtr_homebanking.router, prefix="/hb",       tags=["Homebanking"])
app.include_router(rtr_recuperaciones.router, prefix="/recuperaciones", tags=["Recuperaciones"])

@app.get("/")
def root():
    return {"sistema": "Core Financiero Banco Ripley", "version": "1.0.0", "status": "ok"}
