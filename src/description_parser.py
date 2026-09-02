# Import the text parsing functions
import text_parsing_functions as tpf


def clean_line_by_line(file_path, stopwords_set, name_set, replace_val):
    cleaned_lines = []
    with open(file_path, 'r') as file_obj:
        for line in file_obj:
            cleaned_line = tpf.line_cleaning_pipeline(line, stopwords_set, name_set, replace_val)
            if cleaned_line:
                cleaned_lines.append(cleaned_line)
    return cleaned_lines

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

    file_path = 'data/train_to_busan_description.txt'
    cleaned_line = clean_line_by_line(file_path, stopwords, names, replace)
    for line in cleaned_line:
        print(f"{line}")