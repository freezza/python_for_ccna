# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

qest = {'access':'Введите номер VLAN:', 'trunk':'Введите разрешенные VLANы:'}

q1 = input("Введите режим работы (access/trunk): ", ).lower()
q2 = input("Введите номер интерфейса в виде Gi0/3: ")
q3 = input('{}'.format(qest[q1]))

template = globals()[q1+'_template']

print('interface {}'.format(q2))
print('\n'.join(template).format(q3))