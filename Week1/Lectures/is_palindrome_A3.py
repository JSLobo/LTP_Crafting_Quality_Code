def is_palindrome_v3(s):
    """" (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False

    Reading_1: https://d3c33hcgiwev3.cloudfront.net/_380a7150ad2742acae88b12383e465ca_palindrome_intro.html?Expires=1577923200&Signature=KZhGdxWFb9VUlWJR45DTg1r2NYxYjmCjQFP75tN4DfNfD1te-I8SCh2MN5YkQWYV8-oKLS~BQ0FWTg50BkzIkCJ8Mc9rYzDaF4vOT6N6lTCgCTNjgnUOpFWnPJQbzlXn5YpmiqnXrKMZhsV9lr-XhELdV6HT65dIN2Pm4w1MqTs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A

    """
    # s[i] and s[j] are the next pair of characters to compare.
    i = 0
    j = len(s) - 1

    # The characters in s[:i] have been successfully compared to those in s[j:].
    while i < j and s[i] == s[j]:
        i = i + 1
        j = j - 1

    # If we exited because we successfully compared all pairs of characters,
    # then j <= i
    return j <= i