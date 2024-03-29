# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import Orange

base = Orange.data.Table('risco-credito.csv')

cn2_learner = Orange.classification.rules.CN2Learner()
classificador = cn2_learner(base)

for regras in classificador.rule_list:
    print(regras)
    

# história boa, dívida alta, garantias nenhuma, renda > 35
# história ruim, dívida alta, garantidas adequada, renda < 15    
resultado = classificador([['boa', 'alta', 'nenhuma', 'acima_35'], ['ruim',
                           'alta','adequada', '0_15']])
    
for i in resultado:
    print(base.domain.class_var.values[i])