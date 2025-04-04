## Formulario de opcion multiple
# 

PREGUNTAS = [
    {
        "pregunta": "¿Cuál es la capital de Francia?",
        "respuesta": "D",
        "opcion1": "A) Londres",
        "opcion2": "B) Roma",
        "opcion3": "C) Madrid",
        "opcion4": "D) París"
    },
    {
        "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
        "respuesta": "B",
        "opcion1": "A) 1920",
        "opcion2": "B) 1939",
        "opcion3": "C) 1945",
        "opcion4": "D) 1914"
    },
    {
        "pregunta": "¿Quién pintó la Mona Lisa?",
        "respuesta": "C",
        "opcion1": "A) Pablo Picasso",
        "opcion2": "B) Vincent van Gogh",
        "opcion3": "C) Leonardo da Vinci",
        "opcion4": "D) Claude Monet"
    }
]

def siInputValido(respuesta):
    mayuscula = respuesta.upper()
    if mayuscula not in ['A', 'B', 'C', 'D']:
        return False
    return True 

respuestas = []
resultados = []
contador_correctas = 0
contador_incorrectas = 0

print("\n*** BIENVENIDO AL CUESTIONARIO ***\n")

for i in PREGUNTAS:
    print(i["pregunta"])
    print(i["opcion1"])
    print(i["opcion2"])
    print(i["opcion3"])
    print(i["opcion4"])
    while True:
        res = input("Ingrese su respuesta: ").strip().upper()
        esValido = siInputValido(res)
        if esValido:
            break
        print("Respuesta no valida, Reintentelo")
    respuestas.append(res)
    print()

print("*** RESULTADOS DEL CUESTIONARIO ***\n")
for i in range(len(PREGUNTAS)):
    correcta = PREGUNTAS[i]["respuesta"]
    
    if respuestas[i] == correcta:
        print(f"{respuestas[i]} ---> CORRECTA")
        resultados.append(True)
        contador_correctas += 1
        
    else:
        print(f"{respuestas[i]} ---> INCORRECTA (Correcta: {correcta})")
        resultados.append(False)
        contador_incorrectas += 1

total = contador_correctas + contador_incorrectas
print(f"\nPREGUNTAS CORRECTAS: {contador_correctas} / {total}")
print(f"PREGUNTAS INCORRECTAS: {contador_incorrectas} / {total}") 

print(resultados) 
