def calc_parity_bits(m):
    r = 0
    while (2**r < m + r + 1):
        r += 1
    return r


def pos_parity_bits(data, r):
    j = 0
    k = 1
    m = len(data)
    res = ''

    # Insert parity bits at positions that are powers of 2
    for i in range(1, m + r + 1):
        if i == 2**j:
            res += '0'
            j += 1
        else:
            res += data[-k]   # from right
            k += 1

    return res[::-1]  # reverse back


def calc_parity(res, r):
    n = len(res)
    res = list(res)

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val ^= int(res[-j])  # check bits from right
        res[-(2**i)] = str(val)      # set parity bit

    return ''.join(res)


def detect_error(data, r):
    n = len(data)
    data = list(data)
    res = 0

    for i in range(r):
        val = 0
        for j in range(1, n + 1):
            if j & (2**i) == (2**i):
                val ^= int(data[-j])      # from right
        res += val * (10**i)

    return int(str(res), 2)  # Binary → decimal (right side index)


# ---------------- MAIN ----------------
msg = input("Enter data bits: ")

m = len(msg)
r = calc_parity_bits(m)
arr = pos_parity_bits(msg, r)
arr = calc_parity(arr, r)

print("Encoded Hamming code is:", arr)

# Simulate error
err = list(arr)
pos = int(input("Enter position to flip bit (1 = leftmost, 0 = none): "))

if pos != 0:
    # Flip from LEFT side
    err[pos - 1] = '1' if err[pos - 1] == '0' else '0'
    err = ''.join(err)
    print("Received code with error:", err)

    error_pos = detect_error(err, r)

    if error_pos == 0:
        print("No error detected")
    else:
        # convert right-index → left-index
        left_pos = len(err) - error_pos + 1
        print("Error detected at position:", left_pos)

else:
    print("No error introduced.")
