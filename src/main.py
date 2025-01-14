import time
import random
from controller import fetch_pokemon_data, add_pokemon_to_db

def main():
    max_records = 35  # Número máximo de registros
    added_records = 0  # Contador de registros adicionados

    while added_records < max_records:
        pokemon_id = random.randint(1, 350)  # Gera um ID aleatório entre 1 e 350
        pokemon_schema = fetch_pokemon_data(pokemon_id)

        if pokemon_schema:
            print(f"Adicionando {pokemon_schema.name} ao banco de dados.")
            add_pokemon_to_db(pokemon_schema)
            added_records += 1  # Incrementa o contador de registros adicionados
        else:
            print(f"Não foi possível obter dados para o Pokémon com ID {pokemon_id}.")
        
        time.sleep(10)  # Aguarda 10 segundos entre as requisições

    print(f"Processo concluído. {added_records} registros foram adicionados ao banco de dados.")
    print("Ingestão de dados finalizada!")

if __name__ == "__main__":
    main()
