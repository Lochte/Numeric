all: Exam

Exam: outputExam.txt
	cat $<

outputExam.txt: mainExam.py
	python $< > $@

clean:
	rm -rf __pycache__
	rm -r outputExam.txt *.pyc
