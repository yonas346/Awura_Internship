def ask_ok(prompt, retries=4,reminder='please try again!' ):
    while True:
        rely = input(prompt)
        if rely in {'y','ye','yes'}:
            return True
        if rely in {'n','no','nop','nope'}:
            return False
        reties = reties -1
        if reties < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('queen')