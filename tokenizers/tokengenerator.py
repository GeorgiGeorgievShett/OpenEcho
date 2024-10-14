import random
import string


def generate_cookie_values():
    # Generate 'OAID' value: example 16 alphanumeric characters
    oaid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

    # Generate 's' value: example 16 alphanumeric characters
    s_value = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

    # Generate 't' value: follow the same format as before
    part1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=2))  # e.g., 'a1'
    part2 = ''.join(random.choices(string.ascii_lowercase + string.digits + '_-', k=3))  # e.g., 'b-c'
    part3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=2))  # e.g., '34'
    part4 = ''.join(random.choices(string.ascii_lowercase + string.digits + '_-', k=1))  # e.g., 'a'
    part5 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=2))  # e.g., '56'
    part6 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=2))  # e.g., '78'
    t_value = f"{part1}_{part2}-{part3}_s.{part4}{part5}.{part6}.bg"

    # Generate 'vid' value: example 16 alphanumeric characters
    vid = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

    # Fixed value for 'current_page'
    current_page = 'mailbox/inbox'

    return {
        'OAID': oaid,
        'current_page': current_page,
        's': s_value,
        't': t_value,
        'vid': vid
    }


# Generate and print cookie values
cookie_values = generate_cookie_values()
for key, value in cookie_values.items():
    print(f"'{key}': '{value}'")
