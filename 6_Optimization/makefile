all: A

A: outputA.txt
	cat $<

outputA.txt: main.py minimization.py equations.py counter.py
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputA.txt *.pyc
