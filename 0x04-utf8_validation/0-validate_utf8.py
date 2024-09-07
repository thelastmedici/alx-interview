#!/usr/bin/python3
"""
Return:
True if the data is a valid UTF-8 encoding
False otherwise
Details:
A character in UTF-8 can be 1 to 4 bytes long.
The data set may contain multiple characters.
The data is represented by a list of integers.
Each integer represents one byte of data, so you only need to work with the 8 least significant bits of each integer.
"""


def validUTF8(data):
    """_summary_

    Args:
            data (list[int]): a list of integers
    """
    expected_continuation_bytes = 0

    # Define bit patterns for UTF-8 encoding
    UTF8_BIT_1 = 1 << 7  # 10000000
    UTF8_BIT_2 = 1 << 6  # 01000000

    # Loop over each byte in the input data
    for byte in data:
        # Initialize a mask to check for leading
        # 1's in the current byte
        leading_one_mask = 1 << 7

        # If we are not currently expecting any
        # continuation bytes
        if expected_continuation_bytes == 0:
            # Count the number of leading 1's in the
            # current byte to determine the number of
            # continuation bytes
            while leading_one_mask & byte:
                expected_continuation_bytes += 1
                leading_one_mask = leading_one_mask >> 1

            # If the byte is not a multi-byte sequence,
            # move to the next byte
            if expected_continuation_bytes == 0:
                continue

            if expected_continuation_bytes == 1 or\
                    expected_continuation_bytes > 4:
                return False
        else:
            
            if not (byte & UTF8_BIT_1 and not (byte & UTF8_BIT_2)):
                return False

        # Decrement the expected number of continuation bytes
        expected_continuation_bytes -= 1

    if expected_continuation_bytes == 0:
        return True
    else:
        return False