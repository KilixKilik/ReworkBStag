# Rework on https://github.com/NotCat40/BrawlStarsTagGenerator
# Brawl Stars ID <-> Hashtag converter

class logic:
    def __init__(self, high, low):
        self.high = high
        self.low = low
    
    def __str__(self):
        return f"High: {self.high}, Low: {self.low}"

CONVERSION_CHARS = "0289PYLQGRJCUV"

def baza(value, chars=CONVERSION_CHARS):
    # Convert decimal to custom base
    code = [''] * 12
    base = len(chars)
    
    for i in range(11, -1, -1):
        code[i] = chars[value % base]
        value //= base
        if value == 0:
            return ''.join(code[i:])
    return ''.join(code)

def idk(code, chars=CONVERSION_CHARS):
    # Convert custom base to decimal
    base = len(chars)
    result = 0
    for char in code:
        idx = chars.find(char)
        if idx == -1:
            return -1
        result = result * base + idx
    return result

def id_to_hashtag(id_value, high_id=0):
    # Convert ID to hashtag
    if high_id >= 256:
        return None
    value = (id_value << 8) | high_id
    return '#' + baza(value)

def hashtag_to_id(code):
    # Convert hashtag to ID
    if len(code) >= 14 or not code.startswith('#'):
        return logic(-1, -1)
    id_code = code[1:]
    id_value = idk(id_code)
    if id_value == -1:
        return logic(-1, -1)
    high = id_value & 0xFF
    low = (id_value >> 8) & 0x7FFFFFFF
    return logic(high, low)

if __name__ == "__main__":
    print("Brawl Stars Tag Converter")
    print("1. Convert ID to hashtag")
    print("2. Convert hashtag to ID")
    
    choice = input("\nChoose option (1/2): ").strip()
    
    if choice == "1":
        try:
            id_value = int(input("Enter ID number: "))
            high_id_input = input("Enter High ID (default 0): ").strip()
            high_id = int(high_id_input) if high_id_input else 0
            
            if high_id >= 256:
                print("\nError: High ID must be less than 256")
            else:
                hashtag = id_to_hashtag(id_value, high_id)
                print(f"\nHashtag: {hashtag}")
        except ValueError:
            print("\nError: Please enter valid numbers")
    
    elif choice == "2":
        code = input("Enter hashtag (e.g. #QYUURGGQ): ").strip()
        result = hashtag_to_id(code)
        
        if result.high == -1 and result.low == -1:
            print("\nError: Invalid hashtag format")
        else:
            print(f"\nHigh: {result.high}, Low: {result.low}")
    
    else:
        print("\nInvalid choice. Please enter 1 or 2.")

# by kerikush