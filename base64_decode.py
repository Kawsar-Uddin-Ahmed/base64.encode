import base64

c = []
with open("base64_password.txt") as f:
       data = f.read()
       lines = data.splitlines()
       print(lines)
       for i in range(0,len(lines)):
           # print(lines[i])
           base64_string = lines[i].encode("ascii")
           sample_bytes = base64.b64decode(base64_string)
           sample_strings = sample_bytes.decode("ascii")
           #print(b64_strings)
           c.append(sample_strings)
           with open("Base64_decode_password.txt", "w") as fi:
               print(('\n'.join(str(j) for j in c)),file=fi)











