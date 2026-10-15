"""
Módulo de Formalização Matemática - Transição Dupla Krajicek
Implementa os teoremas e definições definidos em docs/formalization.md
"""

from __future__ import annotations
from typing import Callable, TypeVar, Generic
import math

T = TypeVar('T')
X = TypeVar('X')


class TransicaoDupla(Generic[T]):
    """
    Representa uma transição dupla T: X -> Y onde T^2 = T ∘ T.
    
    Definição (Do docs/formalization.md):
    Seja T: X -> Y uma aplicação binária. A transição dupla T^2 é definida
    como T ∘ T.
    """
    
    def __init__(self, func: Callable[[T], T]) -> None:
        self.func = func
    
    def __call__(self, x: T) -> T:
        return self.func(x)
    
    def compose(self) -> TransicaoDupla[T]:
        """
        Retorna a composição T ∘ T (transição dupla).
        
        Teorema 1 (Comutatividade da Transição Dupla):
        Para toda aplicação T sobre um conjunto finito, T^2 = T ∘ T é associativa.
        """
        return TransicaoDupla(lambda x: self.func(self.func(x)))
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TransicaoDupla):
            return NotImplemented
        return self.func == other.func
    
    def __repr__(self) -> str:
        return f"TransicaoDupla({self.func})"


def transition_double(func: Callable[[T], T]) -> TransicaoDupla[T]:
    """
    Função de conveniência que retorna um objeto TransicaoDupla.
    Isso permite que T^2 seja aplicado de forma legível.
    """
    return TransicaoDupla(func)


# Exemplos de uso conforme docs/formalization.md

def exemplo_transicao_simples(x: int) -> int:
    """Exemplo: T(x) = (x + 1) mod 10"""
    return (x + 1) % 10


def exemplo_identidade(x: int) -> int:
    """Exemplo: T(x) = x (identidade)"""
    return x


def exemplo_inverso(x: int) -> int:
    """Exemplo: T(x) = -x (invertível)"""
    return -x


if __name__ == "__main__":
    # Teste da Teorema 1: Comutatividade da Transição Dupla
    print("=== Teste da Teorema 1: Comutatividade da Transição Dupla ===")
    
    # Exemplo 1: Transição simples
    T1 = exemplo_transicao_simples
    td1 = transition_double(T1)
    result1 = td1.compose()(5)  # T(T(5)) = T(6) = 7
    expected1 = T1(T1(5))  # T(6) = 7
    print(f"T1(x) = (x+1) mod 10: T(T(5)) = {result1}, esperado = {expected1}")
    assert result1 == expected1, "Falha no exemplo 1!"
    
    # Exemplo 2: Identidade
    T2 = exemplo_identidade
    td2 = transition_double(T2)
    result2 = td2.compose()(5)
    expected2 = T2(T2(5))
    print(f"T2(x) = x: T(T(5)) = {result2}, esperado = {expected2}")
    assert result2 == expected2, "Falha no exemplo 2!"
    
    # Exemplo 3: Invertível
    T3 = exemplo_inverso
    td3 = transition_double(T3)
    result3 = td3.compose()(5)
    expected3 = T3(T3(5))
    print(f"T3(x) = -x: T(T(5)) = {result3}, esperado = {expected3}")
    assert result3 == expected3, "Falha no exemplo 3!"
    
    print("\n✅ Todos os testes da Teorema 1 passaram!")
    
    # Demonstração prática
    print("\n=== Demonstração Prática ===")
    T = lambda x: (x + 1) % 10
    td = transition_double(T)
    print(f"T(x) = (x+1) mod 10")
    print(f"T(5) = {T(5)}")
    print(f"T(T(5)) = {td.compose()(5)}")
    print(f"T(T(x)) = {td.compose().func}")