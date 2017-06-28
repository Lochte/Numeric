all: A B C

A: outA.txt
	cat $<

outA.txt: mainptA.py QRdecomp.py
	python $< > $@

B: outB.txt
	cat $<

outB.txt: mainptB.py givens.py
	python $< > $@

C: outC.txt
	cat $<

outC.txt: mainptC.py givens.py
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outA.txt outB.txt outC.txt *.pyc
