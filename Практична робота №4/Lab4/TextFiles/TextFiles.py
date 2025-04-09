def add_funny_text_to_lines():
    with open('output_file', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    modified_lines = [line.strip() + ' Бум-бум-кабум!\n' for line in lines]

    with open('output_file', 'w', encoding='utf-8') as outfile:
        outfile.writelines(modified_lines)

def remove_python_comments():

    with open('input_file', 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    no_comment_lines = []
    for line in lines:
        if '#' in line:
            index = line.find('#')
            no_comment_lines.append(line[:index].rstrip() + '\n')
        else:
            no_comment_lines.append(line)

    with open('output_file', 'w', encoding='utf-8') as outfile:
        outfile.writelines(no_comment_lines)

remove_python_comments()
add_funny_text_to_lines()