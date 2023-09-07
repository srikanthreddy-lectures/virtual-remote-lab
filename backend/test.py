import re

regex = r"\[90m|\[32m|\[1m|\[0m|[\\]\w+"


ansi_escape = re.compile(regex, flags=re.IGNORECASE)


res1=''
target=[]

with open('message.txt') as searchfile:
    for line in searchfile:
        left,sep,right = line.partition('aws_instance.web: Creation complete')
        if sep: # True iff 'Output' in line
            res1=right[:500]
            aa1=ansi_escape.sub(' ', res1)
            ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', aa1 )
            target.append(ip)
            #print(aa2)
            for word in set(aa1.split(" ")):
                #indexes = [w.start() for w in re.finditer(word, aa)]
                match = re.search(r"\[(.+?)\]", word)
                if match:
                    target.append(match.group(1))
            

print(target)
                


#f = open('message.txt')
# Read the contents of the file into a variable
#message = f.read()
#result = ansi_escape.sub('', message)
#print(result)
# Don't forget to close the file again
#f.close()


#start_index = message.find("Outputs:")
#end_index = start_index + len(message)
#res=message[start_index:start_index+27]
#print("-->"+result)