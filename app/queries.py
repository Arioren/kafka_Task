from app.repository.all_messages import get_person_by_email, get_most_common_word_by_email


#How can the full content of an object be extracted
# according to a certain email including suspicious content?
def full_content(email: str):
    res = get_person_by_email(email)
    return res


# How can you get the most common word in the suspicious messages by email?
def most_common_word(email: str):
    res = get_most_common_word_by_email(email)
    return res


print(most_common_word('kevinhall@example.net'))