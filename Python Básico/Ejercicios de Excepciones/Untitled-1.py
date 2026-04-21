def ask_for_user_information():
	try:
		age = int(input('Ingrese su edad'))
		if age < 1 or age > 100:
			raise ValueError()

	except ValueError as ex:
		print("Ingrese una edad valida!")
		raise ex


def main():
	try:
		ask_for_user_information()
		# create_order()

	except Exception as ex:
		exit()


if __name__ == '__main__':
	main()