all: A

A: outputA.txt
	cat $<

outputA.txt: mainptA.py
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputA.txt *.pyc
