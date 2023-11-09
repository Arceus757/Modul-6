#1. Skapa din första def-funktion som kan plussa två tal och returnerar summan med return-kommandot
def plussa(tal1, tal2):
    summa = tal1 + tal2
    return summa

resultat = plussa(5, 5)
print(resultat)  # Resultatet är 10 


#2. Gör en def-funktion som skriver ut ditt namn
def mitt_namn():
    print("Jag heter Dmytro")

mitt_namn()


#3. Gör en loop som skriver ut resultatet av en def 10 gånger
def plussa(tal1, tal2):
    summa = tal1 + tal2
    return summa

for _ in range(10):
    resultat = plussa(5, 5)
    print(resultat)

#4. Skapa ett program som kan ändra/lägga till/ta bort namn i en lista med olika funktioner
# Här är själva listan som sedan kan ändras. 
# def Show_list(namn_lista):
#     print("Namn i listan:")
#     for namn in namn_lista:
#         print(namn)

# # Lägga till ett namn i listan
# def add_name(namn_lista):
#     nytt_namn = input("Ange namnet du vill lägga till: ")
#     namn_lista.append(nytt_namn)
#     print(f"{nytt_namn} har lagts till i listan.")

# # Ta bort ett namn från listan
# def remove_name(namn_lista):
#     namn = input("Ange namnet du vill ta bort: ")
#     if namn in namn_lista:
#         namn_lista.remove(namn)
#         print(f"{namn} har tagits bort från listan.")
#     else:
#         print(f"{namn} finns inte i listan.")

# namn_lista = ["Dmytro"]

# while True:
#     print("======================")
#     print("\nVälj en åtgärd:")
#     print("1. Visa lista")
#     print("2. Lägg till namn")
#     print("3. Ta bort namn")
#     print("4. Avsluta programet")
#     print("\n=====================")
    
#     val = input("Vad vill du göra: ")
    
#     if val == "1":
#         Show_list(namn_lista)
#     elif val == "2":
#         add_name(namn_lista)
#     elif val == "3":
#         remove_name(namn_lista)
#     elif val == "4":
#         break
#     else:
#         print("Du får bara välja mella 1 och 4, var snäll och försök igen men utan dumheter den här gången.")



#5. Bygg vidare på din miniräknare (med fyra räknesätt), så den använder en def som gör alla sorts beräkningar och ger tillbaka svar.
# Funktion för att utföra beräkningar
def rakna(operation, number1, number2):
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2
    else:
        result = None
        print("Du får bara välja mellan + - * och /")
    return result

# Huvudprogram
while True:
    operation = input("Välj vad du vill göra (+, -, *, /) eller 'quit' för att avsluta: ")

    if operation == 'quit':
        break

    if operation not in ['+', '-', '*', '/']:
        print("Fel inmatning. Försök igen.")
        continue

    try:
        number1 = float(input("Ange det första talet: "))
        number2 = float(input("Ange det andra talet: "))
    except ValueError:
        print("Du får bara skriva  siffror. Försök igen och utan dumheter den här gången.")
        continue

    result = rakna(operation, number1, number2)

    if result is not None:
        print(f"Resultat: {result}")
