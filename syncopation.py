
import math
from itertools import combinations, permutations

def is_syncopated(meter, rhythm): ###tuples
	for i in range(len(rhythm) - 1):
		if is_weak_beat(i, meter) and rhythm[i] == 1 and rhythm[i + 1] == 0:
			return True
	return False

def strong_beats(meter):
	strong_beats = []
	if math.floor(meter[0] / 3.0) == meter[0] / 3.0:
		return 3
	elif math.floor(meter[0] / 2.0) == meter[0] / 2.0:
		return 2

def is_strong_beat(beat_number, meter):
	s = strong_beats(meter)
	return beat_number / s == beat_number / float(s)

def is_weak_beat(beat_number, meter):
	if is_strong_beat(beat_number, meter):
		return False
	return True

def comb_to_rhythm(comb,length): ## comb is list? takes combination list object and turns it into 
## rhythm situation, don't remember what's going on here exactly
	l = []
	for i in range(length):
		l.append(0)
	for c in comb:
		l[c] = 1
	return l 




def count_syncopations(num_notes, length, meter):
	meter = meter
	c = combinations(range(length),num_notes)
	sync = 0
	nsync = 0
	for comb in list(c):
		rhythm = comb_to_rhythm(comb,length)
		
		if is_syncopated(meter, rhythm):
			sync = sync + 1
		else:
			nsync = nsync + 1
	return (sync, nsync, sync / float(nsync))

for i in range(12):
	print count_syncopations(i, 12, (6,8))






