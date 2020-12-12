with open('sha1_hashes.csv', 'r') as read_file, open('sha1_prepared_for_hashcat.csv', 'w') as write_file:
    for password_salt in read_file:
        password, salt = password_salt.split(',')
        salt = salt.replace('\n', '')
        write_file.write(f'{password}:{salt}' + '\n')
