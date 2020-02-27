#!/usr/bin/python3

from include import *
from clean_piano import *
from clic import *

def create_the_song(window, name, detect):
	myfont = pygame.font.SysFont("monospace", 34, True)

	pygame.draw.rect(window, back_color, (0, 0, 1920, 1080))

	if (os.path.exists(name)):
		if (os.path.isfile(name)):
			file_exist = myfont.render("This music is already existing in your recording !", 1, (255,0,0))
			continue_to_create = myfont.render("Do you want to continue? (the old music will be overwritten)", 1, (255,0,0))
			window.blit(file_exist, (1920 / 2 - file_exist.get_rect().width / 2, 100))
			window.blit(continue_to_create, (1920 / 2 - continue_to_create.get_rect().width / 2, 200))
			while (1):
				for event in pygame.event.get():
					pass
				mouse_pos = pygame.mouse.get_pos()
				if (mouse_pos[0] >= 636 and mouse_pos[0] <= 930 and mouse_pos[1] >= 650 and mouse_pos[1] <= 829):
					window.blit(yes_c, (636, 650))
					window.blit(no, (990, 650))
					if (pygame.mouse.get_pressed()[0]):
						wait_mouse_up()
						break;
				elif (mouse_pos[0] >= 990 and mouse_pos[0] <= 1284 and mouse_pos[1] >= 650 and mouse_pos[1] <= 829):
					window.blit(yes, (636, 650))
					window.blit(no_c, (990, 650))
					if (pygame.mouse.get_pressed()[0]):
						wait_mouse_up()
						return
				else:
					window.blit(yes, (636, 650))
					window.blit(no, (990, 650))
				pygame.display.update()
				clockFps.tick(maxFps)
			os.remove(name)
		else:
			folder_exist = myfont.render("A folder already exists with this name!", 1, (255,0,0))
			window.blit(folder_exist, (1920 / 2 - folder_exist.get_rect().width / 2, 200))
			pygame.display.update()
			pygame.time.wait(2000)
			return

	os.makedirs(name)
	os.rmdir(name)

	pygame.draw.rect(window, back_color, (0, 0, 1920, 1080))
	clean_piano(window)
	pygame.display.update()
	file = open(name, "w")
	prev_note_time = [0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	going = True
	first = 0
	i = 0
	j = 0

	while (going):
		note = []
		for event in pygame.event.get():
			if (event.type == QUIT):
				going = False
			if (event.type == KEYDOWN):
				if (event.key == K_ESCAPE):
					going = False

			if (event.type == KEYDOWN):
				key = pygame.key.get_pressed()
				while (i != len(key)):
					while (j != len(keyboard)):
						if (int(key[i]) == 1 and i == keyboard[j][0]):
							if (note.count(int(keyboard[j][1])) == 0):
								note.append(int(keyboard[j][1]))
								break
						j = j + 1
					j = 0
					i = i + 1
				i = 0
		if detect.poll():
			midiEvents = detect.read(10)
			vel = midiEvents[0][0][2]

			# print(midiEvents)
			while (i != len(midiEvents)):
				if (midiEvents[i][0][1] != 0):
					print(midiEvents[i])
					note.append(midiEvents[i][0][1])
				i = i + 1
			i = 0
		else:
			midiEvents = [[[0, 0, 0], -1]]

		if (len(note) != 0):
			if (int(midiEvents[0][1]) - prev_note_time[0] <= 50 and int(midiEvents[0][1]) - prev_note_time[0] > 0):
				while (i != len(note)):
					file.write("," + str(note[i]))
					i = i + 1
					#print(", ", midiEvents, end="", sep="")
				i = 0
			else:
				while (j != len(prev_note_time[1])):
					window.blit(touch[0][vpiano[prev_note_time[1][j]][3]], vpiano[prev_note_time[1][j]][2])
					j = j + 1
				j = 0
				prev_note_time = [0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
				if (first == 0):
					first = 1
					file.write(str(note[0]))
					i = 1
					while (i != len(note)):
						file.write("," + str(note[i]))
						i = i + 1
					i = 0
				else:
					file.write("\n" + str(note[0]))
					i = 1
					while (i != len(note)):
						file.write("," + str(note[i]))
						i = i + 1
					i = 0
				#print("\n", midiEvents, end="", sep="")
			while (i != len(vpiano)):
				while (j != len(note)):
					if (int(note[j]) == vpiano[i][1]):
						window.blit(touch[1][vpiano[i][3]], vpiano[i][2])
						prev_note_time[1].append(i)
					j = j + 1
				j = 0
				i = i + 1
			pygame.display.update()
			prev_note_time[0] = int(midiEvents[0][1])
			i = 0
			j = 0
	file.close()

def input_text(window, detect):
	name = str("")
	writing = True

	myfont = pygame.font.SysFont("monospace", 38, True)

	while (writing == True):
		for event in pygame.event.get():
			if (event.type == KEYDOWN):
				if (event.key == K_RETURN):
					writing = False
				if (event.key == K_ESCAPE):
					return
				if (event.key == K_a):
					if (len(name) < 20):
						name = name + "a"
				if (event.key == K_b):
					if (len(name) < 20):
						name = name + "b"
				if (event.key == K_c):
					if (len(name) < 20):
						name = name + "c"
				if (event.key == K_d):
					if (len(name) < 20):
						name = name + "d"
				if (event.key == K_e):
					if (len(name) < 20):
						name = name + "e"
				if (event.key == K_f):
					if (len(name) < 20):
						name = name + "f"
				if (event.key == K_g):
					if (len(name) < 20):
						name = name + "g"
				if (event.key == K_h):
					if (len(name) < 20):
						name = name + "h"
				if (event.key == K_i):
					if (len(name) < 20):
						name = name + "i"
				if (event.key == K_j):
					if (len(name) < 20):
						name = name + "j"
				if (event.key == K_k):
					if (len(name) < 20):
						name = name + "k"
				if (event.key == K_l):
					if (len(name) < 20):
						name = name + "l"
				if (event.key == K_m):
					if (len(name) < 20):
						name = name + "m"
				if (event.key == K_n):
					if (len(name) < 20):
						name = name + "n"
				if (event.key == K_o):
					if (len(name) < 20):
						name = name + "o"
				if (event.key == K_p):
					if (len(name) < 20):
						name = name + "p"
				if (event.key == K_q):
					if (len(name) < 20):
						name = name + "q"
				if (event.key == K_r):
					if (len(name) < 20):
						name = name + "r"
				if (event.key == K_s):
					if (len(name) < 20):
						name = name + "s"
				if (event.key == K_t):
					if (len(name) < 20):
						name = name + "t"
				if (event.key == K_u):
					if (len(name) < 20):
						name = name + "u"
				if (event.key == K_v):
					if (len(name) < 20):
						name = name + "v"
				if (event.key == K_w):
					if (len(name) < 20):
						name = name + "w"
				if (event.key == K_x):
					if (len(name) < 20):
						name = name + "x"
				if (event.key == K_y):
					if (len(name) < 20):
						name = name + "y"
				if (event.key == K_z):
					if (len(name) < 20):
						name = name + "z"
				if (event.key == K_UNDERSCORE):
					if (len(name) < 20):
						name = name + "_"
				if (event.key == K_MINUS):
					if (len(name) < 20):
						name = name + "-"
				if (event.key == K_DELETE or event.key == K_BACKSPACE):
					name = name[:-1]
		pygame.draw.rect(window, (150, 150, 150), (1176, 872, 583, 68))
		window.blit(myfont.render(name + "|", 1, (255,0,0)), (1190, 885))
		pygame.display.update()
		clockFps.tick(maxFps)
	create_the_song(window, "./song/" + name, detect)