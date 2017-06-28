all: A B

A: outputA.txt
	cat $<

outputA.txt: mainptA.py
	python $< > $@

B: outputB.txt
	cat $<

outputB.txt: mainptB.py
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputA.txt outputB.txt *.pyc
