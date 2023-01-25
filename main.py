import os
import re

def extract_text_from_vtt(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
    # Extract the text using regular expressions
    text = re.findall(r'00:.*\n(.*)\n(.*)', data)
    # Convert the tuples to plain text
    plain_text = []
    for tup in text:
        plain_text.append(" ".join(tup))
    # join the plain_text list
    plain_text = " ".join(plain_text)
    # replace double spaces with single space
    plain_text = plain_text.replace("  ", " ")
    # Extract the file name without the extension
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    # Create the output file path
    output_file = os.path.join(output_dir, file_name + '.txt')
    # Write the output to the file
    with open(output_file, 'w') as file:
        file.write(plain_text)
    return "Extracted Text from {} has been saved in {}".format(file_path,output_file)


input_dir = os.path.join(os.path.expanduser("~"), "Desktop", "vtt_folder")
output_dir =os.path.join(os.path.expanduser("~"), "Desktop", "result_txt_folder")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file_name in os.listdir(input_dir):
    if file_name.endswith('.vtt'):
        file_path = os.path.join(input_dir, file_name)
        print(extract_text_from_vtt(file_path))
