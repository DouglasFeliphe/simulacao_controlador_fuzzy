# simulacao_controlador_fuzzy

 Regras Fuzzy

Peso Muito Leve
<ul>
<li>	SE peso é muito leve e sujeira é Quase Limpo, ENTÃO quantidade de detergente é muito pouco.</li>
<li>	SE peso é Muito Leve e sujeira é Sujo, ENTÃO quantidade de detergente é Pouco.</li>
<li>	SE peso é Muito Leve e sujeira é Muito Sujo, ENTÃO quantidade de detergente é Pouco.</li>
<li> SE peso é Muito Leve e sujeira é Extra Sujo, ENTÃO quantidade de detergente é Moderado.</li>
</ul>
Peso Leve
<ul>
<li> SE peso é Leve e sujeira é Quase Limpo, ENTÃO quantidade de detergente é Pouco.</li>
<li>	SE peso é Leve e sujeira é Sujo, ENTÃO quantidade de detergente é Pouco.</li>
<li>	SE peso é Leve e sujeira é Muito Sujo, ENTÃO quantidade de detergente é Moderado.</li>
<li>	SE peso é Leve e sujeira é Extra Sujo, ENTÃO quantidade de detergente é Exagerado.</li>
</ul>
Peso Pesado
<ul>
 <li>	SE peso é Pesado e sujeira é Quase Limpo, ENTÃO quantidade de detergente é Moderado.</li>
 <li>	SE peso é Pesado e sujeira é Sujo, ENTÃO quantidade de detergente é Moderado.</li>
 <li>	SE peso é Pesado e sujeira é Muito Sujo, ENTÃO quantidade de detergente é Exagerado.</li>
 <li> SE peso é Pesado e sujeira é Extra Sujo, ENTÃO quantidade de detergente é Exagerado</li>
</ul>
Peso Muito Pesado
<ul>
 <li>	SE peso é Muito Pesado e sujeira é Quase Limpo, ENTÃO quantidade de detergente é Moderado</li>
 <li>	SE peso é Muito Pesado e sujeira é Sujo, ENTÃO quantidade de detergente é Exagerado</li>
 <li>	SE peso é Muito Pesado e sujeira é Muito Sujo, ENTÃO quantidade de detergente é Máximo</li>
 <li>	SE peso é Muito Pesado e sujeira Extra Sujo, ENTÃO quantidade de detergente é Máximo</li>
</ul>

Universo De Discurso
Os valores ‘Peso’, ‘Sujeira’ e ‘Quantidade de Detergente’ podem variar de 0 á 100



Funções de Pertinência

•	Peso
1.	Muito Leve – [0,20] Rampa
2.	Leve – [10, 50] Triangular
3.	Pesado – [40, 90] Triangular
4.	Muito Pesado [75, 100] – Trapezoidal

•	Sujeira
1.	Quase Limpo – [0, 20] Rampa
2.	Sujo – [10, 50] Triangular
3.	Muito Sujo – [40, 100] Triangular
4.	Extra Sujo – [80, 100] Rampa

•	Quantidade de Detergente
1.	Muito Pouco – [0, 20]  Triangular
2.	Pouco – [20, 40]  Triangular
3.	Moderado – [40, 60]   Triangular
4.	Exagerado – [60, 80]  Triangular
5.	Máximo – [80, 100]  Trapezoidal


Simulação
Valores CRISPS de entrada: 
•	Peso = 45
•	Sujeira = 19
Valores de saída esperados:
•	Quantidade de Detergente = 42 (Moderado)
