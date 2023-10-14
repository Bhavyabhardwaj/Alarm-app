# first install playsound Module


from playsound import playsound
import time

CLEAR = ("\033[H\033[J")
# CLEAR_AND_RETURN = '\033[H]'

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60  # Gives the remainder like 125 % 60 = 2 min. 5 seconds

        time_str = f"{minutes_left:02d}:{seconds_left:02d}"
        print(f"Alarm will sound in: {time_str}")

        playsound("Alarm.mp3")  # Use the file's location if it's in a different directory.

def main():
    minutes = int(input("How many minutes to wait: "))
    seconds = int(input("How many seconds to wait: "))
    total_seconds = minutes * 60 + seconds
    alarm(total_seconds)

if __name__ == "__main__":
    main()
