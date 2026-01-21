def profile_checker(profile, first, second, rate_input, service_detection_check):
    if profile == "Quick scan":
        profile_check_first_entry = 1
        profile_check_second_entry = 1024
        profile_check_rate = 0.1
        profile_check_service = False


    elif profile == "Full TCP scan":
        profile_check_first_entry = 1
        profile_check_second_entry = 65535
        profile_check_rate = 0.2
        profile_check_service = False
    
    elif profile == "Aggressive / Detect":
        profile_check_first_entry = 1
        profile_check_second_entry = 65535
        profile_check_rate = 0.1
        profile_check_service = True

    elif profile == "Custom":
        try:
            profile_check_first_entry = int(first)
            profile_check_second_entry = int(second)
            profile_check_rate = float(rate_input)
            profile_check_service = service_detection_check

        except (ValueError, TypeError):
            return None, None, None, None

    return profile_check_first_entry, profile_check_second_entry, profile_check_rate, profile_check_service

def advanced_settings_refresh(profile, first_entry, second_entry, rate_input, range_label, minus_label, scan_rate_label, second_label, service_detection_check):
    if profile == "Custom":
        range_label.configure(text_color = "white")
        first_entry.configure(state = "normal", placeholder_text = "1")
        minus_label.configure(text_color = "white")
        second_entry.configure(state = "normal", placeholder_text = "65535")
        scan_rate_label.configure(text_color = "white")
        rate_input.configure(state = "normal", placeholder_text = "0.1")
        second_label.configure(text_color = "white")
        service_detection_check.configure(state = "normal")
    else:
        range_label.configure(text_color = "#6b7070")
        first_entry.configure(state = "disabled", placeholder_text = "")
        minus_label.configure(text_color = "#6b7070")
        second_entry.configure(state = "disabled", placeholder_text = "1")
        scan_rate_label.configure(text_color = "#6b7070")
        rate_input.configure(state = "disabled", placeholder_text = "")
        second_label.configure(text_color = "#6b7070")
        service_detection_check.configure(state = "disabled")