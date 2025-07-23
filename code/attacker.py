import hashlib

target_hash = "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3"

# Dictionary attack
with open("rockyou.txt", "r", encoding="latin-1") as f:
	for line in f:
		guess = line.strip()
		if hashlib.sha256(guess.encode()).hexdigest() == target_hash:
			print(f"Password found: {guess}")
			break
