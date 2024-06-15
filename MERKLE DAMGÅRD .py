import hashlib

# Padding function for Merkle-Damgård construction
def pad_message(message, block_size):
    padding_size = block_size - (len(message) % block_size)
    padding = b"\x80" + b"\x00" * (padding_size - 1)
    return message + padding


def merkle_damgard_construction(message, block_size, compression_function):
    # Pad the message to a multiple of the block size
    padded_message = pad_message(message, block_size)
    
    # Divide the padded message into blocks
    blocks = [padded_message[i:i+block_size] for i in range(0, len(padded_message), block_size)]
    
    # Initialize the hash value (initialization vector)
    hash_value = b"\x00" * block_size
    
    # Process each block
    for block in blocks:
        # Apply the compression function to update the hash value
        hash_value = compression_function(block, hash_value)
    
    return hash_value

# Example compression function (SHA-256)
def sha256(block, hash_value):
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the block and current hash value
    sha256.update(block + hash_value)
    
    # Return the resulting hash value
    return sha256.digest()

# Example usage
message = b"this is a test for Merkle Damgard construction"
block_size = 512    # SHA-256 uses a block size of 512 bytes

# Calculate the hash using Merkle-Damgård construction with SHA-256
hash_value = merkle_damgard_construction(message, block_size, sha256)

print("Hash:", hash_value.hex())
