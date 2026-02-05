from datetime import datetime
import platform
import os

print("=" * 50)
print("       Welcome to the Python World!")
print("=" * 50)
print()
print("Hello World!")
print("Greetings from this simple Python script.")
print("Hope you're having a wonderful day!")
print()
print(f"Current date: {datetime.now().strftime('%B %d, %Y, %H:%M:%S')}")
print()
print("-" * 50)
print("System Information:")
print(f"  - OS: {platform.system()} {platform.release()}")
print(f"  - Python version: {platform.python_version()}")
print(f"  - User: {os.getenv('USERNAME') or os.getenv('USER', 'Unknown')}")
print("-" * 50)
print()
print("=" * 50)
print("      Thank you for running this program!")
print("=" * 50)