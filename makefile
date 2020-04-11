make: Main.py
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
	./bchoc add -c 12345678123456781234567812345678 -i 2319

add_many_test:
	./bchoc add -c 12345678123456781234567812345678 -i 8891239 29390 6138219 413138