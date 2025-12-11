READ = 1       # 0001
WRITE = 2      # 0010
EXECUTE = 4    # 0100
ADMIN = 8      # 1000

permisos = 0     # sin permisos al inicio

# Activar permisos
permisos |= READ
permisos |= WRITE
permisos |= ADMIN

print(bin(permisos))  # 0b11  (tiene leer y escribir)


i = 15
j = 22

bit = i & j
print(bit)
print(bin(bit))  # 0b10110 (intersección de bits)