def show_triage(patients):
    if len(patients) == 0:
        print("Triage queue is empty.")
        return

    print("\n================ EMERGENCY TRIAGE ================")
    position = 1

    # check priorities 1, then 2, then 3
    current_rank_to_check = 1

    while current_rank_to_check <= 3:
        for p_id in patients:
            info = patients[p_id]

            # if the patient matches the rank we are looking for, print them
            if info["priority_rank"] == current_rank_to_check:
                print("Position #" + str(position) + " | ID: " + p_id + " | Name: " + info['name'] + " | Status: [" +
                      info['priority_name'] + "]")
                position = position + 1

        # move on to the next priority level
        current_rank_to_check = current_rank_to_check + 1

    print("==================================================")