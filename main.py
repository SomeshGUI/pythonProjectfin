from difflib import SequenceMatcher

def longest_Substring(s1, s2):

    seq_match = SequenceMatcher(None, s1, s2)

    match = seq_match.find_longest_match(0, len(s1), 0, len(s2))

# returns the longest substring
    if (match.size != 0):
        return (s1[match.a: match.a + match.size])
    else:
        return ('Longest common sub-string not found')

s1 = 'mnopqrst'
s2 = 'sfsdvopqrst'
print("Original Substrings:\n", s1 + "\n", s2)
print("\nLongest common sub_string:")
print(longest_Substring(s1, s2))