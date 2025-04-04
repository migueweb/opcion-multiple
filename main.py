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
    if mayuscula != 'A' and mayuscula != "B" and mayuscula != "C" and mayuscula != "D":
        return False
    return True 

respuestas=[]
print("\n***BIENVENIDO A EL CUESTIONARIO***\n")
for i in PREGUNTAS:
    print(i.get("pregunta"))
    print(i.get("opcion1"))
    print(i.get("opcion2"))
    print(i.get("opcion3"))
    print(i.get("opcion4"))
    while True:
        res=input("Ingrese su respuesta: ")
        esValido = siInputValido(res)
        if esValido:
            break
        print("Respuesta no valida, Reintentelo")
    respuestas.append(res)
    print()

print("***SUS RESPUESTAS SON:***\n")
for i in range(len(PREGUNTAS)):

    # Solución 1
    # print(respuestas[i])
   

    if respuestas[i]==(PREGUNTAS[i].get("respuesta")):
        print(f"{respuestas[i]} ---> CORRECTA")
    else:
        print(f"{respuestas[i]} ---> INCORECTA")


   
