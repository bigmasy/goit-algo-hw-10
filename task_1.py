import pulp

model = pulp.LpProblem("Production optimization", pulp.LpMaximize)

A = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
B = pulp.LpVariable('Fruite_juice', lowBound=0, cat='Continuous')

model += A + B, "Total_Production"

model += 2*A + 1*B <= 100, "Water"
model += 1*A <= 50, "Sugar"
model += 1*A <= 30, "Lemon_Juice"
model += 2*B <= 40, "Fruit_Puree"

model.solve()

print("Статус:", pulp.LpStatus[model.status])

print("Кількість виробленого Лимонаду:", pulp.value(A))
print("Кількість виробленого Фруктового соку:", pulp.value(B))

print("Загальна кількість вироблених продуктів:", pulp.value(model.objective))