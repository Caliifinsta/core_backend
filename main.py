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

# CONFIGURACIÓN DE CORS RECOMENDADA PARA PRODUCCIÓN EN RENDER
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiado a "*" para permitir todas las conexiones de Vercel sin bloqueos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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