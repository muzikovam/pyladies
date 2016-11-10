def tah(pole, index, symbol):  # Ukazka DRY principu, vytahli jsme spolecny kod do jedne funkce
    """Vrátí herní pole s daným symbolem umístěným na danou pozici."""
    if pole[index]!="-":
        raise ValueError("hrajes na obsazene pole")
    return pole[:index] + symbol + pole[index + 1:]
