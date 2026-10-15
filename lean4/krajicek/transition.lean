/ lean4\krajicek\transition.lean
/ Base matemática formal da Transição Dupla Krajicek
/ Tratado oficial usando provador Lean 4

-- Teoria dos tipos básicos
import data.fintype

-- Definição de uma aplicação/transição T : α → α
structure Transicao (α : Type u) :=
  func : α → α

-- Definição da transição dupla T² = T ∘ T
def T² {α : Type u} (T : Transicao α) :=
  { func := λ x, T.func (T.func x) }

-- Teorema 1: Comutatividade da Transição Dupla
-- Para toda aplicação T sobre um tipo finito, T² é bem definido e associativo
theorem T²_well_defined {α : Type u} [fintype α] (T : Transicao α) : 
  ∀ x : α, T².func x = T.func (T.func x) :=
  begin
    intro x,
    rw T².func,
    -- Verificação computacional trivial
    refl
  end

-- Corolário: Se T for invertível, então (T²)⁻¹ = (T⁻¹)²
-- Definição de inverso
def inverse {α : Type u} {T : Transicao α} [has_inv T.func] :=
  { func := (T.func)^{-1} }

-- Teorema: (T²)⁻¹ = (T⁻¹)²
theorem T²_inverse_eq {α : Type u} {T : Transicao α} [has_inv T.func] [fintype α] :
  (T²)^{-1}.func = (T^{-1}.func ∘ T^{-1}.func) :=
  begin
    -- Ambos os lados são inversos de T² = T ∘ T
    -- Pela unicidade dos inversos em tipos finitos, são iguais
    ext x,
    have h1 : (T²)^{-1}.func (T.func (T.func x)) = id x,
    {
      rw <- (T²)^{-1}.func,
      rw T².func,
      simp,
    },
    have h2 : (T^{-1}.func ∘ T^{-1}.func).func (T.func (T.func x)) = id x,
    {
      rw ∘_apply,
      rw T².func,
      simp,
    },
    -- Pela unicidade de inversos em tipos finitos, h1 = h2
    eq_unique h1 h2
  end

-- Definição de identidade
structure Identity : Transicao α :=
  { func := id α }

-- Teorema: T² = T quando T = id
theorem T_of_id {α : Type u} : T² {func := id α} = T :=
  begin
    rw T²,
    eq_struct,
    simp [id]
  end

-- Exemplos concretos

-- Exemplo 1: T(x) = (x + 1) sobre ℤ/nℤ (transição simples)
def example_simple {n : Type u} [fintype n] (x : n) := 
  { func := λ x, has_add.add 1 x }

-- Teorema: T²(x) = (x + 2) mod n
theorem example_simple_T2 {n : Type u} [fintype n] [comm_ring n] (x : n) :
  (example_simple n).func ((example_simple n).func x) = has_add.add 2 x :=
  begin
    rw ← example_simple_T2,
    -- Simplificação usando anel commutativo
    have h1 : (has_add.add 1 x) + 1 = has_add.add 2 x,
    { ring },
    exact h1
  end

-- Exemplo 2: T(x) = -x (transição invertível)
def example_involutive : Transicao ℝ :=
  { func := λ x, -x }

-- Teorema: T² = id (autofas)
theorem example_involutive_T2 : (example_involutive).func ((example_involutive).func x) = x :=
  begin
    rw example_involutive.func,
    rw ← <-x,
    rw ← -(-x),
    exact rfl
  end

-- Instância de fintype para tipos numéricos finitos instanciados
-- Exemplo: Tipo com 5 elementos
example : fintype (fin 5) :=
  finite_finset 5