tonns_to_kg = lambda x: x * 1000  
kg_to_gm = lambda x: x * 1000     
gm_to_mg = lambda x: x * 1000    
mg_to_lb = lambda x: x * 0.00220462  

tonns = float(input("Enter weight in tonns: "))

kg = tonns_to_kg(tonns)
gm = kg_to_gm(kg)
mg = gm_to_mg(gm)
lb = mg_to_lb(mg)

print(f"{tonns} tonns = {kg} kg = {gm} grams = {mg} milligrams = {lb} pounds")
