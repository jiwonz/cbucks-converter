import os
from beaupy import select

def main():
	while True:
		options = ["CBUCKS","KRW", "USD", "ROBUX"]
		print("Choose currency unit")
		unit = select(options, cursor="🢧", cursor_style="cyan")
		os.system("cls")
		money = float(input(f"{unit}: "))
		cbucks = float()
		print()
		match unit:
			case "KRW":
				cbucks = money*(320/3360)
			case "USD":
				cbucks = money*(320/2.5)
			case "ROBUX":
				cbucks = money*(320/200)
			case "CBUCKS":
				cbucks = money
				krw = cbucks*(3360/320)
				usd = cbucks*(2.5/320)
				robux = cbucks*(200/320)
				print(f"KRW: {round(krw)} \\")
				print(f"USD: {round(usd)} $")
				print(f"ROBUX: {round(robux)} R$")
				print()
				input("press RETURN to continue")
				os.system("cls")
				continue
		print(f"CBUCKS: {round(cbucks)} C$")
		print()
		input("press RETURN to continue")
		os.system("cls")

if __name__ == "__main__":
	main()