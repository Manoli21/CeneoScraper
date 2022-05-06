import os
import pandas as pd

print(*[filename.split(".")[0] for filename in os.listdir("./opinions")], sep="\n")
product_id = input("Podaj identyfikator produktu: ")

opinions = pd.read_json(f"opinions/{product_id}.json")
print(opinions)

## Przejrzyć dokumenty pandas, policzyć ile mamy opinii, dla ile wady/zalety, liczba gwiazdek 
## przeczytać bibliotekę pandas, matplotlib