"""
Testes unitários para a formalização matemática da Transição Dupla Krajicek.
Cobre os teoremas definidos em docs/formalization.md e a implementação em src/krajicek/math.py.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from krajicek.math import (
    TransicaoDupla,
    transition_double,
    exemplo_transicao_simples,
    exemplo_identidade,
    exemplo_inverso,
)


def test_transition_double_basic():
    """Testa a propriedade T^2 = T ∘ T para transição simples."""
    T = exemplo_transicao_simples
    td = transition_double(T)
    result = td.compose()(5)
    expected = T(T(5))
    assert result == expected, f"Falha: T(T(5)) = {result}, esperado {expected}"
    print("✓ test_transition_double_basic passed")


def test_transition_double_identity():
    """Testa a propriedade para função identidade."""
    T = exemplo_identidade
    td = transition_double(T)
    result = td.compose()(42)
    expected = T(T(42))
    assert result == expected, f"Falha: T(T(42)) = {result}, esperado {expected}"
    print("✓ test_transition_double_identity passed")


def test_transition_double_inverse():
    """Testa a propriedade para função invertível."""
    T = exemplo_inverso
    td = transition_double(T)
    result = td.compose()(10)
    expected = T(T(10))
    assert result == expected, f"Falha: T(T(10)) = {result}, esperado {expected}"
    print("✓ test_transition_double_inverse passed")


def test_transicao_dupla_class():
    """Testa a classe TransicaoDupla diretamente."""
    def func(x: int) -> int:
        return (x * 2) % 7
    
    td = TransicaoDupla(func)
    composed = td.compose()
    # T(T(x)) = ((x*2)%7 * 2) % 7
    result = composed.func(3)
    expected = func(func(3))
    assert result == expected, f"Falha: T(T(3)) = {result}, esperado {expected}"
    print("✓ test_transicao_dupla_class passed")


def test_transicao_dupla_equality():
    """Testa igualdade de transições dobradas."""
    td1 = transition_double(exemplo_transicao_simples)
    td2 = transition_double(exemplo_transicao_simples)
    assert td1 == td2, "Transições iguais deveriam ser iguais"
    
    def func2(x: int) -> int:
        return (x + 5) % 12
    td3 = transition_double(func2)
    assert td1 != td3, "Transições diferentes deveriam ser diferentes"
    print("✓ test_transicao_dupla_equality passed")


def test_composicao_associativa():
    """
    Testa a associatividade da composição: T^n aplicações consecutivas.
    Verifica que a classe TransicaoDupla suporta múltiplas composições.
    """
    T = exemplo_transicao_simples
    
    # T^3 = T ∘ T ∘ T aplicado diretamente
    result_direct = T(T(T(5)))
    assert result_direct == 8, f"T(T(T(5))) deveria ser 8, got {result_direct}"
    
    # Usando TransicaoDupla: compose() aplica T ∘ T (duas aplicações)
    td = transition_double(T)
    result_td2 = td.compose()(5)  # T(T(5)) = 7
    assert result_td2 == 7, f"td.compose()(5) deveria ser 7, got {result_td2}"
    
    # Verificar que compose().compose() dá T^4
    result_td4 = td.compose().compose()(5)  # T(T(T(T(5)))) = 9
    assert result_td4 == 9, f"td.compose().compose()(5) deveria ser 9, got {result_td4}"
    
    print("✓ test_composicao_associativa passed")


if __name__ == "__main__":
    print("=== Executando testes da Formalização Matemática ===\n")
    
    test_transition_double_basic()
    test_transition_double_identity()
    test_transition_double_inverse()
    test_transicao_dupla_class()
    test_transicao_dupla_equality()
    test_composicao_associativa()
    
    print("\n✅ Todos os testes passaram!")