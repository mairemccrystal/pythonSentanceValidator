import re


def sentence_builder(sentence):
    # strip out parenthesis to check for even number returned
    stripped = re.sub('[^"]', "", sentence)

    # find all the numbers in the sentence
    temp = re.findall(r'\d+', sentence)
    nums = list(map(int, temp))

    # check sentence follows all the rules
    if (sentence[0].isupper() == True) & (sentence.count('.') == 1) \
            & (len(stripped) % 2 == 0) & (sentence[len(sentence) - 1] == '.'):

        success = 0
        for x in nums:
            if x < 13:
                success = success + 1

    else:
        success = 1

    return True if success == 0 else False
