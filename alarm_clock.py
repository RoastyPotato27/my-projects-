# Alarm Clock >

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print('***************************')
    print(f'Alarm Set For {alarm_time}')
    print('***************************')
    sound_file = 'Alarm Clock.mp3'
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(current_time)
        time.sleep(1)

        # Stop alarm when timer hits >
        if current_time == alarm_time:
            print('**********')
            print('WAKE UP!! ')
            print('**********')

            is_running = False

            # sound The Alarm >
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play() # Plays for fking 1 second 

            # Making it last longer >
            while pygame.mixer.music.get_busy():
                time.sleep(1)


if __name__ == '__main__':
    alarm_time = input('Enter alarm time (HH:MM:SS): ')
    set_alarm(alarm_time)