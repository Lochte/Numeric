all: A B

A: outA.txt
	cat $<

outA.txt: mainptA.py
	python $< > $@

B: outB.txt
	cat $<

outB.txt: mainptB.py
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outA.txt outB.txt
