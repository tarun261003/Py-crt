def check_string(s):
    if s==s[::-1]:
        return -1
    return ''.join(sorted(s))
print(check_string('mam'))