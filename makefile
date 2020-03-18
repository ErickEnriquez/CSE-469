build-file: Main.py
	cp Main.py bchoc
	chmod +x bchoc

clean:
	rm bchoc 

init_test:
	./bchoc init

verify_test:
	./bchoc verify

checkin_test:
	./bchoc checkin -i 123456789

checkout_test:
	./bchoc checkout -i 987654321

add_one_test:
	./bchoc add -c 012219321938 -i 231923812038

add_many_test:
	./bchoc add -c 01312213 -i 88978971239 29308123982190 613821903821983 413129038