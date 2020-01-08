def is_palindrome_v1(s):
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
    return reverse(s) == s


def reverse(s):
    """ (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """
    rev = ''
    # For each character in s,  add that char to the beginning of rev.
    for ch in s:
        rev = ch + rev
    return rev
