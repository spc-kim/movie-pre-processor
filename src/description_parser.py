# Import the text parsing functions
import text_parsing_functions as tpf

# Function for reading input file and cleaning line by line
def read_and_clean_line_by_line(input_file_path, stopwords_set, name_set, replace_val):
    cleaned_lines = []
    with open(input_file_path, 'r') as input_file_obj:
        for line in input_file_obj:
            cleaned_line = tpf.line_cleaning_pipeline(line, stopwords_set, name_set, replace_val)
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
    return cleaned_lines

# Function for writing cleaned line to output file
def write_cleaned_lines(output_file_path, cleaned_lines):
    with open(output_file_path, 'w') as output_file_obj:
        for line in cleaned_lines:
            output_file_obj.write(line + '\n')

if __name__ == '__main__':

    # Load stopwords from file
    stopwords = tpf.load_stopwords('data/stopwords.txt')

    # Character names that should be replaced with 'person'
    replace = 'person'
    names = set(
        ['suan', 'seongkyeong', 'yonsuk', 'seokwoo',
         'ingil', 'yonghuk', 'jinhee']
    )

    # Test the pipeline with a sample line
    line_text = (
      "pregnant wife Seong-kyeong, "
      "a high school baseball team, "
      "rich-yet-egotistical"
    )
    cleaned_text = tpf.line_cleaning_pipeline(line_text,
                                              stopwords,
                                              names,
                                              replace)

    print(cleaned_text)

    # Set our input and output file paths
    input_file_path = 'data/train_to_busan_description.txt'
    output_file_path = 'parsed/train_to_busan.txt'

    # Call the function that reads and cleans line by line on our input file
    cleaned_line = read_and_clean_line_by_line(input_file_path, stopwords, names, replace)

    # Print cleaned line as preview before we open the file
    for line in cleaned_line:
        print(f"{line}")

    # Write the cleaned line by line to output file
    write_cleaned_lines(output_file_path, cleaned_line)