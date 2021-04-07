import i2c_lib
import lcddriver
import sys

coso = str

def main(coso):
  # Main program block
    lcd = lcddriver.lcd()
    lcd.lcd_clear()
    msg=coso.split('\n')
    #print(msg)
    lcd.lcd_display_string(msg[0], 1)
    if len(msg)>1:
        lcd.lcd_display_string(msg[1], 2)
    if len(msg)>2:
        lcd.lcd_display_string(msg[2], 3)
    if len(msg)>3:
        lcd.lcd_display_string(msg[3], 4)
    if len(msg)>4:
        print("Ultima línea no posible de mostrar por pantalla")
    
        
if __name__ == '__main__':

    main(coso)
