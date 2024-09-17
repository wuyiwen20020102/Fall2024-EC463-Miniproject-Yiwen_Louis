import urequests as requests
from machine import Pin
import network
import time
import random
import json
import network
import time

N: int = 10
sample_ms = 10.0
on_ms = 500

#firebase realtime database URL 
firebase_url = "https://ec463-miniproject-aae95-default-rtdb.firebaseio.com/"

SSID = 'BU Guest (unencrypted)'

#connect to BU guest Wifi
def wificonnection (ssid):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    
    wlan.connect(ssid)

    while not wlan.isconnected():
        print("attempting to connect to WiFi")
        time.sleep(1)
    
    print("connected to WiFi")
    print(f"IP Address: {wlan.ifconfig()[0]}")

wificonnection(SSID)

def random_time_interval(tmin: float, tmax: float) -> float:
    """Return a random time interval between max and min"""
    return random.uniform(tmin, tmax)

def blinker(N: int, led: Pin) -> None:
    # %% let user know game started / is over

    for _ in range(N):
        led.high()
        time.sleep(0.1)
        led.low()
        time.sleep(0.1)

def write_json(json_filename: str, data: dict) -> None:
    """Writes data to a JSON file.

    Parameters
    ----------

    json_filename: str
        The name of the file to write to. This will overwrite any existing file.

    data: dict
        Dictionary data to write to the file.
    """

    with open(json_filename, "w") as f:
        json.dump(data, f)

def scorer(t: list[int | None]) -> dict:
    # %% collate results
    misses = t.count(None)
    print(f"You missed the light {misses} / {len(t)} times")

    t_good = [x for x in t if x is not None]

    #compute average, minimum, maximum response time
    min_val = min(t_good)
    max_val = max(t_good)
    mean_val = sum(t_good)/N
    score = (len(t_good))/N

    print("min:", min_val, "max:", max_val, "mean:", mean_val, "score:", score)

    data = {
        "min": min_val,
        "max": max_val,
        "mean": mean_val,
        "score": score
    }
    return data

def push_to_database(user: str, data: dict) -> None:
    # using "if __name__" allows us to reuse functions in other script files
    headers = {
        'Content-Type': 'application/json',
    }
    
    #store in json file 
    entry_url = f"{firebase_url}/{user}.json"
    
    #request to update data 
    response = requests.put(entry_url, json=data, headers=headers)
    
    if response.status_code == 200:
        print(f"Data successfully uploaded: {user}")
    else:
        print(f"Failed to upload data: {response.status_code}, Response: {response.text}")

if __name__ == "__main__":
    # using "if __name__" allows us to reuse functions in other script files
    led = Pin("LED", Pin.OUT)
    button = Pin(16, Pin.IN, Pin.PULL_UP)

    t = []

    blinker(3, led)

    for i in range(N):
        time.sleep(random_time_interval(0.5, 5.0))

        led.high()

        tic = time.ticks_ms()
        t0 = None
        while time.ticks_diff(time.ticks_ms(), tic) < on_ms:
            if button.value() == 0:
                t0 = time.ticks_diff(time.ticks_ms(), tic)
                led.low()
                break
        t.append(t0)

        led.low()

    blinker(5, led)

    data = scorer(t)

    user = "user"
    
    push_to_database(user, data)
