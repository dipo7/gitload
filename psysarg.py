import sys

for arg in range(1, len(sys.argv)):
    # print(sys.argv[arg])
    # rev_s = s[::-1]
    print("You get '{}' for '{}' using slicing.".format(sys.argv[arg][::-1], sys.argv[arg]))
    # print("You get '{}' for '{} 'using reversed.".format(''.join(reversed(sys.argv[1])), sys.argv[1]))


