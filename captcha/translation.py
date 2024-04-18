# coding:utf-8
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "Helsinki-NLP/opus-mt-en-zh"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
translation = pipeline("translation", model=model, tokenizer=tokenizer)


def translate_text(text, max_length=10240):
    result = translation(text, max_length=max_length)[0]
    return result['translation_text']

text = """Please Click the letter nearest from number '3'.
Please click on green letter
Please click in order:  2 7 3 4 1
Please click on blue letter
Please click in order:  e G K
Please Click the letter nearest from number '3'.
Please click in order:  2 7 5
Please click on all duplicate numbers
Please click in order:  a R B
Please click on all numbers that rotate 90 ° to the right
Please Click the letter nearest from number '7'.
Please click in order:  1 2 5 4 3
Please click in order:  G Y a R
Please click on all letters rotated 180 °
Please click on all numbers rotated 180 °
Please click on red letter
Please Click the number nearest from letter 'S'.
Please click on all numbers that rotate 90 ° to the right
Please click on all letters rotated 180 °
Please click on all numbers rotated 180 °
Please Click the letter nearest from number '3'.
Please click on all letters rotated 180 °
Please click on all duplicate letters
Please click on all duplicate letters
Please click on all duplicate numbers
Please click in order:  E J a Q
Please click in order:  1 5 3 4 2
Please click on all duplicate numbers
Please click on all duplicate numbers
Please click on all letters without rotation
Please click on all duplicate letters
Please click on all tilted numbers
Please click in order:  1 2 3 4 5
Please click in order:  J P h
Please click on yellow number
Please click in order:  C W Q h g
Please click in order:  2 7 4
Please click in order:  T N E
Please click on all tilted numbers
Please Click the letter nearest from number '7'.
Please Click the letter nearest from number '2'.
Please Click the number nearest from letter 'A'.
Please click on all duplicate letters
Please click on green letter
Please Click the letter nearest from number '2'.
Please Click the letter nearest from number '3'.
Please click on yellow number
Please Click the letter nearest from number '4'.
Please Click the letter nearest from number '2'.
Please Click the number nearest from letter 'K'.
Please Click the number nearest from letter 'Y'.
Please Click the letter nearest from number '3'.
Please click on all numbers that rotate 90 ° to the left
Please click in order:  V E B
Please click on all duplicate letters
Please click on all duplicate letters
Please Click the letter nearest from number '7'.
Please click on all numbers that rotate 90 ° to the right
Please click on all duplicate letters
Please click on all duplicate letters
Please Click the letter nearest from number '2'.
Please click on all duplicate numbers
Please click on green letter
Please Click the letter nearest from number '3'.
Please click on all letters that rotate 90 ° to the right
Please click on all duplicate letters
Please click on red letter
Please click in order:  5 2 4
Please click on yellow letter
Please click in order:  4 3 2 1
Please Click the number nearest from letter 'h'.
Please click on all duplicate letters
Please click on blue letter
Please click on all duplicate letters
Please click on all letters that rotate 90 ° to the right
Please click on all numbers that rotate 90 ° to the right
Please click on all duplicate letters
Please click on green number
Please click on red letter
Please click on all duplicate letters
Please click on yellow letter
Please click on all duplicate letters
Please click in order:  4 7 1 2
Please click on all letters that rotate 90 ° to the right
Please click on all letters that rotate 90 ° to the left
Please click in order:  7 4 2 1
Please Click the letter nearest from number '4'.
Please click on red letter
Please click in order:  1 3 7 5
Please click in order:  Q E j h
Please click on green letter
Please click in order:  A W m
Please click in order:  V a e f
Please click on all duplicate letters
Please Click the number nearest from letter 'g'.
Please click on red number
Please click on all numbers rotated 180 °
Please click in order:  A G Q F
Please Click the letter nearest from number '2'.
Please click in order:  4 2 3
Please click on blue letter
Please Click the letter nearest from number '3'.
Please click on all letters rotated 180 °
Please click on all duplicate numbers
Please Click the number nearest from letter 'm'.
Please click on yellow letter
Please Click the letter nearest from number '5'.
Please click on all duplicate letters
Please click on all duplicate letters
Please click on all tilted letters
Please click on green letter
Please click on blue number
Please click on all duplicate numbers
Please Click the number nearest from letter 'j'.
Please click on yellow letter
Please click on all duplicate letters
Please click on all duplicate numbers
Please click on yellow number
Please click on all tilted letters
Please click on all letters rotated 180 °
Please click on all duplicate letters
Please click on yellow number
Please click on green number
Please click in order:  a S T B W
Please click in order:  3 5 2
Please click on all duplicate letters
Please click on blue letter
Please click on all duplicate letters
Please click in order:  3 4 2 5
Please click in order:  e G t F
Please click on green letter
Please click on all duplicate numbers
Please Click the letter nearest from number '7'.
Please click in order:  1 5 3 2
Please click on all numbers that rotate 90 ° to the left
Please click on all duplicate letters
Please click on all duplicate letters
Please Click the letter nearest from number '1'.
Please click in order:  5 3 2 4 7
Please Click the letter nearest from number '2'.
Please click in order:  2 1 7 4 5
Please click in order:  J V N K
Please click on red number
Please click on all duplicate letters
Please click on red letter
Please click on all duplicate letters
Please click on blue letter
Please click on all duplicate letters
Please click on all duplicate numbers
Please Click the number nearest from letter 'C'.
Please click on all duplicate letters
Please Click the number nearest from letter 'Q'.
Please Click the letter nearest from number '1'.
Please click on all numbers rotated 180 °
Please Click the number nearest from letter 'e'.
Please click in order:  5 7 3 1 2"""

for t in text.split('\n'):

    result = translate_text(t, max_length=10240)
    print(result)