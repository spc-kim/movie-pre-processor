# Import the text parsing functions
import text_parsing_functions as tpf


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