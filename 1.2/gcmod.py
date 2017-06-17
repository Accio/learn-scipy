"A module for GC content"

GCs = ('g','c')

def gc_count(seq):
        gc=0;
        for n in seq.lower():
                if n in GCs:
                        gc = gc + 1
        return(gc)

def gc_perc(seq):
	return(gc_count(seq)/len(seq))

if __name__ == '__main__':
	demoseq = 'ATGCTGCA'
	print("Demo seq: " + demoseq)
	print("GC count: " + str(gc_count(demoseq)))
	print("GC perc: " + str(gc_perc(demoseq)))
