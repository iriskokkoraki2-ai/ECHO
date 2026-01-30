"""
ECHO - A simple Python application
This is a starter template for your Replit project
"""

def main():
    """Main function that runs the ECHO application"""
    print("=" * 50)
    print("Welcome to ECHO!")
    print("=" * 50)
    
    while True:
        user_input = input("\nEnter text to echo (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("\nGoodbye! Thanks for using ECHO.")
            break
        
        print(f"ECHO: {user_input}")

if __name__ == "__main__":
    main()
