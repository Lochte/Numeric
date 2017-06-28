A : main-A.py
	python3 main-A.py > out.A.txt
	python3 main-A.py


clean:
	rm -f main-A out.A.txt correct.txt

check: out.A.txt correct.txt
	@echo "checking target A ..."
	@diff --brief out.A.txt correct.txt
	@echo "target A seems to be ok ..."
correct.txt:
	echo "hello, $(shell whoami)" > correct.txt
#	echo "hello, `whoami`" > correct.txt
#	echo "hello, $$(whoami)" > correct.txt
