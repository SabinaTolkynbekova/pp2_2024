def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams_need = 100
ounces_need = grams_to_ounces(grams_need)
print(f"{grams_need} grams is equal to {ounces_need:.2f} ounces.")

