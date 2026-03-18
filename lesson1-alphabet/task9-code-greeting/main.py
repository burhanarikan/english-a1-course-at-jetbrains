def get_greeting(hour: int) -> str:
    """
    Return the correct English greeting based on the hour of the day.

    Args:
        hour: An integer from 0 to 23 representing the current hour.

    Returns:
        A greeting string: 'Good morning!', 'Good afternoon!',
        'Good evening!', or 'Good night!'
    """
    # TODO: implement using if / elif / else
    pass


# Test your function here:
print(get_greeting(8))   # Should print: Good morning!
print(get_greeting(14))  # Should print: Good afternoon!
print(get_greeting(19))  # Should print: Good evening!
print(get_greeting(23))  # Should print: Good night!
