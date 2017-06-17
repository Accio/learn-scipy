"David's first module"

GCs = ('g','c')

def gc_count(seq):
        gc=0;
        for n in seq.lower():
                if n in GCs:
                        gc = gc + 1
        return(gc)

def gc_perc(seq):
	return(gc_count(seq)/len(seq))


