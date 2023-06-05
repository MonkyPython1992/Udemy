#Write a Python program that reverses all the words in a string that start with a specific letter for the following :
# 'We all love python'( 'l' in love)
x='We all love python'
def reverse_sp_word(st, l):
    st = st.split()
    return ' '.join(word[::-1] if word.startswith('l') else word for word in st)

print(reverse_sp_word(x,"l"))