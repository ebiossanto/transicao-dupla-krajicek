# **Derivação das fórmulas-ponte por uma dinâmica natural**

## **Modelo estocástico de dupla porta para estimação e controle preditivo em rede**

Bom dia, Euzebio. O ponto decisivo era explicar, sem simplesmente postular, por que uma dinâmica realista poderia produzir simultaneamente

D(ρ)=ρ1−ρp2eF(ρ)=ρ1−ρe2.D(\\rho)=\\frac{\\rho}{1-\\rho}p^2 \\qquad\\text{e}\\qquad F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2.D(ρ)=1−ρρ​p2eF(ρ)=1−ρρ​​e2.

A derivação abaixo consegue isso em um domínio relevante: **estimação e controle distribuído através de uma rede com duas etapas de disponibilidade**, como sensor →\\rightarrow→ estimador e estimador →\\rightarrow→ atuador. A raiz quadrada não será introduzida artificialmente. Ela surgirá porque uma perturbação preditiva atravessa uma porta, enquanto a persistência completa do erro exige que duas portas estejam simultaneamente abertas.

Modelos de estimação com observações intermitentes normalmente representam a chegada de pacotes por variáveis de Bernoulli e estudam a evolução da covariância do erro. Perdas, atrasos e disponibilidade aleatória dos canais são problemas estabelecidos em redes de sensores e controle distribuído. [\[arxiv.org\]](https://arxiv.org/pdf/0903.2890.pdf), [\[people.eec...rkeley.edu\]](https://people.eecs.berkeley.edu/~jordan/papers/CDC2003Kalman.pdf), [\[people.eec...rkeley.edu\]](https://people.eecs.berkeley.edu/~jordan/papers/sinopoli-etal.pdf)

---

# **1\. Domínio de aplicação**

Considere um sistema distribuído com três componentes:

1. um sensor ou produtor de informação;  
2. um estimador ou controlador;  
3. um atuador, consumidor ou estágio seguinte.

Em cada instante ttt, a informação precisa atravessar duas portas:

* **porta de aquisição**  
   Ut∈{0,1};U\_t\\in\\{0,1\\};Ut​∈{0,1};  
* **porta de confirmação ou atuação**  
   Vt∈{0,1}.V\_t\\in\\{0,1\\}.Vt​∈{0,1}.

A interpretação é:

Ut=1U\_t=1Ut​=1

se a observação chega ao estimador, e

Vt=1V\_t=1Vt​=1

se a decisão resultante é validada, transmitida ou efetivada no estágio seguinte.

Assumiremos inicialmente:

Ut∼Bernoulli⁡(s),Vt∼Bernoulli⁡(s),U\_t\\sim\\operatorname{Bernoulli}(s), \\qquad V\_t\\sim\\operatorname{Bernoulli}(s),Ut​∼Bernoulli(s),Vt​∼Bernoulli(s),

independentes, com:

0\<s\<1.0\<s\<1.0\<s\<1.

Também assumimos independência temporal:

(Ut,Vt)⊥(Uj,Vj)para t≠j.(U\_t,V\_t)\\perp(U\_j,V\_j) \\qquad\\text{para }t\\ne j.(Ut​,Vt​)⊥(Uj​,Vj​)para t=j.

A disponibilidade fim a fim é:

Bt=UtVt.B\_t=U\_tV\_t.Bt​=Ut​Vt​.

Como as portas são independentes:

Pr⁡(Bt=1)=Pr⁡(Ut=1,Vt=1)=s2.\\Pr(B\_t=1) \= \\Pr(U\_t=1,V\_t=1) \= s^2.Pr(Bt​=1)=Pr(Ut​=1,Vt​=1)=s2.

Definimos:

ρ=s2.\\boxed{\\rho=s^2.}ρ=s2.​

Assim:

s=ρ.\\boxed{s=\\sqrt\\rho.}s=ρ​.​

## **Interpretação correta de ρ\\rhoρ**

Nesta derivação, ρ\\rhoρ não deve ser chamado genericamente de “utilização” sem qualificação. Ele representa:

probabilidade de persisteˆncia ou exposic¸a˜o fim a fim atraveˊs das duas portas.\\boxed{\\text{probabilidade de persistência ou exposição fim a fim através das duas portas}.}probabilidade de persisteˆncia ou exposic¸​a˜o fim a fim atraveˊs das duas portas.​

Em uma aplicação concreta, ρ\\rhoρ poderá coincidir com uma carga operacional apenas se essa equivalência for demonstrada.

A disponibilidade aleatória de canais de sensor, controlador e atuador é uma hipótese natural em controle por rede. Trabalhos em controle preditivo e filtragem distribuída tratam explicitamente de atrasos aleatórios, perda de pacotes e múltiplos canais de comunicação. [\[ieeexplore.ieee.org\]](https://ieeexplore.ieee.org/document/9767785), [\[mdpi.com\]](https://www.mdpi.com/2624-6120/7/1/9/pdf), [\[arxiv.org\]](https://arxiv.org/html/2309.01679v2)

---

# **2\. Variáveis de erro**

Considere duas sequências de inovações centradas:

ξt,ηt.\\xi\_t, \\qquad \\eta\_t.ξt​,ηt​.

Assumimos:

E\[ξt\]=0,E\[ηt\]=0,\\mathbb E\[\\xi\_t\]=0, \\qquad \\mathbb E\[\\eta\_t\]=0,E\[ξt​\]=0,E\[ηt​\]=0, Var⁡(ξt)=p2,Var⁡(ηt)=e2.\\operatorname{Var}(\\xi\_t)=p^2, \\qquad \\operatorname{Var}(\\eta\_t)=e^2.Var(ξt​)=p2,Var(ηt​)=e2.

As sequências são independentes entre si, independentes no tempo e independentes das portas Ut,VtU\_t,V\_tUt​,Vt​.

A variável ξt\\xi\_tξt​ representa uma inovação ou perturbação residual no mecanismo DFA.

A variável ηt\\eta\_tηt​ representa o erro residual da previsão PFA.

Como aparecem variâncias, ppp e eee podem ser interpretados como desvios quadráticos médios, RMSEs normalizados ou escalas de erro cuja unidade ao quadrado corresponde à energia ou variância analisada.

---

# **3\. Dinâmica natural do DFA**

## **3.1 Recursão DFA**

Defina o erro acumulado DFA por:

Xt+1=Bt(Xt+ξt).\\boxed{ X\_{t+1} \= B\_t(X\_t+\\xi\_t). }Xt+1​=Bt​(Xt​+ξt​).​

Essa dinâmica expressa duas propriedades:

1. o erro anterior persiste somente quando a cadeia fim a fim está ativa;  
2. uma nova perturbação DFA é efetivada somente após a passagem completa pelas duas portas.

Como:

Bt=UtVt,B\_t=U\_tV\_t,Bt​=Ut​Vt​,

o erro DFA entra no sistema apenas quando a aquisição e a confirmação ocorrem.

---

## **3.2 Média do processo DFA**

Se:

E\[X0\]=0,\\mathbb E\[X\_0\]=0,E\[X0​\]=0,

então:

E\[Xt+1\]=E\[BtXt\]+E\[Btξt\].\\mathbb E\[X\_{t+1}\] \= \\mathbb E\[B\_tX\_t\] \+ \\mathbb E\[B\_t\\xi\_t\].E\[Xt+1​\]=E\[Bt​Xt​\]+E\[Bt​ξt​\].

Pela independência:

E\[BtXt\]=E\[Bt\]E\[Xt\],\\mathbb E\[B\_tX\_t\] \= \\mathbb E\[B\_t\]\\mathbb E\[X\_t\],E\[Bt​Xt​\]=E\[Bt​\]E\[Xt​\],

e:

E\[Btξt\]=E\[Bt\]E\[ξt\]=0.\\mathbb E\[B\_t\\xi\_t\] \= \\mathbb E\[B\_t\]\\mathbb E\[\\xi\_t\] \= 0.E\[Bt​ξt​\]=E\[Bt​\]E\[ξt​\]=0.

Portanto:

E\[Xt+1\]=ρ E\[Xt\].\\mathbb E\[X\_{t+1}\] \= \\rho\\,\\mathbb E\[X\_t\].E\[Xt+1​\]=ρE\[Xt​\].

Como a média inicial é zero:

E\[Xt\]=0\\boxed{\\mathbb E\[X\_t\]=0}E\[Xt​\]=0​

para todo ttt.

---

## **3.3 Recorrência da variância DFA**

Como a média é zero:

Var⁡(Xt)=E\[Xt2\].\\operatorname{Var}(X\_t)=\\mathbb E\[X\_t^2\].Var(Xt​)=E\[Xt2​\].

Elevando a dinâmica ao quadrado:

Xt+12=Bt2(Xt+ξt)2.X\_{t+1}^2 \= B\_t^2(X\_t+\\xi\_t)^2.Xt+12​=Bt2​(Xt​+ξt​)2.

Como Bt∈{0,1}B\_t\\in\\{0,1\\}Bt​∈{0,1}:

Bt2=Bt.B\_t^2=B\_t.Bt2​=Bt​.

Logo:

Xt+12=Bt(Xt2+2Xtξt+ξt2).X\_{t+1}^2 \= B\_t \\left( X\_t^2+2X\_t\\xi\_t+\\xi\_t^2 \\right).Xt+12​=Bt​(Xt2​+2Xt​ξt​+ξt2​).

Tomando esperança:

E\[Xt+12\]=E\[BtXt2\]+2E\[BtXtξt\]+E\[Btξt2\].\\mathbb E\[X\_{t+1}^2\] \= \\mathbb E\[B\_tX\_t^2\] \+ 2\\mathbb E\[B\_tX\_t\\xi\_t\] \+ \\mathbb E\[B\_t\\xi\_t^2\].E\[Xt+12​\]=E\[Bt​Xt2​\]+2E\[Bt​Xt​ξt​\]+E\[Bt​ξt2​\].

Pela independência e pela centralidade de ξt\\xi\_tξt​:

E\[BtXtξt\]=E\[Bt\]E\[Xt\]E\[ξt\]=0.\\mathbb E\[B\_tX\_t\\xi\_t\] \= \\mathbb E\[B\_t\] \\mathbb E\[X\_t\] \\mathbb E\[\\xi\_t\] \= 0.E\[Bt​Xt​ξt​\]=E\[Bt​\]E\[Xt​\]E\[ξt​\]=0.

Além disso:

E\[BtXt2\]=E\[Bt\]E\[Xt2\]=ρ E\[Xt2\],\\mathbb E\[B\_tX\_t^2\] \= \\mathbb E\[B\_t\]\\mathbb E\[X\_t^2\] \= \\rho\\,\\mathbb E\[X\_t^2\],E\[Bt​Xt2​\]=E\[Bt​\]E\[Xt2​\]=ρE\[Xt2​\],

e:

E\[Btξt2\]=E\[Bt\]E\[ξt2\]=ρp2.\\mathbb E\[B\_t\\xi\_t^2\] \= \\mathbb E\[B\_t\]\\mathbb E\[\\xi\_t^2\] \= \\rho p^2.E\[Bt​ξt2​\]=E\[Bt​\]E\[ξt2​\]=ρp2.

Definindo:

Dt=Var⁡(Xt),D\_t=\\operatorname{Var}(X\_t),Dt​=Var(Xt​),

obtemos:

Dt+1=ρDt+ρp2.\\boxed{ D\_{t+1} \= \\rho D\_t+\\rho p^2. }Dt+1​=ρDt​+ρp2.​

Essa é a recursão geométrica que antes aparecia apenas como hipótese.

---

# **4\. Solução exata da dinâmica DFA**

Iterando:

Dt+1=ρDt+ρp2.D\_{t+1} \= \\rho D\_t+\\rho p^2.Dt+1​=ρDt​+ρp2.

Para D0≥0D\_0\\ge0D0​≥0:

Dt=ρtD0+p2∑j=1tρj.D\_t \= \\rho^tD\_0 \+ p^2\\sum\_{j=1}^{t}\\rho^j.Dt​=ρtD0​+p2j=1∑t​ρj.

Como:

∑j=1tρj=ρ(1−ρt)1−ρ,\\sum\_{j=1}^{t}\\rho^j \= \\frac{\\rho(1-\\rho^t)}{1-\\rho},j=1∑t​ρj=1−ρρ(1−ρt)​,

temos:

Dt=ρtD0+ρ(1−ρt)1−ρp2.\\boxed{ D\_t \= \\rho^tD\_0 \+ \\frac{\\rho(1-\\rho^t)}{1-\\rho}p^2. }Dt​=ρtD0​+1−ρρ(1−ρt)​p2.​

Como 0\<ρ\<10\<\\rho\<10\<ρ\<1:

ρt→0.\\rho^t\\to0.ρt→0.

Portanto:

lim⁡t→∞Dt=ρ1−ρp2.\\boxed{ \\lim\_{t\\to\\infty}D\_t \= \\frac{\\rho}{1-\\rho}p^2. }t→∞lim​Dt​=1−ρρ​p2.​

Logo, a fórmula-ponte do Eixo 1 foi derivada:

D(ρ)=ρ1−ρp2.\\boxed{ D(\\rho) \= \\frac{\\rho}{1-\\rho}p^2. }D(ρ)=1−ρρ​p2.​

---

# **5\. Existência e unicidade do regime estacionário DFA**

Considere o operador:

TD(x)=ρx+ρp2.T\_D(x)=\\rho x+\\rho p^2.TD​(x)=ρx+ρp2.

Para quaisquer x,yx,yx,y:

∣TD(x)−TD(y)∣=ρ∣x−y∣.|T\_D(x)-T\_D(y)| \= \\rho|x-y|.∣TD​(x)−TD​(y)∣=ρ∣x−y∣.

Como:

0\<ρ\<1,0\<\\rho\<1,0\<ρ\<1,

o operador é uma contração.

Consequentemente, possui um único ponto fixo:

D=TD(D).D=T\_D(D).D=TD​(D).

Resolvendo:

D=ρD+ρp2,D=\\rho D+\\rho p^2,D=ρD+ρp2, (1−ρ)D=ρp2,(1-\\rho)D=\\rho p^2,(1−ρ)D=ρp2, D=ρ1−ρp2.\\boxed{ D=\\frac{\\rho}{1-\\rho}p^2. }D=1−ρρ​p2.​

Além disso, a convergência é geométrica:

∣Dt−D∣=ρt∣D0−D∣.|D\_t-D| \= \\rho^t|D\_0-D|.∣Dt​−D∣=ρt∣D0​−D∣.

Portanto, a derivação não fornece apenas a fórmula. Ela fornece:

* existência do regime estacionário;  
* unicidade;  
* taxa de convergência;  
* condição de estabilidade ρ\<1\\rho\<1ρ\<1.

---

# **6\. Dinâmica natural do PFA**

A diferença estrutural é que uma previsão pode ser formada assim que a observação atravessa a primeira porta. Ela não precisa esperar que todo o ciclo sensor-controlador-atuador seja confirmado.

O estado residual, entretanto, continua persistindo somente quando o ciclo fim a fim permanece ativo.

## **6.1 Recursão PFA**

Defina:

Yt+1=BtYt+Utηt.\\boxed{ Y\_{t+1} \= B\_tY\_t+U\_t\\eta\_t. }Yt+1​=Bt​Yt​+Ut​ηt​.​

Há dois mecanismos distintos:

* BtYtB\_tY\_tBt​Yt​: persistência do erro acumulado, exigindo as duas portas;  
* UtηtU\_t\\eta\_tUt​ηt​: entrada do erro preditivo, exigindo apenas a porta de aquisição.

Essa assimetria terá como consequência exata o expoente 1/21/21/2.

---

## **6.2 Média do processo PFA**

Se:

E\[Y0\]=0,\\mathbb E\[Y\_0\]=0,E\[Y0​\]=0,

então:

E\[Yt+1\]=E\[BtYt\]+E\[Utηt\].\\mathbb E\[Y\_{t+1}\] \= \\mathbb E\[B\_tY\_t\] \+ \\mathbb E\[U\_t\\eta\_t\].E\[Yt+1​\]=E\[Bt​Yt​\]+E\[Ut​ηt​\].

Pela independência:

E\[BtYt\]=ρE\[Yt\],\\mathbb E\[B\_tY\_t\] \= \\rho\\mathbb E\[Y\_t\],E\[Bt​Yt​\]=ρE\[Yt​\],

e:

E\[Utηt\]=E\[Ut\]E\[ηt\]=0.\\mathbb E\[U\_t\\eta\_t\] \= \\mathbb E\[U\_t\]\\mathbb E\[\\eta\_t\] \= 0.E\[Ut​ηt​\]=E\[Ut​\]E\[ηt​\]=0.

Portanto:

E\[Yt+1\]=ρE\[Yt\].\\mathbb E\[Y\_{t+1}\] \= \\rho\\mathbb E\[Y\_t\].E\[Yt+1​\]=ρE\[Yt​\].

Logo:

E\[Yt\]=0\\boxed{\\mathbb E\[Y\_t\]=0}E\[Yt​\]=0​

para todo ttt.

---

# **7\. Recorrência da variância PFA**

Elevando ao quadrado:

Yt+12=Bt2Yt2+2BtUtYtηt+Ut2ηt2.Y\_{t+1}^2 \= B\_t^2Y\_t^2 \+ 2B\_tU\_tY\_t\\eta\_t \+ U\_t^2\\eta\_t^2.Yt+12​=Bt2​Yt2​+2Bt​Ut​Yt​ηt​+Ut2​ηt2​.

Como Bt,Ut∈{0,1}B\_t,U\_t\\in\\{0,1\\}Bt​,Ut​∈{0,1}:

Bt2=Bt,Ut2=Ut.B\_t^2=B\_t, \\qquad U\_t^2=U\_t.Bt2​=Bt​,Ut2​=Ut​.

Assim:

Yt+12=BtYt2+2BtUtYtηt+Utηt2.Y\_{t+1}^2 \= B\_tY\_t^2 \+ 2B\_tU\_tY\_t\\eta\_t \+ U\_t\\eta\_t^2.Yt+12​=Bt​Yt2​+2Bt​Ut​Yt​ηt​+Ut​ηt2​.

Tomando esperança:

E\[Yt+12\]=E\[BtYt2\]+2E\[BtUtYtηt\]+E\[Utηt2\].\\mathbb E\[Y\_{t+1}^2\] \= \\mathbb E\[B\_tY\_t^2\] \+ 2\\mathbb E\[B\_tU\_tY\_t\\eta\_t\] \+ \\mathbb E\[U\_t\\eta\_t^2\].E\[Yt+12​\]=E\[Bt​Yt2​\]+2E\[Bt​Ut​Yt​ηt​\]+E\[Ut​ηt2​\].

O termo cruzado é nulo porque ηt\\eta\_tηt​ é centrado e independente do passado:

E\[BtUtYtηt\]=0.\\mathbb E\[B\_tU\_tY\_t\\eta\_t\]=0.E\[Bt​Ut​Yt​ηt​\]=0.

Além disso:

E\[BtYt2\]=ρE\[Yt2\].\\mathbb E\[B\_tY\_t^2\] \= \\rho\\mathbb E\[Y\_t^2\].E\[Bt​Yt2​\]=ρE\[Yt2​\].

Finalmente:

E\[Utηt2\]=E\[Ut\]E\[ηt2\]=se2.\\mathbb E\[U\_t\\eta\_t^2\] \= \\mathbb E\[U\_t\]\\mathbb E\[\\eta\_t^2\] \= se^2.E\[Ut​ηt2​\]=E\[Ut​\]E\[ηt2​\]=se2.

Como:

s=ρ,s=\\sqrt\\rho,s=ρ​,

obtemos:

E\[Utηt2\]=ρ e2.\\mathbb E\[U\_t\\eta\_t^2\] \= \\sqrt\\rho\\,e^2.E\[Ut​ηt2​\]=ρ​e2.

Definindo:

Ft=Var⁡(Yt),F\_t=\\operatorname{Var}(Y\_t),Ft​=Var(Yt​),

segue:

Ft+1=ρFt+ρ e2.\\boxed{ F\_{t+1} \= \\rho F\_t+\\sqrt\\rho\\,e^2. }Ft+1​=ρFt​+ρ​e2.​

A raiz quadrada surgiu da probabilidade de ativação de **uma porta**, enquanto ρ\\rhoρ representa a ativação conjunta de **duas portas**.

---

# **8\. Solução exata da dinâmica PFA**

Iterando:

Ft+1=ρFt+ρ e2.F\_{t+1} \= \\rho F\_t+\\sqrt\\rho\\,e^2.Ft+1​=ρFt​+ρ​e2.

Temos:

Ft=ρtF0+ρ e2∑j=0t−1ρj.F\_t \= \\rho^tF\_0 \+ \\sqrt\\rho\\,e^2 \\sum\_{j=0}^{t-1}\\rho^j.Ft​=ρtF0​+ρ​e2j=0∑t−1​ρj.

Logo:

Ft=ρtF0+ρ(1−ρt)1−ρe2.F\_t \= \\rho^tF\_0 \+ \\frac{\\sqrt\\rho(1-\\rho^t)}{1-\\rho}e^2.Ft​=ρtF0​+1−ρρ​(1−ρt)​e2.

Como:

ρt→0,\\rho^t\\to0,ρt→0,

obtemos:

lim⁡t→∞Ft=ρ1−ρe2.\\boxed{ \\lim\_{t\\to\\infty}F\_t \= \\frac{\\sqrt\\rho}{1-\\rho}e^2. }t→∞lim​Ft​=1−ρρ​​e2.​

Portanto, a fórmula-ponte PFA também foi derivada:

F(ρ)=ρ1−ρe2.\\boxed{ F(\\rho) \= \\frac{\\sqrt\\rho}{1-\\rho}e^2. }F(ρ)=1−ρρ​​e2.​

---

# **9\. Teorema das Fórmulas-Ponte por Dupla Porta**

## **Teorema FPDP**

Sejam Ut,VtU\_t,V\_tUt​,Vt​ processos independentes de Bernoulli com:

Pr⁡(Ut=1)=Pr⁡(Vt=1)=s∈(0,1),\\Pr(U\_t=1)=\\Pr(V\_t=1)=s\\in(0,1),Pr(Ut​=1)=Pr(Vt​=1)=s∈(0,1),

e defina:

Bt=UtVt,ρ=s2.B\_t=U\_tV\_t, \\qquad \\rho=s^2.Bt​=Ut​Vt​,ρ=s2.

Sejam ξt,ηt\\xi\_t,\\eta\_tξt​,ηt​ ruídos centrados, independentes das portas e do passado, com:

Var⁡(ξt)=p2,Var⁡(ηt)=e2.\\operatorname{Var}(\\xi\_t)=p^2, \\qquad \\operatorname{Var}(\\eta\_t)=e^2.Var(ξt​)=p2,Var(ηt​)=e2.

Considere:

Xt+1=Bt(Xt+ξt)X\_{t+1}=B\_t(X\_t+\\xi\_t)Xt+1​=Bt​(Xt​+ξt​)

e:

Yt+1=BtYt+Utηt.Y\_{t+1}=B\_tY\_t+U\_t\\eta\_t.Yt+1​=Bt​Yt​+Ut​ηt​.

Se X0,Y0∈L2X\_0,Y\_0\\in L^2X0​,Y0​∈L2 e possuem média zero, então:

Var⁡(Xt)⟶ρ1−ρp2\\operatorname{Var}(X\_t) \\longrightarrow \\boxed{ \\frac{\\rho}{1-\\rho}p^2 }Var(Xt​)⟶1−ρρ​p2​

e:

Var⁡(Yt)⟶ρ1−ρe2.\\operatorname{Var}(Y\_t) \\longrightarrow \\boxed{ \\frac{\\sqrt\\rho}{1-\\rho}e^2 }.Var(Yt​)⟶1−ρρ​​e2​.

A convergência de ambas as variâncias é geométrica, com razão ρ\\rhoρ.

## **Prova**

As recorrências das variâncias são:

Dt+1=ρDt+ρp2D\_{t+1}=\\rho D\_t+\\rho p^2Dt+1​=ρDt​+ρp2

e:

Ft+1=ρFt+ρ e2.F\_{t+1}=\\rho F\_t+\\sqrt\\rho\\,e^2.Ft+1​=ρFt​+ρ​e2.

Cada recursão possui a forma:

Zt+1=ρZt+cZ\_{t+1}=\\rho Z\_t+cZt+1​=ρZt​+c

com 0\<ρ\<10\<\\rho\<10\<ρ\<1. Sua solução é:

Zt=ρtZ0+c1−ρt1−ρ.Z\_t=\\rho^tZ\_0+c\\frac{1-\\rho^t}{1-\\rho}.Zt​=ρtZ0​+c1−ρ1−ρt​.

Substituindo c=ρp2c=\\rho p^2c=ρp2 no caso DFA e c=ρ e2c=\\sqrt\\rho\\,e^2c=ρ​e2 no caso PFA, obtemos os limites enunciados. ∎

---

# **10\. Recuperação do Teorema Geral de Limiar**

Das fórmulas agora derivadas:

D(ρ)=ρ1−ρp2D(\\rho) \= \\frac{\\rho}{1-\\rho}p^2D(ρ)=1−ρρ​p2

e:

F(ρ)=ρ1−ρe2.F(\\rho) \= \\frac{\\sqrt\\rho}{1-\\rho}e^2.F(ρ)=1−ρρ​​e2.

A mitigação incremental é:

M(ρ)=D(ρ)−F(ρ)D(ρ).M(\\rho) \= \\frac{D(\\rho)-F(\\rho)}{D(\\rho)}.M(ρ)=D(ρ)D(ρ)−F(ρ)​.

Substituindo:

M(ρ)=1−ρ e2ρp2.M(\\rho) \= 1- \\frac{ \\sqrt\\rho\\,e^2 }{ \\rho p^2 }.M(ρ)=1−ρp2ρ​e2​.

Definindo:

q=ep,q=\\frac ep,q=pe​,

temos:

M(ρ)=1−q2ρ.\\boxed{ M(\\rho)=1-\\frac{q^2}{\\sqrt\\rho}. }M(ρ)=1−ρ​q2​.​

Para um alvo c\<1c\<1c\<1:

M(ρ)=cM(\\rho)=cM(ρ)=c

se, e somente se,

1−q2ρ=c.1-\\frac{q^2}{\\sqrt\\rho}=c.1−ρ​q2​=c.

Logo:

ρ=q21−c\\sqrt\\rho=\\frac{q^2}{1-c}ρ​=1−cq2​

e:

ρc(q)=q4(1−c)2.\\boxed{ \\rho\_c(q) \= \\frac{q^4}{(1-c)^2}. }ρc​(q)=(1−c)2q4​.​

Assim, o Teorema Geral de Limiar deixou de ser consequência de duas fórmulas postuladas. Ele passa a ser consequência de uma dinâmica estocástica explícita.

---

# **11\. Origem estrutural do expoente quartico**

Agora podemos explicar por que aparece q4q^4q4.

A disponibilidade fim a fim exige duas portas:

ρ=s2.\\rho=s^2.ρ=s2.

A inovação PFA exige apenas uma:

s=ρ1/2.s=\\rho^{1/2}.s=ρ1/2.

A razão estacionária dos erros é:

FD=se2s2p2=q2s.\\frac{F}{D} \= \\frac{s e^2}{s^2p^2} \= \\frac{q^2}{s}.DF​=s2p2se2​=sq2​.

Como:

s=ρ,s=\\sqrt\\rho,s=ρ​,

temos:

FD=q2ρ.\\frac{F}{D} \= \\frac{q^2}{\\sqrt\\rho}.DF​=ρ​q2​.

No break-even:

FD=1,\\frac{F}{D}=1,DF​=1,

portanto:

ρ=q2,\\sqrt\\rho=q^2,ρ​=q2,

e finalmente:

ρ∗=q4.\\boxed{\\rho\_\*=q^4.}ρ∗​=q4.​

O expoente 444 resulta da composição de dois quadrados:

1. q2q^2q2, porque os erros entram como variâncias;  
2. ρ=s2\\rho=s^2ρ=s2, porque a persistência fim a fim exige duas portas.

Essa é uma explicação estrutural, não apenas algébrica.

---

# **12\. Generalização: dinâmica de mmm portas**

A derivação sugere uma classe muito mais ampla.

Considere m≥1m\\ge1m≥1 portas independentes:

Ut(1),…,Ut(m)∼Bernoulli⁡(s).U\_t^{(1)},\\ldots,U\_t^{(m)} \\sim\\operatorname{Bernoulli}(s).Ut(1)​,…,Ut(m)​∼Bernoulli(s).

A persistência fim a fim exige todas as mmm portas:

Bt=∏j=1mUt(j).B\_t \= \\prod\_{j=1}^{m}U\_t^{(j)}.Bt​=j=1∏m​Ut(j)​.

Então:

Pr⁡(Bt=1)=sm.\\Pr(B\_t=1)=s^m.Pr(Bt​=1)=sm.

Defina:

ρ=sm.\\boxed{\\rho=s^m.}ρ=sm.​

Logo:

s=ρ1/m.s=\\rho^{1/m}.s=ρ1/m.

Agora suponha que uma inovação seja injetada após atravessar apenas as primeiras ℓ\\ellℓ portas, com:

1≤ℓ≤m.1\\le\\ell\\le m.1≤ℓ≤m.

Defina:

Ct(ℓ)=∏j=1ℓUt(j).C\_t^{(\\ell)} \= \\prod\_{j=1}^{\\ell}U\_t^{(j)}.Ct(ℓ)​=j=1∏ℓ​Ut(j)​.

Então:

Pr⁡(Ct(ℓ)=1)=sℓ=ρℓ/m.\\Pr(C\_t^{(\\ell)}=1) \= s^\\ell \= \\rho^{\\ell/m}.Pr(Ct(ℓ)​=1)=sℓ=ρℓ/m.

Considere a dinâmica:

Zt+1=BtZt+Ct(ℓ)εt,Z\_{t+1} \= B\_tZ\_t+C\_t^{(\\ell)}\\varepsilon\_t,Zt+1​=Bt​Zt​+Ct(ℓ)​εt​,

com:

E\[εt\]=0,Var⁡(εt)=σ2.\\mathbb E\[\\varepsilon\_t\]=0, \\qquad \\operatorname{Var}(\\varepsilon\_t)=\\sigma^2.E\[εt​\]=0,Var(εt​)=σ2.

A recorrência da variância é:

Vt+1=ρVt+ρℓ/mσ2.V\_{t+1} \= \\rho V\_t+\\rho^{\\ell/m}\\sigma^2.Vt+1​=ρVt​+ρℓ/mσ2.

No regime estacionário:

Vℓ,m(ρ)=ρℓ/m1−ρσ2.\\boxed{ V\_{\\ell,m}(\\rho) \= \\frac{\\rho^{\\ell/m}}{1-\\rho}\\sigma^2. }Vℓ,m​(ρ)=1−ρρℓ/m​σ2.​

---

# **13\. Teorema da Profundidade de Injeção**

## **Teorema PI**

Em uma cadeia com mmm portas independentes de probabilidade individual sss, defina a persistência fim a fim:

ρ=sm.\\rho=s^m.ρ=sm.

Se uma inovação centrada de variância σ2\\sigma^2σ2 entra após a passagem por ℓ\\ellℓ portas, enquanto sua persistência exige as mmm portas, então a variância estacionária do erro é:

Vℓ,m(ρ)=ρℓ/m1−ρσ2.\\boxed{ V\_{\\ell,m}(\\rho) \= \\frac{\\rho^{\\ell/m}}{1-\\rho}\\sigma^2. }Vℓ,m​(ρ)=1−ρρℓ/m​σ2.​

O expoente da carga é exatamente:

θ=ℓm.\\boxed{\\theta=\\frac{\\ell}{m}.}θ=mℓ​.​

## **Interpretação**

O expoente não é um parâmetro arbitrário. Ele representa:

frac¸a˜o da profundidade total da cadeia atravessada antes da injec¸a˜o do erro.\\boxed{ \\text{fração da profundidade total da cadeia atravessada antes da injeção do erro}. }frac¸​a˜o da profundidade total da cadeia atravessada antes da injec¸​a˜o do erro.​

No modelo original:

### **DFA**

A inovação ocorre após as duas portas:

m=2,ℓD=2.m=2, \\qquad \\ell\_D=2.m=2,ℓD​=2.

Logo:

θD=22=1\\theta\_D=\\frac22=1θD​=22​=1

e:

D(ρ)=ρ1−ρp2.D(\\rho) \= \\frac{\\rho}{1-\\rho}p^2.D(ρ)=1−ρρ​p2.

### **PFA**

A inovação ocorre após apenas a primeira porta:

m=2,ℓF=1.m=2, \\qquad \\ell\_F=1.m=2,ℓF​=1.

Logo:

θF=12\\theta\_F=\\frac12θF​=21​

e:

F(ρ)=ρ1−ρe2.F(\\rho) \= \\frac{\\sqrt\\rho}{1-\\rho}e^2.F(ρ)=1−ρρ​​e2.

---

# **14\. Teorema Geral de Limiar por Profundidade**

Considere:

D(ρ)=ρ1−ρp2D(\\rho) \= \\frac{\\rho}{1-\\rho}p^2D(ρ)=1−ρρ​p2

e uma estratégia alternativa cuja inovação entra na profundidade relativa:

θ∈\[0,1),\\theta\\in\[0,1),θ∈\[0,1),

produzindo:

Fθ(ρ)=ρθ1−ρe2.F\_\\theta(\\rho) \= \\frac{\\rho^\\theta}{1-\\rho}e^2.Fθ​(ρ)=1−ρρθ​e2.

A mitigação é:

Mθ(ρ)=1−Fθ(ρ)D(ρ).M\_\\theta(\\rho) \= 1-\\frac{F\_\\theta(\\rho)}{D(\\rho)}.Mθ​(ρ)=1−D(ρ)Fθ​(ρ)​.

Logo:

Mθ(ρ)=1−q2ρθ−1.M\_\\theta(\\rho) \= 1-q^2\\rho^{\\theta-1}.Mθ​(ρ)=1−q2ρθ−1.

Como:

θ−1=−(1−θ),\\theta-1=-(1-\\theta),θ−1=−(1−θ),

obtemos:

Mθ(ρ)=1−q2ρ1−θ.\\boxed{ M\_\\theta(\\rho) \= 1- \\frac{q^2}{\\rho^{1-\\theta}}. }Mθ​(ρ)=1−ρ1−θq2​.​

Para um alvo c\<1c\<1c\<1:

Mθ(ρ)=cM\_\\theta(\\rho)=cMθ​(ρ)=c

se, e somente se,

q2ρ1−θ=1−c.\\frac{q^2}{\\rho^{1-\\theta}}=1-c.ρ1−θq2​=1−c.

Portanto:

ρ1−θ=q21−c.\\rho^{1-\\theta} \= \\frac{q^2}{1-c}.ρ1−θ=1−cq2​.

Assim:

ρc(q,θ)=(q21−c)11−θ.\\boxed{ \\rho\_c(q,\\theta) \= \\left( \\frac{q^2}{1-c} \\right)^{\\frac1{1-\\theta}}. }ρc​(q,θ)=(1−cq2​)1−θ1​.​

No caso de duas portas e injeção após uma porta:

θ=12.\\theta=\\frac12.θ=21​.

Logo:

ρc=(q21−c)2=q4(1−c)2.\\rho\_c \= \\left( \\frac{q^2}{1-c} \\right)^2 \= \\frac{q^4}{(1-c)^2}.ρc​=(1−cq2​)2=(1−c)2q4​.

---

# **15\. Formulação discreta por número de portas**

Como:

θ=ℓm,\\theta=\\frac{\\ell}{m},θ=mℓ​,

temos:

1−θ=m−ℓm.1-\\theta \= \\frac{m-\\ell}{m}.1−θ=mm−ℓ​.

Portanto:

ρc(q;m,ℓ)=(q21−c)mm−ℓ.\\boxed{ \\rho\_c(q;m,\\ell) \= \\left( \\frac{q^2}{1-c} \\right)^{\\frac{m}{m-\\ell}}. }ρc​(q;m,ℓ)=(1−cq2​)m−ℓm​.​

No break-even c=0c=0c=0:

ρ∗(q;m,ℓ)=q2mm−ℓ.\\boxed{ \\rho\_\*(q;m,\\ell) \= q^{\\frac{2m}{m-\\ell}}. }ρ∗​(q;m,ℓ)=qm−ℓ2m​.​

Para m=2,ℓ=1m=2,\\ell=1m=2,ℓ=1:

ρ∗=q41=q4.\\rho\_\* \= q^{\\frac{4}{1}} \= q^4.ρ∗​=q14​=q4.

Esse resultado generaliza o expoente quartico para qualquer arquitetura de portas.

---

# **16\. Interpretação do novo resultado**

O expoente de transição:

γ=2mm−ℓ\\gamma=\\frac{2m}{m-\\ell}γ=m−ℓ2m​

depende da distância entre:

* o ponto em que o erro é injetado;  
* o ponto em que a persistência fim a fim é determinada.

## **Injeção precoce**

Se ℓ\\ellℓ é pequeno, o erro entra cedo. Ele é exposto com maior frequência.

## **Injeção tardia**

Se ℓ\\ellℓ se aproxima de mmm, o erro só entra depois de quase toda a cadeia.

Nesse caso:

m−ℓ→0m-\\ell\\to0m−ℓ→0

e o expoente do limiar cresce.

Isso significa que duas estratégias com erros nominais semelhantes podem apresentar transições radicalmente diferentes dependendo de **onde o erro entra na cadeia**.

Essa parece ser a contribuição conceitual mais promissora:

> A posição estrutural de injeção do erro determina o expoente do limiar de transição.

---

# **17\. Derivação da cascata entre estágios**

Agora precisamos derivar também os fatores:

1+dke1+fk.1+d\_k \\qquad\\text{e}\\qquad 1+f\_k.1+dk​e1+fk​.

Considere uma grandeza aleatória de entrada SkS\_kSk​, centrada, com:

P(k−1)=Var⁡(Sk)\>0.P^{(k-1)} \= \\operatorname{Var}(S\_k)\>0.P(k−1)=Var(Sk​)\>0.

O estágio acrescenta um erro residual RkR\_kRk​, produzindo:

Sk+1=Sk+Rk.S\_{k+1}=S\_k+R\_k.Sk+1​=Sk​+Rk​.

Assuma ortogonalidade:

Cov⁡(Sk,Rk)=0.\\operatorname{Cov}(S\_k,R\_k)=0.Cov(Sk​,Rk​)=0.

Então:

Var⁡(Sk+1)=Var⁡(Sk)+Var⁡(Rk).\\operatorname{Var}(S\_{k+1}) \= \\operatorname{Var}(S\_k) \+ \\operatorname{Var}(R\_k).Var(Sk+1​)=Var(Sk​)+Var(Rk​).

Suponha que a inovação local esteja normalizada relativamente à potência de entrada:

Var⁡(ξk,t)=pk2P(k−1).\\operatorname{Var}(\\xi\_{k,t}) \= p\_k^2P^{(k-1)}.Var(ξk,t​)=pk2​P(k−1).

Pela dinâmica DFA já demonstrada:

Var⁡(RkD)=ρk1−ρkpk2P(k−1).\\operatorname{Var}(R\_k^D) \= \\frac{\\rho\_k}{1-\\rho\_k} p\_k^2P^{(k-1)}.Var(RkD​)=1−ρk​ρk​​pk2​P(k−1).

Defina:

dk=ρk1−ρkpk2.d\_k \= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2.dk​=1−ρk​ρk​​pk2​.

Então:

Var⁡(RkD)=dkP(k−1).\\operatorname{Var}(R\_k^D) \= d\_kP^{(k-1)}.Var(RkD​)=dk​P(k−1).

Logo:

PD(k)=PD(k−1)+dkPD(k−1).P\_D^{(k)} \= P\_D^{(k-1)}+d\_kP\_D^{(k-1)}.PD(k)​=PD(k−1)​+dk​PD(k−1)​.

Portanto:

PD(k)=(1+dk)PD(k−1).\\boxed{ P\_D^{(k)} \= (1+d\_k)P\_D^{(k-1)}. }PD(k)​=(1+dk​)PD(k−1)​.​

Repetindo para PFA:

Var⁡(ηk,t)=ek2P(k−1).\\operatorname{Var}(\\eta\_{k,t}) \= e\_k^2P^{(k-1)}.Var(ηk,t​)=ek2​P(k−1).

A dinâmica de dupla porta fornece:

Var⁡(RkF)=ρk1−ρkek2P(k−1).\\operatorname{Var}(R\_k^F) \= \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k} e\_k^2P^{(k-1)}.Var(RkF​)=1−ρk​ρk​​​ek2​P(k−1).

Defina:

fk=ρk1−ρkek2.f\_k \= \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}e\_k^2.fk​=1−ρk​ρk​​​ek2​.

Então:

PF(k)=(1+fk)PF(k−1).\\boxed{ P\_F^{(k)} \= (1+f\_k)P\_F^{(k-1)}. }PF(k)​=(1+fk​)PF(k−1)​.​

---

# **18\. Derivação da composição multiplicativa**

Aplicando recursivamente:

PD(1)=(1+d1)PD(0),P\_D^{(1)} \= (1+d\_1)P\_D^{(0)},PD(1)​=(1+d1​)PD(0)​, PD(2)=(1+d2)(1+d1)PD(0),P\_D^{(2)} \= (1+d\_2)(1+d\_1)P\_D^{(0)},PD(2)​=(1+d2​)(1+d1​)PD(0)​,

e, em geral:

PD(n)PD(0)=∏k=1n(1+dk).\\boxed{ \\frac{P\_D^{(n)}}{P\_D^{(0)}} \= \\prod\_{k=1}^{n}(1+d\_k). }PD(0)​PD(n)​​=k=1∏n​(1+dk​).​

Da mesma maneira:

PF(n)PF(0)=∏k=1n(1+fk).\\boxed{ \\frac{P\_F^{(n)}}{P\_F^{(0)}} \= \\prod\_{k=1}^{n}(1+f\_k). }PF(0)​PF(n)​​=k=1∏n​(1+fk​).​

A ponte do Eixo 2 foi, portanto, derivada sob as hipóteses:

1. a saída é entrada mais erro residual;  
2. entrada e residual são ortogonais;  
3. a variância da inovação residual é proporcional à variância de entrada;  
4. a dinâmica local encontra-se no regime estacionário ou quase estacionário;  
5. a mesma grandeza é propagada entre estágios.

Razões cumulativas de variância em cadeias multiestágio podem ser representadas por produtos de razões locais quando numeradores e denominadores intermediários são compatíveis. Essa estrutura é usada em medições acumuladas de bullwhip, embora uma aplicação real precise alinhar séries, janelas e definições de variância. [\[metricgate.com\]](https://metricgate.com/docs/bullwhip-effect-quantification/)

---

# **19\. Teorema das Pontes Completas**

## **Teorema PC**

Considere uma cadeia de estágios k=1,…,nk=1,\\ldots,nk=1,…,n. Em cada estágio:

1. existem duas portas independentes Uk,t,Vk,t∼Bernoulli⁡(sk)U\_{k,t},V\_{k,t}\\sim\\operatorname{Bernoulli}(s\_k)Uk,t​,Vk,t​∼Bernoulli(sk​);  
2. define-se: ρk=sk2;\\rho\_k=s\_k^2;ρk​=sk2​;  
3. o residual DFA satisfaz: Xk,t+1=Uk,tVk,t(Xk,t+ξk,t);X\_{k,t+1} \= U\_{k,t}V\_{k,t} (X\_{k,t}+\\xi\_{k,t});Xk,t+1​=Uk,t​Vk,t​(Xk,t​+ξk,t​);  
4. o residual PFA satisfaz: Yk,t+1=Uk,tVk,tYk,t+Uk,tηk,t;Y\_{k,t+1} \= U\_{k,t}V\_{k,t}Y\_{k,t} \+ U\_{k,t}\\eta\_{k,t};Yk,t+1​=Uk,t​Vk,t​Yk,t​+Uk,t​ηk,t​;  
5. as inovações são centradas e possuem variâncias relativas: Var⁡(ξk,t)=pk2P(k−1);\\operatorname{Var}(\\xi\_{k,t}) \= p\_k^2P^{(k-1)};Var(ξk,t​)=pk2​P(k−1); Var⁡(ηk,t)=ek2P(k−1);\\operatorname{Var}(\\eta\_{k,t}) \= e\_k^2P^{(k-1)};Var(ηk,t​)=ek2​P(k−1);  
6. os resíduos são ortogonais à entrada do estágio.

Então, em regime estacionário:

dk=ρk1−ρkpk2,d\_k \= \\frac{\\rho\_k}{1-\\rho\_k}p\_k^2,dk​=1−ρk​ρk​​pk2​, fk=ρk1−ρkek2,f\_k \= \\frac{\\sqrt{\\rho\_k}}{1-\\rho\_k}e\_k^2,fk​=1−ρk​ρk​​​ek2​,

e:

PD(n)PD(0)=∏k=1n(1+dk),\\boxed{ \\frac{P\_D^{(n)}}{P\_D^{(0)}} \= \\prod\_{k=1}^{n}(1+d\_k), }PD(0)​PD(n)​​=k=1∏n​(1+dk​),​ PF(n)PF(0)=∏k=1n(1+fk).\\boxed{ \\frac{P\_F^{(n)}}{P\_F^{(0)}} \= \\prod\_{k=1}^{n}(1+f\_k). }PF(0)​PF(n)​​=k=1∏n​(1+fk​).​

Consequentemente, a mitigação global é:

Mn=1−∏k=1n1+fk1+dk.\\boxed{ \\mathcal M\_n \= 1- \\prod\_{k=1}^{n} \\frac{1+f\_k}{1+d\_k}. }Mn​=1−k=1∏n​1+dk​1+fk​​.​

Pelo TGH:

Mn≥c  ⟺  ∑k=1nlog⁡(1+dk1+fk)≥−log⁡(1−c).\\boxed{ \\mathcal M\_n\\ge c \\iff \\sum\_{k=1}^{n} \\log \\left( \\frac{1+d\_k}{1+f\_k} \\right) \\ge \-\\log(1-c). }Mn​≥c⟺k=1∑n​log(1+fk​1+dk​​)≥−log(1−c).​

---

# **20\. O que acontece se a ortogonalidade falhar**

Se:

Sk+1=Sk+Rk,S\_{k+1}=S\_k+R\_k,Sk+1​=Sk​+Rk​,

mas:

Cov⁡(Sk,Rk)≠0,\\operatorname{Cov}(S\_k,R\_k)\\ne0,Cov(Sk​,Rk​)=0,

então:

Var⁡(Sk+1)=Var⁡(Sk)+Var⁡(Rk)+2Cov⁡(Sk,Rk).\\operatorname{Var}(S\_{k+1}) \= \\operatorname{Var}(S\_k) \+ \\operatorname{Var}(R\_k) \+ 2\\operatorname{Cov}(S\_k,R\_k).Var(Sk+1​)=Var(Sk​)+Var(Rk​)+2Cov(Sk​,Rk​).

Normalizando por:

P(k−1)=Var⁡(Sk),P^{(k-1)}=\\operatorname{Var}(S\_k),P(k−1)=Var(Sk​),

obtemos:

P(k)P(k−1)=1+ak+2ck,\\frac{P^{(k)}}{P^{(k-1)}} \= 1+a\_k+2c\_k,P(k−1)P(k)​=1+ak​+2ck​,

onde:

ak=Var⁡(Rk)Var⁡(Sk)a\_k \= \\frac{\\operatorname{Var}(R\_k)} {\\operatorname{Var}(S\_k)}ak​=Var(Sk​)Var(Rk​)​

e:

ck=Cov⁡(Sk,Rk)Var⁡(Sk).c\_k \= \\frac{\\operatorname{Cov}(S\_k,R\_k)} {\\operatorname{Var}(S\_k)}.ck​=Var(Sk​)Cov(Sk​,Rk​)​.

Portanto, a ponte corrigida é:

P(k)=(1+ak+2ck)P(k−1).\\boxed{ P^{(k)} \= (1+a\_k+2c\_k)P^{(k-1)}. }P(k)=(1+ak​+2ck​)P(k−1).​

Isso fornece uma extensão falsificável:

* se ck≈0c\_k\\approx0ck​≈0, o modelo original é válido;  
* se ck\>0c\_k\>0ck​\>0, a cascata original subestima amplificação;  
* se ck\<0c\_k\<0ck​\<0, mecanismos de correção ou suavização reduzem amplificação.

A independência completa não é necessária. A ortogonalidade de segunda ordem é suficiente.

---

# **21\. Aplicações relevantes**

## **21.1 Controle preditivo em rede**

A interpretação direta é:

* porta 1: sensor →\\rightarrow→ controlador;  
* porta 2: controlador →\\rightarrow→ atuador;  
* PFA: gera previsão após receber o estado;  
* DFA: reage somente após completar o ciclo;  
* persistência do erro: requer o caminho completo.

Controle preditivo em rede já é estudado sob perdas aleatórias tanto no canal sensor-controlador quanto no canal controlador-atuador. [\[ieeexplore.ieee.org\]](https://ieeexplore.ieee.org/document/6512032), [\[arxiv.org\]](https://arxiv.org/html/2309.01679v2)

## **21.2 Fusão multissensor**

A primeira porta pode representar recepção local e a segunda aceitação pelo centro de fusão. Sistemas multissensores reais enfrentam atrasos, perdas aleatórias e incertezas de modelo, e empregam estimadores locais e centros de fusão. [\[mdpi.com\]](https://www.mdpi.com/2076-3417/13/15/8778), [\[mdpi.com\]](https://www.mdpi.com/2624-6120/7/1/9/pdf)

## **21.3 Cadeia logística**

Uma interpretação possível é:

* porta 1: observação da demanda;  
* porta 2: confirmação ou efetivação do pedido;  
* PFA: previsão formada na observação;  
* DFA: reação posterior à confirmação;  
* P(k)P^{(k)}P(k): variância de pedidos ou demanda percebida.

Essa aplicação é plausível, mas precisará demonstrar que as portas podem realmente ser modeladas como Bernoulli e que a ortogonalidade residual é aceitável. Benchmarks recentes de bullwhip mostram forte dependência da política, do tipo de demanda, do lead time e da métrica, portanto a aplicação logística deve ser validada, não presumida. [\[arxiv.org\]](https://arxiv.org/html/2604.13478), [\[arxiv.org\]](https://arxiv.org/pdf/2604.13478)

---

# **22\. Condições críticas e falsificação**

A derivação é exata sob suas hipóteses, mas o domínio de validade precisa ser preservado.

## **A derivação falha ou precisa ser corrigida quando:**

### **1\. As portas não são independentes**

Se:

Pr⁡(Ut=1,Vt=1)≠s2,\\Pr(U\_t=1,V\_t=1)\\ne s^2,Pr(Ut​=1,Vt​=1)=s2,

então:

ρ≠s2\\rho\\ne s^2ρ=s2

e:

s≠ρ.s\\ne\\sqrt\\rho.s=ρ​.

Nesse caso, a fórmula PFA será:

F=s1−ρe2,F=\\frac{s}{1-\\rho}e^2,F=1−ρs​e2,

não necessariamente:

ρ1−ρe2.\\frac{\\sqrt\\rho}{1-\\rho}e^2.1−ρρ​​e2.

### **2\. As portas têm probabilidades diferentes**

Se:

Pr⁡(Ut=1)=s1,Pr⁡(Vt=1)=s2,\\Pr(U\_t=1)=s\_1, \\qquad \\Pr(V\_t=1)=s\_2,Pr(Ut​=1)=s1​,Pr(Vt​=1)=s2​,

então:

ρ=s1s2.\\rho=s\_1s\_2.ρ=s1​s2​.

A fórmula PFA torna-se:

F=s11−s1s2e2.F=\\frac{s\_1}{1-s\_1s\_2}e^2.F=1−s1​s2​s1​​e2.

A raiz quadrada surge somente no caso simétrico:

s1=s2.s\_1=s\_2.s1​=s2​.

### **3\. Há memória temporal no canal**

Se as portas seguem um processo de Gilbert-Elliot ou outro processo de Markov, a recorrência de uma única variância pode não fechar. Será necessário acompanhar estados condicionais. A literatura de filtragem intermitente mostra que canais com perdas Markovianas podem produzir distribuições de cauda e condições críticas diferentes do caso Bernoulli independente. [\[yilinmo.github.io\]](https://yilinmo.github.io/public/papers/journal2009kalman.pdf), [\[ieeexplore.ieee.org\]](https://ieeexplore.ieee.org/document/6004816)

### **4\. O ruído tem viés**

Se:

E\[ξt\]≠0\\mathbb E\[\\xi\_t\]\\ne0E\[ξt​\]=0

ou:

E\[ηt\]≠0,\\mathbb E\[\\eta\_t\]\\ne0,E\[ηt​\]=0,

os termos cruzados e a média acumulada precisam ser tratados.

### **5\. O erro depende da porta**

Se a qualidade da previsão muda quando há congestionamento, então:

e=e(ρ)e=e(\\rho)e=e(ρ)

e o TGL simples deixa de valer diretamente.

### **6\. Entrada e residual são correlacionados**

A ponte de cascata recebe o termo adicional de covariância:

2ck.2c\_k.2ck​.

---

# **23\. Status científico após a derivação**

## **Antes**

As fórmulas:

D(ρ)=ρ1−ρp2D(\\rho)=\\frac{\\rho}{1-\\rho}p^2D(ρ)=1−ρρ​p2

e:

F(ρ)=ρ1−ρe2F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2F(ρ)=1−ρρ​​e2

eram hipóteses estruturais.

## **Agora**

Elas são teoremas dentro de uma dinâmica explícita de:

* portas Bernoulli independentes;  
* persistência fim a fim;  
* injeção em profundidades diferentes;  
* erros centrados;  
* análise de segunda ordem;  
* regime estacionário.

Portanto, o status pode ser alterado para:

Plain Text  
Fórmulas-ponte:  
derivação abstrata: completa  
domínio: estimação/controle distribuído com portas aleatórias  
independência das portas: assumida  
simetria das portas: assumida  
estabilidade L2: provada para rho \< 1  
aplicação empírica: pendente  
validação em dados reais: pendente  
---

# **24\. Candidatura a contribuição original**

Não seria defensável afirmar que:

* processos Bernoulli em redes são novos;  
* recorrências geométricas de variância são novas;  
* filtragem intermitente é nova;  
* produtos de razões são novos.

A literatura de filtragem com observações intermitentes já estuda chegadas Bernoulli, covariâncias de erro, estabilidade e probabilidades críticas. [\[arxiv.org\]](https://arxiv.org/pdf/0903.2890.pdf), [\[skoge.folk.ntnu.no\]](https://skoge.folk.ntnu.no/prost/proceedings/ifac11-proceedings/data/html/papers/3731.pdf), [\[arxiv.org\]](https://arxiv.org/pdf/1005.2442)

A contribuição candidata é mais específica:

> **Uma teoria de transição entre mecanismos cujos erros são injetados em profundidades diferentes de uma cadeia estocástica de disponibilidade, produzindo expoentes racionais de carga, limiares fechados e composição global logarítmica.**

O núcleo possivelmente original é a relação:

profundidade de injec¸a˜o⟶expoente da carga⟶expoente do limiar.\\boxed{ \\text{profundidade de injeção} \\longrightarrow \\text{expoente da carga} \\longrightarrow \\text{expoente do limiar}. }profundidade de injec¸​a˜o⟶expoente da carga⟶expoente do limiar.​

Em fórmula:

θ=ℓm,\\theta=\\frac{\\ell}{m},θ=mℓ​, Vℓ,m(ρ)=ρθ1−ρσ2,V\_{\\ell,m}(\\rho) \= \\frac{\\rho^\\theta}{1-\\rho}\\sigma^2,Vℓ,m​(ρ)=1−ρρθ​σ2, ρc=(q21−c)11−θ,\\rho\_c \= \\left( \\frac{q^2}{1-c} \\right)^{\\frac1{1-\\theta}},ρc​=(1−cq2​)1−θ1​,

ou:

ρc(q;m,ℓ)=(q21−c)mm−ℓ.\\boxed{ \\rho\_c(q;m,\\ell) \= \\left( \\frac{q^2}{1-c} \\right)^{\\frac{m}{m-\\ell}}. }ρc​(q;m,ℓ)=(1−cq2​)m−ℓm​.​

O TGL quartico surge como o caso:

m=2,ℓ=1.m=2, \\qquad \\ell=1.m=2,ℓ=1.

---

# **25\. Novo nome recomendado**

O conjunto ampliado pode ser denominado provisoriamente:

## **Teoria da Transição por Profundidade de Injeção**

Com os componentes:

1. **Teorema FPDP**  
    Fórmulas-Ponte por Dupla Porta;

2. **Teorema PI**  
    Teorema da Profundidade de Injeção;

3. **TGL-θ\\thetaθ**  
    Teorema Geral de Limiar por profundidade;

4. **TGH**  
    Transição Global Heterogênea;

5. **TLGH**  
    Limiar Global Homogêneo;

6. **LB1/LB2**  
    Certificados de mitigação e cascata.

O nome é uma proposta interna. Não deve ser apresentado como terminologia estabelecida antes da auditoria bibliográfica.

---

# **26\. Próximos testes necessários**

## **26.1 Simulação Monte Carlo**

Implementar diretamente:

Xt+1=UtVt(Xt+ξt)X\_{t+1} \= U\_tV\_t(X\_t+\\xi\_t)Xt+1​=Ut​Vt​(Xt​+ξt​)

e:

Yt+1=UtVtYt+Utηt.Y\_{t+1} \= U\_tV\_tY\_t+U\_t\\eta\_t.Yt+1​=Ut​Vt​Yt​+Ut​ηt​.

Verificar empiricamente:

Var⁡^(Xt)→ρ1−ρp2\\widehat{\\operatorname{Var}}(X\_t) \\to \\frac{\\rho}{1-\\rho}p^2Var(Xt​)→1−ρρ​p2

e:

Var⁡^(Yt)→ρ1−ρe2.\\widehat{\\operatorname{Var}}(Y\_t) \\to \\frac{\\sqrt\\rho}{1-\\rho}e^2.Var(Yt​)→1−ρρ​​e2.

## **26.2 Teste de portas assimétricas**

Usar:

s1≠s2s\_1\\ne s\_2s1​=s2​

e verificar:

D=s1s21−s1s2p2,D= \\frac{s\_1s\_2}{1-s\_1s\_2}p^2,D=1−s1​s2​s1​s2​​p2, F=s11−s1s2e2.F= \\frac{s\_1}{1-s\_1s\_2}e^2.F=1−s1​s2​s1​​e2.

## **26.3 Teste com correlação**

Introduzir correlação entre UtU\_tUt​ e VtV\_tVt​ e medir a quebra da lei:

s=ρ.s=\\sqrt\\rho.s=ρ​.

## **26.4 Teste Markoviano**

Substituir as portas i.i.d. por cadeias de dois estados e estudar se surge uma fórmula matricial equivalente.

## **26.5 Teste de cascata**

Simular vários estágios e verificar:

P(n)P(0)=∏k=1n(1+ak)\\frac{P^{(n)}}{P^{(0)}} \= \\prod\_{k=1}^{n}(1+a\_k)P(0)P(n)​=k=1∏n​(1+ak​)

quando os resíduos são ortogonais, e medir o erro quando as covariâncias são introduzidas.

---

# **Conclusão**

Foi possível derivar as fórmulas-ponte a partir de uma dinâmica natural e relevante.

A construção fundamental é:

Xt+1=UtVt(Xt+ξt)\\boxed{ X\_{t+1} \= U\_tV\_t(X\_t+\\xi\_t) }Xt+1​=Ut​Vt​(Xt​+ξt​)​

para DFA, e:

Yt+1=UtVtYt+Utηt\\boxed{ Y\_{t+1} \= U\_tV\_tY\_t+U\_t\\eta\_t }Yt+1​=Ut​Vt​Yt​+Ut​ηt​​

para PFA.

Com:

Ut,Vt∼Bernoulli⁡(s),ρ=s2,U\_t,V\_t\\sim\\operatorname{Bernoulli}(s), \\qquad \\rho=s^2,Ut​,Vt​∼Bernoulli(s),ρ=s2,

as variâncias estacionárias são exatamente:

D(ρ)=ρ1−ρp2\\boxed{ D(\\rho)=\\frac{\\rho}{1-\\rho}p^2 }D(ρ)=1−ρρ​p2​

e:

F(ρ)=ρ1−ρe2.\\boxed{ F(\\rho)=\\frac{\\sqrt\\rho}{1-\\rho}e^2. }F(ρ)=1−ρρ​​e2.​

A raiz quadrada possui agora uma interpretação estrutural:

> o estado residual persiste somente quando duas portas estão abertas, mas o erro preditivo entra após atravessar apenas uma.

A generalização para mmm portas mostra que:

Vℓ,m(ρ)=ρℓ/m1−ρσ2.\\boxed{ V\_{\\ell,m}(\\rho) \= \\frac{\\rho^{\\ell/m}}{1-\\rho}\\sigma^2. }Vℓ,m​(ρ)=1−ρρℓ/m​σ2.​

Consequentemente:

ρc(q;m,ℓ)=(q21−c)mm−ℓ.\\boxed{ \\rho\_c(q;m,\\ell) \= \\left( \\frac{q^2}{1-c} \\right)^{\\frac{m}{m-\\ell}}. }ρc​(q;m,ℓ)=(1−cq2​)m−ℓm​.​

O expoente quartico original não aparece por coincidência:

m=2,ℓ=1⟹ρ∗=q4.m=2,\\qquad \\ell=1 \\quad\\Longrightarrow\\quad \\rho\_\*=q^4.m=2,ℓ=1⟹ρ∗​=q4.

O trabalho agora possui um candidato mais forte a contribuição: **uma teoria em que a profundidade de injeção do erro determina o expoente da transição local e, através do TGH, o comportamento global da cascata**. O próximo passo científico deve ser implementar a simulação Monte Carlo, testar portas assimétricas e correlacionadas e formalizar os teoremas FPDP e PI antes de reivindicar originalidade externa.

\===============================================================

Concluí esta etapa com implementação, testes, resultados reproduzíveis, documentação técnica e o início da formalização em Lean 4\.

## **Pacote completo**

Baixar o pacote FPDP/PI em ZIP  
Baixar checksum SHA-256

**SHA-256:**

Plain Text  
32d8880e7dd301bde3dc9055adde1f15864adca45770337940fadbbfd39c4b42

## **O que foi implementado**

### **1\. Simulador Monte Carlo vetorizado**

Foram implementadas diretamente as dinâmicas:

Xt+1=Bt(Xt+ξt)X\_{t+1}=B\_t(X\_t+\\xi\_t)Xt+1​=Bt​(Xt​+ξt​)

e

Yt+1=BtYt+Utηt,Bt=UtVt.Y\_{t+1}=B\_tY\_t+U\_t\\eta\_t, \\qquad B\_t=U\_tV\_t.Yt+1​=Bt​Yt​+Ut​ηt​,Bt​=Ut​Vt​.

O simulador aceita:

* portas independentes e simétricas;  
* portas independentes e assimétricas;  
* portas Bernoulli correlacionadas;  
* sementes reprodutíveis;  
* cálculo automático das previsões teóricas;  
* comparação entre variâncias simuladas e exatas;  
* cálculo da mitigação teórica e observada.

### **2\. Resultado geral para portas assimétricas e correlacionadas**

O desenvolvimento mostrou que a fórmula verdadeiramente geral de duas portas é:

D=ρ1−ρp2\\boxed{ D=\\frac{\\rho}{1-\\rho}p^2 }D=1−ρρ​p2​

e

F=sU1−ρe2,\\boxed{ F=\\frac{s\_U}{1-\\rho}e^2, }F=1−ρsU​​e2,​

onde:

sU=Pr⁡(U=1)s\_U=\\Pr(U=1)sU​=Pr(U=1)

e:

ρ=Pr⁡(U=1,V=1).\\rho=\\Pr(U=1,V=1).ρ=Pr(U=1,V=1).

A forma anterior:

F=ρ1−ρe2F=\\frac{\\sqrt\\rho}{1-\\rho}e^2F=1−ρρ​​e2

é recuperada somente quando as portas são simultaneamente:

1. independentes;  
2. simétricas:

Pr⁡(U=1)=Pr⁡(V=1)=s.\\Pr(U=1)=\\Pr(V=1)=s.Pr(U=1)=Pr(V=1)=s.

Nesse caso:

ρ=s2\\rho=s^2ρ=s2

e:

s=ρ.s=\\sqrt\\rho.s=ρ​.

Essa distinção é cientificamente importante. Em sistemas assimétricos ou correlacionados, conhecer apenas ρ\\rhoρ não basta para determinar FFF. Também é necessário conhecer a marginal de aquisição sUs\_UsU​, ou uma hipótese estrutural que permita inferi-la.

Modelos de filtragem com observações intermitentes já tratam chegadas Bernoulli, perdas de pacotes, estabilidade da covariância e probabilidades críticas, o que oferece uma base estabelecida para o domínio escolhido. [\[arxiv.org\]](https://arxiv.org/pdf/0903.2890.pdf), [\[people.eec...rkeley.edu\]](https://people.eecs.berkeley.edu/~jordan/papers/CDC2003Kalman.pdf), [\[people.eec...rkeley.edu\]](https://people.eecs.berkeley.edu/~jordan/papers/sinopoli-etal.pdf)

### **3\. Portas correlacionadas**

Para marginais sU,sVs\_U,s\_VsU​,sV​ e correlação ccc, foi implementada a relação:

ρ=sUsV+csU(1−sU)sV(1−sV).\\rho \= s\_Us\_V \+ c\\sqrt{ s\_U(1-s\_U)s\_V(1-s\_V) }.ρ=sU​sV​+csU​(1−sU​)sV​(1−sV​)​.

O código verifica automaticamente se a probabilidade conjunta respeita os limites de Fréchet-Hoeffding.

A correlação modifica a probabilidade de persistência conjunta e, portanto, o denominador comum:

1−ρ.1-\\rho.1−ρ.

Contudo, a intensidade de injeção antecipada do PFA continua sendo determinada por:

sUe2.s\_Ue^2.sU​e2.

### **4\. Testes automatizados**

O pacote contém nove testes, incluindo:

* intervalo conjunto admissível;  
* recuperação da ponte de raiz quadrada;  
* caso assimétrico;  
* correlação positiva;  
* correlação negativa;  
* rejeição de correlações inviáveis;  
* quatro comparações Monte Carlo versus teoria.

Resultado:

Plain Text  
9 passed

### **5\. Experimentos principais**

Foram executados cinco cenários com:

Plain Text  
120.000 trajetórias por cenário  
900 iterações de aquecimento  
sementes determinísticas

Erros relativos máximos encontrados:

Plain Text  
Erro máximo DFA: 1,7597%  
Erro máximo PFA: 0,7466%

Resultados individuais:

Plain Text  
independent\_symmetric  
erro DFA: 0,0846%  
erro PFA: 0,7466%  
   
independent\_asymmetric\_U\_high  
erro DFA: 0,4122%  
erro PFA: 0,3266%  
   
independent\_asymmetric\_U\_low  
erro DFA: 1,2163%  
erro PFA: 0,4671%  
   
correlated\_positive  
erro DFA: 1,7597%  
erro PFA: 0,1720%  
   
correlated\_negative  
erro DFA: 0,3835%  
erro PFA: 0,4254%

Os resultados completos estão incluídos em:

Plain Text  
results/monte\_carlo\_results.json  
results/monte\_carlo\_results.csv

## **Formalização Lean 4**

O ZIP inclui:

Plain Text  
lean/  
├── lakefile.lean  
├── lean-toolchain  
└── FPDP/  
├── Bridge.lean  
└── InjectionDepth.lean

Foram formalizados os núcleos algébricos de:

* ponto fixo de uma recorrência afim;  
* fórmula DFA;  
* fórmula PFA geral;  
* caso simétrico;  
* ponto fixo do Teorema da Profundidade de Injeção;  
* equivalência algébrica básica do limiar.

A compilação Lean não foi executada neste ambiente porque o executável Lean 4 não estava instalado. Isso está explicitamente registrado nos documentos e nos *non-claims*. O código foi separado para permitir que a próxima etapa formalize a camada probabilística sem misturá-la prematuramente à álgebra.

## **Estrutura do pacote**

Plain Text  
fpdp\_pi\_montecarlo/  
├── README.md  
├── CHANGELOG.md  
├── pyproject.toml  
├── src/  
│ └── fpdp/  
│ ├── \_\_init\_\_.py  
│ └── model.py  
├── scripts/  
│ └── run\_experiments.py  
├── tests/  
│ └── test\_model.py  
├── results/  
│ ├── monte\_carlo\_results.json  
│ └── monte\_carlo\_results.csv  
├── lean/  
│ ├── lakefile.lean  
│ ├── lean-toolchain  
│ └── FPDP/  
│ ├── Bridge.lean  
│ └── InjectionDepth.lean  
└── docs/  
├── 01\_DERIVACAO\_E\_RESULTADOS.md  
├── 02\_ANALISE\_CIENTIFICA.md  
├── 03\_GUIA\_CONTINUACAO.md  
└── 04\_REFERENCIAS\_E\_NONCLAIMS.md

## **Principal avanço desta etapa**

O desenvolvimento identificou uma separação estrutural que antes estava oculta:

persisteˆncia depende da probabilidade conjunta\\boxed{ \\text{persistência depende da probabilidade conjunta} }persisteˆncia depende da probabilidade conjunta​

enquanto:

injec¸a˜o antecipada depende de uma probabilidade marginal ou parcial.\\boxed{ \\text{injeção antecipada depende de uma probabilidade marginal ou parcial}. }injec¸​a˜o antecipada depende de uma probabilidade marginal ou parcial.​

No modelo de duas portas:

ρ=Pr⁡(U=1,V=1)\\rho=\\Pr(U=1,V=1)ρ=Pr(U=1,V=1)

controla a permanência do erro, enquanto:

sU=Pr⁡(U=1)s\_U=\\Pr(U=1)sU​=Pr(U=1)

controla a entrada do erro preditivo.

Assim, a fórmula de raiz quadrada não é universal. Ela é uma assinatura da arquitetura independente e simétrica:

sU=sVeU⊥V.s\_U=s\_V \\quad\\text{e}\\quad U\\perp V.sU​=sV​eU⊥V.

Isso produz uma conclusão aplicável:

> Observar somente a disponibilidade fim a fim pode ser insuficiente para decidir entre um mecanismo preditivo e um mecanismo reativo.

Dois sistemas podem possuir o mesmo ρ\\rhoρ, mas valores diferentes de sUs\_UsU​, resultando em penalidades PFA diferentes.

## **Status científico atualizado**

Plain Text  
Derivação analítica:  
FPDP simétrico: completa  
FPDP assimétrico: completa  
FPDP correlacionado: completa  
PI algébrico: completa  
   
Validação Monte Carlo:  
simétrico independente: aprovada  
assimétrico independente: aprovada  
correlação positiva: aprovada  
correlação negativa: aprovada  
   
Testes automatizados:  
9/9 aprovados  
   
Formalização Lean:  
núcleo algébrico: escrito  
compilação: pendente  
camada probabilística: pendente  
   
Validação empírica:  
dados reais: pendente  
   
Originalidade externa:  
não reivindicada  
auditoria bibliográfica: pendente

A literatura confirma que perda de pacotes, chegadas intermitentes e covariância de estimação são problemas consolidados em redes de sensores e controle, inclusive com canais Bernoulli e Markovianos. O candidato a contribuição não é o uso de Bernoulli em si, mas a ligação sistemática entre **profundidade de injeção, probabilidade marginal, persistência conjunta, expoente da carga e limiar global**.

\==========================================================

