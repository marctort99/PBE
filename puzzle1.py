import i2c_lib
import i2c_driver
import sys 

def main():
  # Main program block
  lcd = i2c_driver.lcd()
  while True:
    print("Escribe un texto por líneas de 20 caracteres y pulsa Enter seguido de Ctrl+D")
    msg = sys.stdin.readlines()
    lcd.lcd_clear()
    for x in range(len(msg)):
        lcd.lcd_display_string(msg[x].replace("\n", ""), x+1)
        
if __name__ == '__main__':
    
    main()
