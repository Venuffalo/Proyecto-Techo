# Ejercicio: Create code that enables an AI to generate music.
# Generado y probado por Profesor de Codigo el 2026-11-24 02:13:16

import random
import time

# Simulate generating a simple melody
def generate_melody(num_notes=10):
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    melody = [random.choice(notes) for _ in range(num_notes)]
    return melody

# Simulate playing the melody
def play_melody(melody):
    print("Playing melody:", melody)

# Main function to generate and play a melody
def generate_and_play_melody():
    melody = generate_melody()
    play_melody(melody)

# Run the function 3 times with a short delay
for _ in range(3):
    generate_and_play_melody()
    time.sleep(1)  # Simulate a short delay between iterations

# In production, this would run indefinitely with the real interval instead of a fixed count
