import pyaudio
import numpy as np
import time
import os
import subprocess
import sys

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CLAP_THRESHOLD = 2000 

DOTA_PATH = r"C:\Program Files (x86)\Steam\steamapps\common\dota 2 beta\game\bin\win64\dota2.exe"

p = pyaudio.PyAudio()

def calculate_volume(audio_data):
    if len(audio_data) == 0:
        return 0

    squares = audio_data.astype(np.float32) ** 2
    mean_square = np.mean(squares)
    if mean_square <= 0:
        return 0
    return np.sqrt(mean_square)

try:
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
        input_device_index=None 
    )

    game_launched = False
    launch_time = 0
    
    while True:
        try:
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)

            if len(audio_data) == 0:
                continue

            volume = calculate_volume(audio_data)

            current_time = time.time()
            if volume > CLAP_THRESHOLD:
                print(f"Clap detected! Volume: {volume}")

                if not game_launched or (current_time - launch_time > 10):           
                    try:
                        subprocess.Popen([DOTA_PATH])
                        game_launched = True
                        launch_time = current_time
                        print("Dota 2 launched!") 
                    except Exception as e:
                        print(f"Error launching game: {e}")

                    time.sleep(0.5)
            time.sleep(0.01)
            
        except IOError as e:
            if "Input overflowed" in str(e):
                continue
            else:
                raise

except Exception as e:
    print(f"Error: {e}")

finally:
    try:
        stream.stop_stream()
        stream.close()
    except:
        pass
    p.terminate()