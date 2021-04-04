import random
import time
import math


symbols = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ .,"
P = 797

def is_prime(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0: 
            return False
    return number > 1

def count_c(p):
	prime_numbers = []
	for i in range(2, p-1):
		if i%2 !=0 and is_prime(i) and gratest_commot_divisor(i, p-1)[0] == 1:
			prime_numbers.append(i)

	return random.choice(prime_numbers)

def count_d(c, p):
	d = gratest_commot_divisor(p-1, c)[2]
	if d < 0:
		d += p-1
	if (c*d)%(p-1) == 1:
		return d

def get_message_from_file(file_name):
	message_text = ''
	with open(file_name, encoding='utf-8') as f:
		message_text = f.read()

	return message_text

def dump_message_to_file(file_name, message):
	with open(file_name, 'w') as f:
		f.write(message)

def divide_line_on_blocks(line, block_length):
	return [line[i:i+block_length] for i in range(0, len(line), block_length)]

def get_symbol_by_code(symbol_code):
	return symbols[symbol_code - 10]

def get_code_by_symbol(symbol):
	return symbols.index(symbol) + 10

def convert_message_to_code(message):
	encoded_message = ''
	for symbol in message:
		encoded_message += str(get_code_by_symbol(symbol))

	return encoded_message

def convert_message_to_symbols(encoded_message):
	decoded_message = ''
	for i in divide_line_on_blocks(encoded_message, 2):
		decoded_message += get_symbol_by_code(int(i))

	return decoded_message

def gratest_commot_divisor(num1, num2):
	
	u = (num1, 1, 0)
	v = (num2, 0, 1)

	while v[0] != 0:
		q = u[0]//v[0]
		t = (u[0]%v[0],u[1]- q*v[1], u[2]- q*v[2])
		u = v
		v = t

	return u

def fast_pow(x, y):
	if y == 0:
		return 1

	if y == -1:
		return 1./x

	p = fast_pow(x, y // 2)
	p *= p

	if y % 2:
		p *= x

	return p

def main():
	message = get_message_from_file('message_to_send.txt')

	c_a = count_c(P)
	d_a = count_d(c_a, P)


	c_b = count_c(P)
	d_b = count_d(c_b, P)

	encoded_message = convert_message_to_code(message)
	encoded_message = divide_line_on_blocks(encoded_message, 2)

	recieved_message = []
	for block in encoded_message:
		x1 = fast_pow(int(block), c_a) % P
		x2 = fast_pow(x1, c_b) % P
		x3 = fast_pow(x2, d_a) % P
		x4 = fast_pow(x3, d_b) % P

		recieved_message.append(str(x4))

	recieved_message = convert_message_to_symbols(''.join(recieved_message))

	dump_message_to_file('recieved_message.txt', recieved_message)






if __name__ == '__main__':
	main()