INPUT = input('enter passphrase')

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=/|;:,<.>?'

OUTPUT ='1!2@3#4$5%6^7&8*9(0)-_=+/|azbycxdwevfugthsirjqkplomnABCDEFGHIJKLMNOPQRSTUVWXYZΑΕΗΙΟΥΩ'

out = ''

for char in INPUT:
    for i in range(0, len(OUTPUT)):
        if char == OUTPUT[i]:
            out += CHARS[i]
print(out)
