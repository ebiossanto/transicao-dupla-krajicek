"""Aplicação FastAPI - Transição Dupla Krajicek
Expor os serviços matemáticos como endpoints API REST.

Este módulo integra a formalização matemática (docs/formalization.md)
com uma API prática para consumo por clientes e interfaces.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from typing import Optional

from src.krajicek.math import (
    TransicaoDupla,
    transition_double,
    exemplo_transicao_simples,
    exemplo_identidade,
    exemplo_inverso,
)

app = FastAPI(
    title="Transição Dupla Krajicek API",
    description="" +
    "API REST que expõe os teoremas e funções da formalização matemática\n" +
    "da Transição Dupla Krajicek. Baseado em docs/formalization.md e\n" +
    "src/krajicek/math.py. Ideal para integração com interfaces e\n" +
    "outros serviços de cálculo.",
    version="0.1.0",
    contact={
        "name": "Projeto Transição Dupla Krajicek",
    }
)

# Endpoint raiz
@app.get("/", tags=["Root"])
async def root():
    """
    Retorna uma mensagem de boas-vindas e links para a documentação.
    """
    return {
        "message": "Bem-vindo à API Transição Dupla Krajicek",
        "version": "0.1.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# Endpoint: Transição Simples
@app.get(
    "/transicao/simples/{x}",
    response_model=int,
    tags=["Transição"],
    summary="Aplicar a transição simples T(x) = (x + 1) mod 10"
)
async def transicao_simples(x: int):
    """
    Aplica a função de transição simples: T(x) = (x + 1) mod 10.
    
    Este é o exemplo fundamental definido em docs/formalization.md.
    """
    return exemplo_transicao_simples(x)

# Endpoint: Transição Dupla (T²)
@app.get(
    "/transicao/dupla/{x}",
    response_model=int,
    tags=["Transição"],
    summary="Aplicar a transição dupla T²(x) = T(T(x))"
)
async def transicao_dupla(x: int):
    """
    Aplica a transição dupla T² = T ∘ T, conforme o Teorema 1
    (Comutatividade da Transição Dupla) definido em docs/formalization.md.
    
    Retorna o resultado de aplicar T duas vezes consecutivas.
    """
    td = transition_double(exemplo_transicao_simples)
    return td.compose()(x)

# Endpoint: Identidade
@app.get(
    "/identidade/{x}",
    response_model=int,
    tags=["Propriedades"],
    summary="Aplicar a função identidade T(x) = x"
)
async def funcao_identidade(x: int):
    """
    Retorna o resultado da função identidade, que é o próprio valor x.
    Usado como caso base e referência nos testes e provas.
    """
    return exemplo_identidade(x)

# Endpoint: Invertível
@app.get(
    "/invertido/{x}",
    response_model=int,
    tags=["Propriedades"],
    summary="Aplicar a função invertível T(x) = -x"
)
async def funcao_invertida(x: int):
    """
    Aplica a função invertível T(x) = -x.
    Conforme corolário: (T²)⁻¹ = (T⁻¹)² quando T é invertível.
    """
    return exemplo_inverso(x)

# Endpoint: Teorema da Comutatividade
@app.get(
    "/teorema/comutatividade/{x}",
    tags=["Teoremas"],
    summary="Verificar a propriedade T² = T ∘ T"
)
async def teorema_comutatividade(x: int):
    """
    Implementa e verifica a Teorema 1: Para toda aplicação T
    sobre um conjunto finito, T² = T ∘ T é associativa.
    
    Demonstração prática: T(T(x)) deve ser consistente independentemente
    da ordem de composição.
    """
    # Verificar a propriedade diretamente
    T = exemplo_transicao_simples
    td = transition_double(T)
    result_via_td = td.compose()(x)
    result_direto = T(T(x))
    
    if result_via_td != result_direto:
        raise HTTPException(
            status_code=500,
            detail="Falha na propriedade de comutatividade T² = T ∘ T"
        )
    
    return {
        "entrada": x,
        "T(T(x))": result_direto,
        "via TransicaoDupla": result_via_td,
        "propriedade_verificada": True
    }

# Exceção personalizada
@app.exception_handler(HTTPException)
async def custom_http_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "status": exc.status_code}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)