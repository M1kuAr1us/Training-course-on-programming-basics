def frame_text(symbol):
    def decorator(func):
        def inner(*args, **kwargs):
            text = func(*args, **kwargs)

            framed_line = f"{symbol} {text} {symbol}"
            border = symbol * len(framed_line)

            return f"{border}\n{framed_line}\n{border}"
        
        return inner

    return decorator

symbol_decorator = input("Enter the symbol (decorator): ")
input_text = input("Enter the text:\n")

@frame_text(symbol_decorator)
def get_text():
    return input_text

print(get_text())