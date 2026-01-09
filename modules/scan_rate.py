def rate(rate_input):
    try:
        input = float(rate_input)
        if input <= 0:
            return 0.1
        else:
            return input
    except ValueError:
        return 0.1