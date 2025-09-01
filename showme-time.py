from datetime import datetime

def main():
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {today}")

if __name__ == "__main__":
    main()
