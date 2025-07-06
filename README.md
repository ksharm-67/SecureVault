# SecureVault Password Manager


### Description

This is a command line (CLI) based password manager that securely stores a user's account info using AES-CBC encryption and PBKDF2 for key derivation, with password protected access.

### Features

1. Master password setup (using PBKDF2) and authentication

2. AES-CBC encryption of stored passwords using a per-session derived key

3. PBKDF2-HMAC-SHA256 key derivation with salt and high iteration (100,000) count

4. Encrypted storage of credentials using Python's pickle module

5. Add, view, delete, and list all stored credentials

6. Change master password

### How It Works

- When the vault is first run, you're prompted to create a master password.

- A random salt is generated, and your master password is hashed with PBKDF2.

- All future logins verify the master password using that hash.

- Passwords for services are encrypted using AES-CBC with a key derived from the same master password and salt.

- The IV is prepended to the ciphertext and stored.

- Data is serialized with pickle and saved in local .vault files.

### Files

main.py: Program entry point and CLI

vault.py: Vault management (create, store, read, delete)

crypto.py: Password hashing and master password verification

AESencryption.py: AES-CBC encryption and decryption helpers

strength.py: To help calculate the randomness and security of the master password

brute_force.py: To help secure the vault against brute-force hacks

### Usage

python main.py

You'll be prompted to log in or set up a new vault.

#### Options after login:

- Find a password for a given service

- Store a new password

- Delete a stored credential

- View all stored credentials (decrypted)

- Change master password

- Log out

### Security

- Encryption: AES-256-CBC with random IVs

- Key Derivation: PBKDF2-HMAC-SHA256, 100,000 iterations

- Storage: All data is stored locally and encrypted. No plaintext passwords are saved.

- Dependencies: Uses pycryptodome for AES and padding

### Requirements

- Python 3.6+

- pycryptodome

##### Can be installed using 

``pip install pycryptodome``

#### License

MIT License