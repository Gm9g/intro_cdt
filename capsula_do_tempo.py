# --- CÓDIGO DA CÁPSULA DO TEMPO DIGITAL ---

# 1. Coletando informações do usuário
# Usamos input() para perguntar e armazenamos a resposta em variáveis
print("Olá! Vamos criar sua Cápsula do Tempo Digital! 🚀")


nome = input("Qual é o nome do seu artista favorito do seu Spotify? ")  # Variável para guardar o nome [cite: 88, 92]
hobby = input("Qual é seu album favorito? ") # Variável para guardar o hobby
sonho = input("Qual musica mais te inspira? ") # Variável para guardar o sonho

# Coletando informações numéricas e convertendo para inteiro com int()
# Isso é importante para podermos fazer cálculos com a idade 
ano_atual_str = input("Quantos Anos Você Tem?(ex, 17y) ")

ano_atual = int(ano_atual_str) # Converte o texto (string) para número inteiro (int) 

anos_no_futuro_str = input("Você Quer Quardar este segerdo por quantos anos? (ex, 10y)")
anos_no_futuro = int(anos_no_futuro_str) # Converte para número inteiro

# 2. Processando as informações
# Calculando o ano em que a cápsula será "aberta" 
ano_da_abertura = ano_atual + anos_no_futuro

# 3. Exibindo a mensagem da cápsula do tempo
# Usamos f-strings para formatar a saída de forma clara e personalizada 
print("\n--- ABRINDO SUA CÁPSULA DO TEMPO DIGITAL ---")
print(f"Olá do passado! Esta mensagem foi criada por você, quando você tinha {ano_atual}.")
print(f"Naquela época, o Album favorito do seu Spotify era: {hobby}.")
print(f"Aquela musica que te inspirou para o futuro  {nome} era: {sonho}.")
print(f"\nEspero que com seus {ano_da_abertura}, esteja ficado igualzinho!")
print("--- FIM DA CÁPSULA ---")