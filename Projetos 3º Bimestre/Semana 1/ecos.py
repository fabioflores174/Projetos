# Dicionário contendo as medições de som para cada direção
sons = {
	"Norte": [32,35, 40,39, 41], # Medições desom no Norte
	"Sul": [22,21, 19,23,25], # Medições desom noSul
	"Leste": [28,30,33,34,32], # Medições desom noLeste
	"Oeste": [40, 44, 42, 45, 43] # Medições desom no Oeste
}

# Compreensão de dicionario para calcular a média dos sons para cada direção
media_sons = {
	direcao: sum(valores) / len(valores) # Calcolala media de cada lista de sons
	for direcao, valores in sons.items() # Itera sobre as direções e suas medições
}

#Encontra a direção com a salon média de som usando max()
# A função max() usa a média dos sons como critério para encontrar a direção mais
barulhenta
direcao_mais_barulho max(media_sons, key-media_sons.get) 

# Exibe a direção que possul a maior media de son
print("Direção mais barulhenta:", direcao_mais_barulho)