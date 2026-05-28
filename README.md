# Simple SHA-256 Calculator

This document explains how a simple SHA-256 calculator works.

## What is SHA-256?

SHA-256 is a cryptographic hash function that transforms any input data into a fixed 256-bit (32-byte) output. The output is usually shown as a 64-character hexadecimal string.

Key properties:
- Deterministic: same input always produces the same output.
- Fixed size: any input length gives a 256-bit digest.
- One-way: hard to reverse from output back to input.
- Collision-resistant: hard to find two different inputs with the same output.

## How the calculator works

A simple SHA-256 calculator typically follows these steps:

1. Accept input text or message.
2. Convert the input into bytes.
3. Process the bytes through the SHA-256 compression and mixing algorithm.
4. Produce a 32-byte digest.
5. Convert the digest into a hexadecimal string.

## Example

Input:

```
hello world
```

SHA-256 output:

```
b94d27b9934d3e08a52e52d7da7dabfa
c484efe37a5380ee9088f7ace2efcde9
```

## Use cases

- Verifying file integrity.
- Password hashing (with salt and additional protections).
- Blockchain and digital signatures.

## Notes

A simple calculator is useful for learning and testing, but real applications should use a trusted cryptographic library to avoid implementation errors.
