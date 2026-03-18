# Coding Task: Greetings by Time of Day

Implement the function `get_greeting(hour)` that returns the correct English greeting based on the hour of the day.

## Rules

| Hour | Greeting |
|------|----------|
| 0 – 11 | `Good morning!` |
| 12 – 17 | `Good afternoon!` |
| 18 – 21 | `Good evening!` |
| 22 – 23 | `Good night!` |

## Expected Examples

```python
get_greeting(8)   # → 'Good morning!'
get_greeting(14)  # → 'Good afternoon!'
get_greeting(19)  # → 'Good evening!'
get_greeting(23)  # → 'Good night!'
```

## Instructions

Complete the function using `if / elif / else`.

💡 **Hint:** Start with `if hour < 12:` to catch morning hours.
