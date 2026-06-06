import easygui
import sys

def main():
    opcion = easygui.buttonbox("Seleccione el autómata celular a ejecutar:",
                               title="Autómatas Celulares",
                               choices=["Hormiga de Langton", "Juego de la Vida (Life-Like)", "Salir"])
    
    if opcion == "Hormiga de Langton":
        try:
            import Hormiga_visual as hormiga
            hormiga.main()
        except ImportError:
            easygui.msgbox("No se encuentra el archivo Hormiga_visual.py", "Error")
    elif opcion == "Juego de la Vida (Life-Like)":
        try:
            import guiVida as vida
            vida.main()
        except ImportError:
            easygui.msgbox("No se encuentra el archivo guiVida.py", "Error")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
