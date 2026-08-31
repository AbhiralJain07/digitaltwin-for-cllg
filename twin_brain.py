import json, time

while True:
    try:
        with open('physical_data.json') as f:
            physical = json.load(f)
        
        queue = physical['queue_length']
        
        # Twin Logic - This is AI part
        avg_service_time_per_student = 0.5 # mins
        predicted_wait = queue * avg_service_time_per_student
        
        if predicted_wait > 10:
            status = "CRITICAL RUSH"
            action = "Open 2nd counter immediately"
        elif predicted_wait > 5:
            status = "MODERATE"
            action = "Prepare 2nd counter"
        else:
            status = "NORMAL"
            action = "1 counter enough"

        # What-if Simulation (This is Digital Twin power)
        what_if_2_counters = (queue * 0.5) / 2

        twin_state = {
            "live_queue": queue,
            "predicted_wait_mins": round(predicted_wait, 1),
            "status": status,
            "action_recommended": action,
            "what_if_analysis": {
                "if_1_counter": f"{predicted_wait} mins wait",
                "if_2_counters": f"{round(what_if_2_counters, 1)} mins wait"
            },
            "timestamp": physical['timestamp']
        }

        with open('twin_state.json', 'w') as f:
            json.dump(twin_state, f)
            
    except:
        pass
    time.sleep(2)