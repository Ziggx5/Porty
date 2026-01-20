def profile_checker(profile, first, second, rate_input):
    if profile == "Quick scan":
        profile_check_first_entry = 1
        profile_check_second_entry = 1024
        profile_check_rate = 0.1

    elif profile == "Full TCP scan":
        profile_check_first_entry = 1
        profile_check_second_entry = 65535
        profile_check_rate = 0.2
    
    elif profile == "Aggressive / Detect":
        profile_check_first_entry = 1
        profile_check_second_entry = 65535
        profile_check_rate = 0.1
    
    elif profile == "Custom":
        profile_check_first_entry = first
        profile_check_second_entry = second
        profile_check_rate = rate_input

    return profile_check_first_entry, profile_check_second_entry, profile_check_rate

