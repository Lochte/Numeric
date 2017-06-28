all: A

A: output.txt
	cat $<

output.txt: main.py LSbyQR.py
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r output.txt *.pyc
	rm -f lsfit.png
