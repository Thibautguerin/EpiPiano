#!/usr/bin/python3

from include import *
from clean_piano import *
from verif_format import *

def play_the_song(window, song, detect):
	myfont = pygame.font.SysFont("monospace", 50, True)

	pygame.draw.rect(window, back_color, (0, 0, 1920, 1080))
	name = myfont.render(song, 1, (255,0,0))
	window.blit(name, (1920 / 2 - name.get_rect().width / 2, 100))

	clean_piano(window)
	pygame.display.update()
	i = 0
	good_note = 0
	find_note = []
	display_note = 0
	going = True
	prev_note_time = [0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	j = 0
	y = 0
	parsing = verif_format("./song/" + song)

	pygame.display.update()

	while (1 and i != len(parsing)):
		for event in pygame.event.get():
			if (event.type == QUIT):
				return
			if (event.type == KEYDOWN):
				if (event.key == K_ESCAPE):
					return
				if (event.key == K_f):
					pygame.display.toggle_fullscreen()
		if (find_note == []):
			while (y != len(vpiano)):
				while (j != len(parsing[i])):
					if (int(parsing[i][j]) == vpiano[y][1]):
						window.blit(touch[1][vpiano[y][3]], vpiano[y][2])
					j = j + 1
				j = 0
				if (display_note == 1):
					break
				y = y + 1
			display_note = 0
			find_note = list(parsing[i])
			y = 0
			pygame.display.update()

		if detect.poll():
			midiEvents = detect.read(10)
			note = midiEvents[0][0][1]
			vel = midiEvents[0][0][2]

			if (vel != 0):
				while (j != len(find_note)):
					if (int(note) == int(find_note[j])):
						find_note.remove(find_note[j])
						while (y != len(vpiano)):
							if (int(note) == vpiano[y][1]):
								window.blit(touch[0][vpiano[y][3]], vpiano[y][2])
								pygame.display.update()
								good_note = 1
								break
							y = y + 1
						y = 0
						break
					j = j + 1;
				if (good_note == 0):
					while (y != len(vpiano)):
						if (int(note) == vpiano[y][1]):
							window.blit(touch[3][vpiano[y][3]], vpiano[y][2])
							pygame.display.update()
							break
						y = y + 1
					y = 0
				good_note = 0
				if (find_note == []):
					i = i + 1
				prev_note_time[0] = int(midiEvents[0][1])
				#prev_note_time[1].append()
				j = 0