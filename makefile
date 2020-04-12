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

add_1_more:
	./bchoc add -c fce7da5c-4994-45db-9440-0b872895db01 -i 3537722545

add_many_test:
	./bchoc add -c 954a9eb9-f7db-442a-a08c-e5826584543d -i 1547161094 -i 2630006027 -i 1036897748 -i 2897527353 -i 3953455618 -i 3412673101 -i 3235388174