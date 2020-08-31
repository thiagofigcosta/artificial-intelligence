# Linear Regression

# Exercicio 1
```
python3 linearRegression.py --single -a 0.01 -e 10
```
Para se obter uma curva de aprendizado mais suave:
```
python3 linearRegression.py --single -a 0.001 -e 50
python3 linearRegression.py --single -a 0.0001 -e 500
```

# Exercicio 2
```
python3 linearRegression.py --multi -a 0.01 -e 10
```
ou
```
python3 linearRegression.py --multi -a 0.001 -e 250
```

Não é possível traçar o ajuste linear pois a vizualização seria de um plano 3D e não uma reta.

# Exercicio 3
Para data1.txt:
```
python3 linearRegression.py --normal1
```

Para data2.txt:
```
python3 linearRegression.py --normal2
```

Para o data2 o erro quadratico é menor usando o método da equação normal caso o se executem poucas iterações ou se use uma taxa alta de aprendizado, entretantanto ao se usar uma taxa baixa com muitas iterações o erro é menor para a regreção linear pois neste caso é feito um ajuste fino e mesmo a equação normal calculando os valores exatos ela usa o coeficiente linear como 0 o que não é o ideal para todos os cenários.