import notify2 
import subprocess
from playsound import playsound

def check_battery():
    try:
        prueba = subprocess.run(["acpi", "-b"], capture_output=True, text=True)
        if int(prueba.stdout[20:23].strip()) <= 20:
            batNotify("Batería baja, por favor conecte el cargador")
            play_sound()
    except:
        batNotify("""Error al encontrar la barrería
        revisa la configuracion para resolver el problema""")

def batNotify(argu):
    notify2.init("Batería baja")
    notificacion = notify2.Notification("Batería baja", message=argu, icon="/home/idksa_script/Codigo/Proyectos/BateriaBaja/icono/bateriaBaja.png")
    notificacion.show()
    
def play_sound():
    playsound("/home/idksa_script/Codigo/Proyectos/BateriaBaja/Sonidos/bateria-baja.wav")

if __name__ == "__main__":
    check_battery()