from concurrent.futures.process import _ThreadWakeup


# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

saldo = 1000
saque = 250
limite = 200
conta_especial = True

print(True and True )
print(True and False)
print(False and False)
print(True or False)
print(True or True )
print(True or False)


exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp)
print(exp_2)