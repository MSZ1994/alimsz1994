from datetime import datetime

print("=== Contract Signing ===")

name = input("Full name: ")

contract = """
I agree to the terms and conditions of this contract.
By signing below, I confirm that I have read and accepted them.
"""

print(contract)

confirm = input("Type 'yes' to sign: ").strip().lower()

if confirm == "yes":
    with open("signed_contract.txt", "w") as f:
        f.write(f"Signer: {name}\n")
        f.write(f"Date: {datetime.now()}\n")
        f.write("Status: Signed\n")
    print("Contract signed successfully.")
else:
    print("Signing cancelled.")
# like ev
