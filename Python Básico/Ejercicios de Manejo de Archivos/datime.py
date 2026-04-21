from datetime import datetime


def generate_time_log():
  current_time = datetime.now()
  return 'Esto fue escrito a las ' + current_time.strftime('%I:%M %p')

def write_time_log_to_file(file_path):
  log = generate_time_log()
  with open(file_path, 'w') as file:
    file.write(log)


print('Se ejecuto la funcion')
write_time_log_to_file('c:/Users/bjoseign/Desktop/LYFTER/Ejercicios de Manejo de Archivos/time_entries.log')