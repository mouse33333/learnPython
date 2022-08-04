s1 = "Do you love Canglaoshi? Canglaoshi is a good teacher."
s2 = s1.split(" ")
for i, s3 in enumerate(s2):
    if "Canglaoshi" in s3:
        s2[i] = "PHP"

print s2
