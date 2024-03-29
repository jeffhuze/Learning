text = "X-DSPAM-Confidence:    0.8475"
position1 = text.find('0')
# print(position1)
newText = text[position1:9999]
fNewText = float(newText)
print(fNewText)
