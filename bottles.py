# Write a program that can print the song "99 Bottles of Beer".

def bottles_song(num):

    while num > 0:

        next_num = num -1

        if num == 1:
            print(f'{num} bottle of beer on the wall, {num} bottle of beer.Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer.'
            'Go to the store and buy some more, 99 bottles of beer on the wall.')
        
        else:
            print(f'{num} bottles of beer on the wall, {num} bottles of beer.Take one down and pass it around, {next_num} bottles of beer on the wall.')
        
        num = next_num
        
bottles_song(99)