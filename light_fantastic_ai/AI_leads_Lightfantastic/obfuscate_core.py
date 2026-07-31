# obfuscate_core.py
# Script ini akan mengobfuscate core.py menjadi lebih sulit dibaca

import base64
import zlib
import os

def obfuscate_file(input_file, output_file):
    # Baca file asli
    with open(input_file, 'r', encoding='utf-8') as f:
        original_code = f.read()
    
    # Compress dan encode
    compressed = zlib.compress(original_code.encode())
    encoded = base64.b64encode(compressed).decode()
    
    # Buat wrapper yang akan mendekode dan mengeksekusi
    obfuscated = f'''import base64
import zlib

_exec_code = """{encoded}"""

def __get_exec_code():
    return zlib.decompress(base64.b64decode(_exec_code)).decode()

# Execute the obfuscated code
exec(__get_exec_code())
'''
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(obfuscated)
    
    print(f"Success! Obfuscated file saved as: {output_file}")
    print(f"Original size: {len(original_code)} bytes")
    print(f"Obfuscated size: {len(obfuscated)} bytes")

if __name__ == "__main__":
    # Cek apakah file core.py ada
    if not os.path.exists("core.py"):
        print("Error: core.py not found in current directory!")
        print("Please make sure core.py exists before running this script.")
    else:
        obfuscate_file("core.py", "core_obfuscated.py")
        print("\nNext steps:")
        print("1. Rename core_obfuscated.py to core.py")
        print("2. Or update main.py to import from core_obfuscated.py")