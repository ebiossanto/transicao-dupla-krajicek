"""
Testes de integração da API FastAPI - Transição Dupla Krajicek.
Valida todos os endpoints expostos pela aplicação src/app.py.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from src.app import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root_endpoint():
    """Testa o endpoint raiz da API."""
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert data["message"] == "Bem-vindo à API Transição Dupla Krajicek"
    assert data["version"] == "0.1.0"
    assert "docs" in data
    assert "redoc" in data
    print("✓ test_root_endpoint passed")


def test_transicao_simples():
    """Testa a transição simples T(x) = (x + 1) mod 10."""
    resp = client.get("/transicao/simples/5")
    assert resp.status_code == 200
    assert resp.json() == 6  # T(5) = (5+1) % 10 = 6
    print("✓ test_transicao_simples passed")


def test_transicao_dupla():
    """Testa a transição dupla T²(x) = T(T(x))."""
    resp = client.get("/transicao/dupla/5")
    assert resp.status_code == 200
    assert resp.json() == 7  # T(T(5)) = T(6) = 7
    print("✓ test_transicao_dupla passed")


def test_identidade():
    """Testa a função identidade T(x) = x."""
    resp = client.get("/identidade/42")
    assert resp.status_code == 200
    assert resp.json() == 42
    print("✓ test_identidade passed")


def test_invertido():
    """Testa a função invertível T(x) = -x."""
    resp = client.get("/invertido/10")
    assert resp.status_code == 200
    assert resp.json() == -10
    print("✓ test_invertido passed")


def test_teorema_comutatividade():
    """Verifica a Teorema 1: T² = T ∘ T."""
    resp = client.get("/teorema/comutatividade/5")
    assert resp.status_code == 200
    data = resp.json()
    assert data["entrada"] == 5
    assert data["T(T(x))"] == 7
    assert data["via TransicaoDupla"] == 7
    assert data["propriedade_verificada"] == True
    print("✓ test_teorema_comutatividade passed")


def test_transicao_simples_outras_entradas():
    """Testa a transição simples com diferentes valores de entrada."""
    # T(0) = 1, T(9) = 0
    resp = client.get("/transicao/simples/0")
    assert resp.status_code == 200
    assert resp.json() == 1
    
    resp = client.get("/transicao/simples/9")
    assert resp.status_code == 200
    assert resp.json() == 0
    print("✓ test_transicao_simples_outras_entradas passed")


def test_teorema_comutatividade_outras_entradas():
    """Verifica a comutatividade com diferentes valores de entrada."""
    for x in [0, 1, 10, 100, -5]:
        resp = client.get(f"/teorema/comutatividade/{x}")
        assert resp.status_code == 200
        data = resp.json()
        assert data["propriedade_verificada"] == True, f"Falha para x={x}"
    print("✓ test_teorema_comutatividade_outras_entradas passed")