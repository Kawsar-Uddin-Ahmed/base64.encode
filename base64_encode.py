import base64

c = []
with open("password.txt") as f:
       data = f.read()
       lines = data.splitlines()
       print(lines)
       for i in range(0,len(lines)):
           # print(lines[i])
           sample_string_bytes = lines[i].encode("ascii")
           b64_bytes = base64.b64encode(sample_string_bytes)
           b64_strings = b64_bytes.decode("ascii")
           #print(b64_strings)
           c.append(b64_strings)
           with open("base64_password1.txt", "w") as fi:
               print(('\n'.join(str(j) for j in c)),file=fi)











