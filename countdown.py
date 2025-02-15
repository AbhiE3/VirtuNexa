import time
import threading

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02}:{secs:02}"
        print(timer_display, end="\r")
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

def main():
    try:
        duration = int(input("Enter countdown time in seconds: "))
        print("Countdown started...")
        
        thread = threading.Thread(target=countdown_timer, args=(duration,))
        thread.start()
        thread.join()
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
