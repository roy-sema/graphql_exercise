import numpy as np
import simpleaudio as sa

def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    audio = (wave * 32767).astype(np.int16)
    return audio

def play_wave(audio, sample_rate=44100):
    wave_obj = sa.WaveObject(audio.tobytes(), num_channels=1, bytes_per_sample=2, sample_rate=sample_rate)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def play_melody():
    notes = {
        'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
        'G4': 392.00, 'A4': 440.00, 'B4': 493.88, 'C5': 523.25
    }
    melody = ['C4', 'E4', 'G4', 'C5', 'G4', 'E4', 'C4']
    duration = 0.4  # seconds per note
    
    for note in melody:
        frequency = notes[note]
        wave = generate_sine_wave(frequency, duration)
        play_wave(wave)

if __name__ == "__main__":
    play_melody()

