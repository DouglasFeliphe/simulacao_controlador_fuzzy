import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# functions
peso = ctrl.Antecedent(np.arange(0, 101, 1), 'peso')
sujeira = ctrl.Antecedent(np.arange(0, 101, 1), 'sujeira')
qtd_detergente = ctrl.Consequent(np.arange(0, 101, 1), 'qtd_detergente')

# funções de pertinência 
peso['Muito Leve'] = fuzz.trimf(peso.universe, [0, 0, 20])
peso['Leve'] = fuzz.trimf(peso.universe, [10, 30, 50])
peso['Pesado'] = fuzz.trimf(peso.universe, [40, 65, 90])
peso['Muito Pesado'] = fuzz.trapmf(peso.universe, [75, 90, 100, 100])

sujeira['Quase Limpo'] = fuzz.trimf(sujeira.universe, [0, 0, 20])
sujeira['Sujo'] = fuzz.trimf(sujeira.universe, [10, 30, 50])
sujeira['Muito Sujo'] = fuzz.trimf(sujeira.universe, [40, 70, 100])
sujeira['Extra Sujo'] = fuzz.trimf(sujeira.universe, [80, 100, 100])

qtd_detergente['Muito Pouco'] = fuzz.trimf(qtd_detergente.universe, [0, 10, 20])
qtd_detergente['Pouco'] = fuzz.trimf(qtd_detergente.universe, [20, 30, 40])
qtd_detergente['Moderado'] = fuzz.trimf(qtd_detergente.universe, [40, 50, 60])
qtd_detergente['Exagerado'] = fuzz.trimf(qtd_detergente.universe, [60, 70, 80])
qtd_detergente['Máximo'] = fuzz.trapmf(qtd_detergente.universe, [80, 90, 100, 100])

# You can see how these look with .view()
# peso.view()
# sujeira.view()
# qtd_detergente.view()

# Regras Fuzzy
rule1a = ctrl.Rule(peso['Muito Leve'] & sujeira['Quase Limpo'], qtd_detergente['Muito Pouco'])
rule2a = ctrl.Rule(peso['Muito Leve'] & sujeira['Sujo'], qtd_detergente['Pouco'])
rule3a = ctrl.Rule(peso['Muito Leve'] & sujeira['Muito Sujo'], qtd_detergente['Pouco'])
rule4a = ctrl.Rule(peso['Muito Leve'] & sujeira['Extra Sujo'], qtd_detergente['Moderado'])

rule1b = ctrl.Rule(peso['Leve'] & sujeira['Quase Limpo'], qtd_detergente['Pouco'])
rule2b = ctrl.Rule(peso['Leve'] & sujeira['Sujo'], qtd_detergente['Pouco'])
rule3b = ctrl.Rule(peso['Leve'] & sujeira['Muito Sujo'], qtd_detergente['Moderado'])
rule4b = ctrl.Rule(peso['Leve'] & sujeira['Extra Sujo'], qtd_detergente['Exagerado'])

rule1c = ctrl.Rule(peso['Pesado'] & sujeira['Quase Limpo'], qtd_detergente['Moderado'])
rule2c = ctrl.Rule(peso['Pesado'] & sujeira['Sujo'], qtd_detergente['Moderado'])
rule3c = ctrl.Rule(peso['Pesado'] & sujeira['Muito Sujo'], qtd_detergente['Exagerado'])
rule4c = ctrl.Rule(peso['Pesado'] & sujeira['Extra Sujo'], qtd_detergente['Exagerado'])

rule1d = ctrl.Rule(peso['Muito Pesado'] & sujeira['Quase Limpo'], qtd_detergente['Moderado'])
rule2d = ctrl.Rule(peso['Muito Pesado'] & sujeira['Sujo'], qtd_detergente['Exagerado'])
rule3d = ctrl.Rule(peso['Muito Pesado'] & sujeira['Muito Sujo'], qtd_detergente['Máximo'])
rule4d = ctrl.Rule(peso['Muito Pesado'] & sujeira['Extra Sujo'], qtd_detergente['Máximo'])

# Criação do controle do sistema
tipping_ctrl = ctrl.ControlSystem([rule1a, rule2a, rule3a, rule4a,
                                  rule1b, rule2b, rule3b, rule4b,
                                  rule1c, rule2c, rule3c, rule4c,
                                  rule1d, rule2d, rule3d, rule4d,])

tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

#Simulação
  
tipping.input['peso'] =  47 # valor aleatório para o peso das roupas
tipping.input['sujeira'] = 19 # valor aleatório para a quantidade de sujeira

#computando os valores
tipping.compute()

# visualizando a sáida e resultados
print(tipping.output['qtd_detergente'])
qtd_detergente.view(sim=tipping)

rule1a.view()




