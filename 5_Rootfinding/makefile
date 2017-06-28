all: A B

B: outputB.txt
	cat $<

outputB.txt: mainptB.py findroots.py
	python $< > $@

A: outputA.txt
	cat $<

outputA.txt: mainptA.py findroots.py equations.py
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputA.txt outputB.txt *.pyc
