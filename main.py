# 在这个文件中编写代码实现题目要求的功能
import keyword  # 建议使用这个库处理关键字
reserved_words = set(keyword.kwlist)

# 以下内容自行完成
import keyword

reserved_words = set(keyword.kwlist)

def convert_source_code(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    result = []
    in_string = False
    current_identifier = []
    
    for char in content:
        if char in ('"', "'"):
            in_string = not in_string
            result.append(char)
            continue
        
        if in_string:
            result.append(char)
            continue
        
        if char.isalpha() or char == '_':
            current_identifier.append(char)
        else:
            if current_identifier:
                identifier = ''.join(current_identifier)
                if identifier not in reserved_words:
                    identifier = identifier.upper()
                result.append(identifier)
                current_identifier = []
            result.append(char)
    
    if current_identifier:
        identifier = ''.join(current_identifier)
        if identifier not in reserved_words:
            identifier = identifier.upper()
        result.append(identifier)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(result))

if __name__ == "__main__":
    input_file = "random_int.py"
    output_file = "random_int_converted.py"
    convert_source_code(input_file, output_file)
    print(f"File conversion completed. Result saved to {output_file}")
