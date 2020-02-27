#!/usr/bin/python3

from include import *

def verif_format(song):
	file = open(song, "r")
	parsing = (file.read()).split("\n")
	i = 0
	j = 0

	if (parsing == ['']):
		return (False)

	while (i != len(parsing)):
		parsing[i] = parsing[i].split(",")
		while (j != len(parsing[i])):
			if (parsing[i][j] == ""):
				return (False)
			elif (int(parsing[i][j]) > 96 or int(parsing[i][j]) < 36):
				return (False)
			else:
				j = j + 1
		j = 0
		i = i + 1
	file.close()
	return (parsing)