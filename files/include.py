#!/usr/bin/python3

from __future__ import print_function
from math import *
import re
import os
import contextlib
with contextlib.redirect_stdout(None):
	import pygame
	from pygame.locals import *
	import pygame.midi as midi
import sys

#variables globales

maxFps = 30
back_color = (33, 33, 33)
clockFps = pygame.time.Clock()
global_x_song = 0

### LOAD PIANO SPRITES ###

tb = pygame.image.load("src/t_black.png")
t1 = pygame.image.load("src/t_white.png")
t2 = pygame.image.load("src/t_white_l.png")
t3 = pygame.image.load("src/t_white_c.png")
t4 = pygame.image.load("src/t_white_r.png")

sb = pygame.image.load("src/s_black.png")
s1 = pygame.image.load("src/s_white.png")
s2 = pygame.image.load("src/s_white_l.png")
s3 = pygame.image.load("src/s_white_c.png")
s4 = pygame.image.load("src/s_white_r.png")

ob = pygame.image.load("src/ok_black.png")
o1 = pygame.image.load("src/ok_white.png")
o2 = pygame.image.load("src/ok_white_l.png")
o3 = pygame.image.load("src/ok_white_c.png")
o4 = pygame.image.load("src/ok_white_r.png")

kb = pygame.image.load("src/ko_black.png")
k1 = pygame.image.load("src/ko_white.png")
k2 = pygame.image.load("src/ko_white_l.png")
k3 = pygame.image.load("src/ko_white_c.png")
k4 = pygame.image.load("src/ko_white_r.png")

touch = [[tb, t1, t2, t3, t4], [sb, s1, s2, s3, s4], [ob, o1, o2, o3, o4], [kb, k1, k2, k3, k4]]

### LOAD SPRITES ###

yes_c = pygame.image.load("src/yes_c.png")
yes = pygame.image.load("src/yes.png")
no_c = pygame.image.load("src/no_c.png")
no = pygame.image.load("src/no.png")

select = pygame.image.load("src/select.png")

arrow_l_c = pygame.image.load("src/arrow_l_c.png")
arrow_l = pygame.image.load("src/arrow_l.png")
arrow_r_c = pygame.image.load("src/arrow_r_c.png")
arrow_r = pygame.image.load("src/arrow_r.png")

create = pygame.image.load("src/create.png")
start_c = pygame.image.load("src/start_c.png")
start = pygame.image.load("src/start.png")
delete = pygame.image.load("src/delete.png")
delete_c = pygame.image.load("src/delete_c.png")

song = pygame.image.load("src/song.png")
input_choice = pygame.image.load("src/input_choice.png")
input_tab = pygame.image.load("src/input_tab.png")
title = pygame.image.load("src/title.png")

play_c = pygame.image.load("src/play_c.png")
play = pygame.image.load("src/play.png")
parameters_c = pygame.image.load("src/parameters_c.png")
parameters = pygame.image.load("src/parameters.png")

### VIRTUAL PIANO ###

rect = [0, 36, (6, 710), 2]
rect2 = [0, 38, (59, 710), 3]
rect4 = [0, 40, (112, 710), 4]
rect5 = [0, 41, (165, 710), 2]
rect7 = [0, 43, (218, 710), 3]
rect9 = [0, 45, (271, 710), 3]
rect11 = [0, 47, (324, 710), 4]
rect12 = [0, 48, (377, 710), 2]
rect14 = [0, 50, (430, 710), 3]
rect16 = [0, 52, (483, 710), 4]
rect17 = [0, 53, (536, 710), 2]
rect19 = [0, 55, (589, 710), 3]
rect21 = [0, 57, (642, 710), 3]
rect23 = [0, 59, (695, 710), 4]
rect24 = [0, 60, (748, 710), 2]
rect26 = [0, 62, (801, 710), 3]
rect28 = [0, 64, (854, 710), 4]
rect29 = [0, 65, (907, 710), 2]
rect31 = [0, 67, (960, 710), 3]
rect33 = [0, 69, (1013, 710), 3]
rect35 = [0, 71, (1066, 710), 4]
rect36 = [0, 72, (1119, 710), 2]
rect38 = [0, 74, (1172, 710), 3]
rect40 = [0, 76, (1225, 710), 4]
rect41 = [0, 77, (1278, 710), 2]
rect43 = [0, 79, (1331, 710), 3]
rect45 = [0, 81, (1384, 710), 3]
rect47 = [0, 83, (1437, 710), 4]
rect48 = [0, 84, (1490, 710), 2]
rect50 = [0, 86, (1543, 710), 3]
rect52 = [0, 88, (1596, 710), 4]
rect53 = [0, 89, (1649, 710), 2]
rect55 = [0, 91, (1702, 710), 3]
rect57 = [0, 93, (1755, 710), 3]
rect59 = [0, 95, (1808, 710), 4]
rect60 = [0, 96, (1861, 710), 1]

rect1 = [1, 37, (43, 710), 0]
rect3 = [1, 39, (96, 710), 0]

rect6 = [1, 42, (202, 710), 0]
rect8 = [1, 44, (255, 710), 0]
rect10 = [1, 46, (308, 710), 0]

rect13 = [1, 49, (414, 710), 0]
rect15 = [1, 51, (467, 710), 0]

rect18 = [1, 54, (573, 710), 0]
rect20 = [1, 56, (626, 710), 0]
rect22 = [1, 58, (679, 710), 0]

rect25 = [1, 61, (785, 710), 0]
rect27 = [1, 63, (838, 710), 0]

rect30 = [1, 66, (944, 710), 0]
rect32 = [1, 68, (997, 710), 0]
rect34 = [1, 70, (1050, 710), 0]

rect37 = [1, 73, (1156, 710), 0]
rect39 = [1, 75, (1209, 710), 0]

rect42 = [1, 78, (1315, 710), 0]
rect44 = [1, 80, (1368, 710), 0]
rect46 = [1, 82, (1421, 710), 0]

rect49 = [1, 85, (1527, 710), 0]
rect51 = [1, 87, (1580, 710), 0]

rect54 = [1, 90, (1686, 710), 0]
rect56 = [1, 92, (1739, 710), 0]
rect58 = [1, 94, (1792, 710), 0]

vpiano = [rect, rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9
, rect10, rect11, rect12, rect13, rect14, rect15, rect16, rect17, rect18, rect19
, rect20, rect21, rect22, rect23, rect24, rect25, rect26, rect27, rect28, rect29
, rect30, rect31, rect32, rect33, rect34, rect35, rect36, rect37, rect38, rect39
, rect40, rect41, rect42, rect43, rect44, rect45, rect46, rect47, rect48, rect49
, rect50, rect51, rect52, rect53, rect54, rect55, rect56, rect57, rect58, rect59, rect60]

### KEYBOARD ###

krect = [9, 36]
krect2 = [97, 38]
krect4 = [122, 40]
krect5 = [101, 41]
krect7 = [114, 43]
krect9 = [116, 45]
krect11 = [121, 47]
krect12 = [117, 48]
krect14 = [105, 50]
krect16 = [111, 52]
krect17 = [112, 53]
krect19 = [36, 55]
krect21 = [13, 57]
krect23 = [304, 59]
krect24 = [60, 60]
krect26 = [119, 62]
krect28 = [120, 64]
krect29 = [99, 65]
krect31 = [118, 67]
krect33 = [98, 69]
krect35 = [110, 71]
krect36 = [44, 72]
krect38 = [59, 74]
krect40 = [58, 76]
krect41 = [33, 77]
krect43 = [303, 79]
krect45 = [282, 81]
krect47 = [283, 83]
krect48 = [284, 84]
krect50 = [285, 86]
krect52 = [286, 88]
krect53 = [287, 89]
krect55 = [288, 91]
krect57 = [289, 93]
krect59 = [290, 95]
krect60 = [291, 96]

krect1 = [38, 37]
krect3 = [233, 39]

krect6 = [39, 42]
krect8 = [40, 44]
krect10 = [45, 46]

krect13 = [95, 49]
krect15 = [231, 51]

krect18 = [41, 54]
krect20 = [61, 56]
krect22 = [8, 58]

krect25 = [113, 61]
krect27 = [115, 63]

krect30 = [102, 66]
krect32 = [103, 68]
krect34 = [104, 70]

krect37 = [107, 73]
krect39 = [108, 75]

krect42 = [109, 78]
krect44 = [249, 80]
krect46 = [42, 82]

krect49 = [292, 85]
krect51 = [293, 87]

krect54 = [278, 90]
krect56 = [279, 92]
krect58 = [277, 94]

keyboard = [krect, krect1, krect2, krect3, krect4, krect5, krect6, krect7, krect8, krect9
, krect10, krect11, krect12, krect13, krect14, krect15, krect16, krect17, krect18, krect19
, krect20, krect21, krect22, krect23, krect24, krect25, krect26, krect27, krect28, krect29
, krect30, krect31, krect32, krect33, krect34, krect35, krect36, krect37, krect38, krect39
, krect40, krect41, krect42, krect43, krect44, krect45, krect46, krect47, krect48, krect49
, krect50, krect51, krect52, krect53, krect54, krect55, krect56, krect57, krect58, krect59, krect60]
