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

def si_input_valido(respuesta):
    mayuscula = respuesta.upper()
    if mayuscula not in ['A', 'B', 'C', 'D']:
        return False
    return True 

respuestas = []
resultados = []
contador_correctas = 0
contador_incorrectas = 0

nombre = input("\t\t\t\t\t\t ¿Como te llamas?: ")
print()
print("\t"*6,"*** BIENVENIDO AL CUESTIONARIO ***\n")
print("\t"*6,f"*** Te damos la bienvenida {nombre}...\n")
print("\t"*6,"Espero estes listo para las siguientes preguntas...\n")

for i in PREGUNTAS:
    print("\t"*6, i["pregunta"])
    print("\t"*6, i["opcion1"])
    print("\t"*6, i["opcion2"])
    print("\t"*6, i["opcion3"])
    print("\t"*6, i["opcion4"])
    while True:
        res = input("\n\t\t\t\t\t\tIngrese su respuesta: ").strip().upper()
        es_valido = si_input_valido(res)
        if es_valido:
            break
        print("\t\t\t\t\t\tCaracter Invalido, la respuesta solo puede ser A,B,C o D")
    print("\t\t\t\t\t\tRespuesta registrada")
    respuestas.append(res)
    print()

print("\t"*6,"*** RESULTADOS DEL CUESTIONARIO ***\n")
for i in range(len(PREGUNTAS)):
    correcta = PREGUNTAS[i]["respuesta"]
    
    if respuestas[i] == correcta:
        print("\t"*6,f"Pregunta {i+1}: {respuestas[i]} -> ✅")
        resultados.append(True)
        contador_correctas += 1
        
    else:
        print("\t"*6,f"Pregunta {i+1}: {respuestas[i]} -> ❌")
        resultados.append(False)
        contador_incorrectas += 1

total = contador_correctas + contador_incorrectas
print()
print("\t"*6,f"✅ PREGUNTAS CORRECTAS: {contador_correctas} / {total}")
print("\t"*6,f"❌ PREGUNTAS INCORRECTAS: {contador_incorrectas} / {total}") 
print()

total = 100*contador_correctas / total
print("\t"*6,f"Porcentaje de aciertos: {total:.2f}%")
