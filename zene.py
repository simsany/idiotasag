import pygame.midi
import time
def note_to_number(note,octav):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    return notes.index(note)+12*octav



pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(25)
for _ in range(2):
    player.note_on(60, 100)
    time.sleep(0.5)
    player.note_off(60, 100)
    player.note_on(64, 100)
    time.sleep(0.5)
    player.note_off(64, 100)
    player.note_on(60, 100)
    time.sleep(0.5)
    player.note_off(60, 100)
    player.note_on(64, 100)
    time.sleep(0.5)
    player.note_off(64, 100)


    player.note_on(67, 100)
    time.sleep(1)
    player.note_off(67, 100)
    player.note_on(67, 100)
    time.sleep(1)
    player.note_off(67, 100)

player.note_on(note_to_number('C',6), 100)
time.sleep(0.5)
player.note_off(note_to_number('C',6), 100)
player.note_on(note_to_number('B',5), 100)
time.sleep(0.5)
player.note_off(note_to_number('B',5), 100)
player.note_on(note_to_number('A',5), 100)
time.sleep(0.5)
player.note_off(note_to_number('A',5), 100)
player.note_on(note_to_number('G',5), 100)
time.sleep(0.5)
player.note_off(note_to_number('G',5), 100)
player.note_on(note_to_number('F',5), 100)
time.sleep(1)
player.note_off(note_to_number('F',5), 100)
player.note_on(note_to_number('A',5), 100)
time.sleep(1)
player.note_off(note_to_number('A',5), 100)
player.note_on(note_to_number('G',5), 100)
time.sleep(0.5)
player.note_off(note_to_number('G',5), 100)
player.note_on(note_to_number('F',5), 100)
time.sleep(0.5)
player.note_off(note_to_number('F',5), 100)
player.note_on(note_to_number('E',5), 100)
time.sleep(0.5)
player.note_off(note_to_number('E',5), 100)
player.note_on(note_to_number('D',5), 100)
time.sleep(0.5)
player.note_off(note_to_number('D',5), 100)
player.note_on(note_to_number('C',5), 100)
time.sleep(1)
player.note_off(note_to_number('C',5), 100)
player.note_on(note_to_number('C',5), 100)
time.sleep(1)
player.note_off(note_to_number('C',5), 100)




del player
pygame.midi.quit()