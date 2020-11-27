# format of the student ID is jc123456
# starts with jc and has 8 numbers after jc
STUDENT_ID_LENGTH = 10


def is_valid_student_id(string):
    valid_student_id = False
    if len(string) == STUDENT_ID_LENGTH:  # length of the id is 10
        prefix = string[0:2]  # pick first 2 characters
        if prefix.lower() == "jc":  # only if prefix is jc, then we check further
            student_number = string[2:]  # pick the string from position 2 onwards
            # need to check all are digits
            if student_number.isdigit():
                valid_student_id = True

    return valid_student_id


def main():
    # 1. incorrect length
    is_valid1 = is_valid_student_id("jc9999999999999")  # returns false

    # 2. incorrect prefix
    is_valid2 = is_valid_student_id("cd12345678")  # returns false

    # 3. incorrect student number
    is_valid3 = is_valid_student_id("jc123 5678")  # returns false

    # 4. valid case
    is_valid4 = is_valid_student_id("jc12345678")  # returns True

    print(is_valid1)
    print(is_valid2)
    print(is_valid3)
    print(is_valid4)


main()
