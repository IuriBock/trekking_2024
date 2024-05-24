import bluerobotics_navigator as navigator
import time


# Definir pinos dos motores
PWM_PIN_M = navigator.PwmChannel.Ch4 # Pino PWM para o motor 
IN1_PIN_M = navigator.PwmChannel.Ch3  # Pino IN1 para o motor 
IN2_PIN_M = navigator.PwmChannel.Ch2  # Pino IN2 para o motor 

# Definir pino do servo motor
SERVO_PIN = navigator.PwmChannel.Ch1 # Pino para o servo motor


# Inicializa a navigator 
navigator.init()
navigator.set_pwm_freq_hz(50)


# Funções de controle dos motores
def motor_forward():
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 1)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 1)
    navigator.set_pwm_enable(True)

def motor_backward():
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 1)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 1)
    navigator.set_pwm_enable(True)

def stop_motor():
    navigator.set_pwm_enable(False)
    navigator.set_pwm_channel_duty_cycle(IN1_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(IN2_PIN_M, 0)
    navigator.set_pwm_channel_duty_cycle(PWM_PIN_M, 0)



# Função do servo
def direction_servo(direction=0.105):
    navigator.set_pwm_enable(True)
    if direction == 'direita':
        x = 0.12
    elif direction == 'esquerda':
        x = 0.08
    elif direction == 'reto':
        x = 0.105
    else:
        x = direction
    navigator.set_pwm_channel_duty_cycle(SERVO_PIN, x)

direction_servo() # Inicia com servo centralizado

def dir(x):
    navigator.set_pwm_channel_duty_cycle(SERVO_PIN, x)
	


# Teste de movimentação
try:

    dir(0.105)
    print('ligando')
    time.sleep(3)

    print('frente')
    motor_forward() # Carrinho anda por 1 segundo
    time.sleep(2)

    dir(0.12)
    print('direita')
    direction_servo('direita') # Vira para direita
    time.sleep(1)

    dir(0.105)
    print('reto')
    direction_servo() # Centraliza servo
    time.sleep(2)

    print('para')
    stop_motor() # Para de andar
    time.sleep(1)

    dir(0.08)    
    print('esquerda')
    direction_servo('esquerda') # Vira o servo para esquerda
    
    print('ré')
    motor_backward() # Anda para trás
    time.sleep(2)

    dir(0.105)
    print('reto')
    direction_servo() # Centraliza servo
    time.sleep(1)

    print('frente')
    motor_forward() # Anda para frente
    print('direita')
    dir(0.12)
    direction_servo('direita') # Vira para direita
    time.sleep(2)

    print('para')
    stop_motor() # Para de andar
    print('finalizado')
    
except:
    navigator.set_pwm_enable(False)
