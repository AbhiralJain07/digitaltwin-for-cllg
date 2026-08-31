import random, time, json
from datetime import datetime

queue = 0
counter_open = 1
counter_open = 2

while True:
    # Random students coming (like real IoT sensor data)
    new_students = random.randint(0, 5) # lunch time rush
    served = random.randint(0, 3) * counter_open
    
    queue = max(0, queue + new_students - served)
    
    data = {
        "timestamp": str(datetime.now())[11:19],
        "queue_length": queue,
        "counters_open": counter_open,
        "new_arrivals": new_students
    }
    
    with open('physical_data.json', 'w') as f:
        json.dump(data, f)
    
    print(f"Physical: Queue={queue}")
    time.sleep(3)