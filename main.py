import subprocess
import sys

def main():
    print("MLB Spraychart Tool")
    print("=" * 40)
    print("1. Generate spray chart(s)")
    print("2. Cleanup PNG files")
    print("=" * 40)
    
    choice = input("Select an option (1 or 2): ").strip()
    
    if choice == "1":
        subprocess.run([sys.executable, ".graph.py"])
    elif choice == "2":
        subprocess.run([sys.executable, ".cleanup.py"])
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()

if __name__ == "__main__":
    main()