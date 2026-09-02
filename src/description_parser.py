# Get our text parsing functions from other file and set keyword
import text_parsing_functions as tpf

if __name__ == '__main__':

    # Set test arguments
    stopwords = tpf.load_stopwords('data/stopwords.txt')
    name_set = set(['seokwoo', 'suan', 'seongkyeong', 'busan'])
    replace_val = 'person'

    # Open the example description file
    with open('data/train_to_busan_description.txt', 'r') as file_obj:
        sample_text = file_obj.read()

    # Run our pipeline and print it
    cleaned_text = tpf.line_cleaning_pipeline(sample_text, stopwords, name_set, replace_val)
    print(cleaned_text)