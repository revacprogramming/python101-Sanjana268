# Strings
text = 'X-DSPAM-Confidence:    0.8475'
def find_pos(tex): 
    x=tex.find(':')
    y=tex[x+1:]
    z=float(y)
    print(z)

text = "X-DSPAM-Confidence:    0.8475"
pos=find_pos(text)