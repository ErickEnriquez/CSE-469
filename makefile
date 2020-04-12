make: Main.py
	cp Main.py bchoc
	chmod +x bchoc

clean:
	rm bchoc 
	rm data.bin

init_test:
	./bchoc init

verify_test:
	./bchoc verify

checkin_test:
	./bchoc checkin -i 123456789

checkout_test:
	./bchoc checkout -i 987654321

add_one_test:
	./bchoc add -c fce7da5c-4994-45db-9440-0b872895db01 -i 3537722555

add_many_test:
	./bchoc add -c 12345678123456781234567812345678 -i 8891239 29390 6138219 413138