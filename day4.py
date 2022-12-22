with open("day4input.txt", 'r') as f:
    _input = f.readlines()
    
def remove_non_digits(string) -> int:
  return int(''.join([c for c in string if c.isdigit()]))

containing: int = 0
for line in _input:
    pair = line.split(',')
    print(pair)
    pair_one: int = pair[0].split('-')
    pair_two: int = pair[1].split('-')
    
    range_one = range(remove_non_digits(pair_one[0]), remove_non_digits(pair_one[1]))
    range_two = range(remove_non_digits(pair_two[0]), remove_non_digits(pair_two[1]))
    
    if range_one.start >= range_two.start and range_one.stop <= range_two.stop:
        containing += 1
    elif range_two.start >= range_one.start and range_two.stop <= range_one.stop:
        containing += 1
        
print(containing)
