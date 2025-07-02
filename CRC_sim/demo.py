def xor(a, b):
    result = ""
    for i in range(1, len(b)):
        result += str(int(a[i]) ^ int(b[i]))
    return result

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    codeword = data + remainder
    return codeword, remainder

# --- DỮ LIỆU MẪU ---
data = "110101000"     # P
key = "1011"           # G

print("Dữ liệu gốc (P):", data)
print("Đa thức sinh (G):", key)

codeword, crc = encodeData(data, key)

print("Phần dư CRC (R):", crc)
print("Chuỗi truyền đi (D = P + R):", codeword)

# --- Mô phỏng kiểm tra tại bên nhận ---
received = codeword  # giả sử truyền đúng

check = mod2div(received, key)
print("Kiểm tra tại bên nhận (P(x) mod G(x)):", check)

if "1" in check:
    print("❌ Lỗi phát hiện trong dữ liệu nhận")
else:
    print("✅ Dữ liệu nhận hợp lệ (không lỗi)")

