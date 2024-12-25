def look_and_say(n):
    if n <= 0:
        return []
    
    my_sequence = ['1']
    
    for _ in range(n - 1):
        old_term = my_sequence[-1]
        new_term = ''
        count = 1
        current_number = old_term[0]
        
        for i in range(1, len(old_term)):
            if old_term[i] == current_number:
                count += 1
            else:
                new_term += str(count) + current_number
                count = 1
                current_number = old_term[i]
        new_term += str(count) + current_number
        my_sequence.append(new_term)
    
    return my_sequence  


for i, term in enumerate(look_and_say(6), 1):
    print(f"Term {i}: {term}")