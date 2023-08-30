# Mode of file opening
# For Read mode, we can mention 'r'
# For Write Mode, we can mention 'w'

# Scenario is Read Data from file and reverse it and then write back to file

with open('test.txt','r') as reader:
    content=reader.readlines()
    reversed(content)
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)


