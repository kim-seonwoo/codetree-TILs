def right_shift(s, k):
    # 오른쪽으로 k번 shift
    return s[-k:] + s[:-k]

def run_length_encoding(s):
    if not s:
        return 0
    
    encoded_length = 0
    current_char = s[0]
    count = 1
    
    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded_length += 1 + len(str(count))
            current_char = char
            count = 1
    
    encoded_length += 1 + len(str(count))
    return encoded_length

def find_min_rle_length(s):
    n = len(s)
    min_length = float('inf')
    
    for k in range(n):
        shifted_string = right_shift(s, k)
        rle_length = run_length_encoding(shifted_string)
        if rle_length < min_length:
            min_length = rle_length
    
    return min_length

# 입력 받기
input_string = input().strip()

# 최소 RLE 길이 찾기
result = find_min_rle_length(input_string)
print(result)