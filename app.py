import os
import sys
import time
from google import genai

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def efecto_escritura(texto):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(0.01)
    print()

def main():
    try:
        client = genai.Client()
    except Exception:
        limpiar_pantalla()
        print("="*60)
        print(" ⚠️  ERROR DE CONFIGURACIÓN DE LA IA")
        print("="*60)
        print("Por favor, configura tu API Key de Gemini.")
        print("Ejecuta en tu terminal de VS Code:")
        print("Windows (PowerShell):  $env:GEMINI_API_KEY=\"tu_clave_aquí\"")
        print("Linux/Mac/Git Bash:   export GEMINI_API_KEY=\"tu_clave_aquí\"")
        print("="*60)
        return

    while True:
        limpiar_pantalla()
        print("="*60)
        print("       🤖 GENERADOR DE HISTORIAS CON IA GENERATIVA 🤖       ")
        print("="*60)
        print("1. Crear una Historia Fantástica")
        print("2. Crear un Poema Creativo")
        print("3. Salir del Programa")
        print("="*60)
        
        opcion = input("Elige una opción (1-3): ").strip()
        
        if opcion == "3":
            print("\n¡Gracias por usar la IA Generativa! Éxitos en tu presentación. 🚀")
            break
            
        if opcion not in ["1", "2"]:
            print("\n❌ Opción no válida. Presiona Enter para intentar de nuevo...")
            input()
            continue
            
        tema = input("\n📝 ¿Sobre qué tema o personaje quieres que escriba?: ")
        if not tema:
            print("\n❌ El tema no puede estar vacío.")
            input("\nPresiona Enter para continuar...")
            continue
            
        if opcion == "1":
            prompt = f"Escribe una historia corta, bonita y fantástica sobre: {tema}. Que sea creativa y tenga un final feliz."
            tipo = "HISTORIA GENERADA"
        else:
            prompt = f"Escribe un poema corto y emotivo con rima hermosa sobre: {tema}."
            tipo = "POEMA GENERADO"
            
        print("\n🧠 Conectando con la IA Generativa... Por favor espera...")
        
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )
            
            print("\n" + "="*60)
            print(f" ✨ {tipo} ✨ ")
            print("="*60 + "\n")
            
            efecto_escritura(response.text)
            
            print("\n" + "="*60)
            input("Presiona Enter para volver al menú principal...")
            
        except Exception as e:
            print(f"\n❌ Ocurrió un error: {e}")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
