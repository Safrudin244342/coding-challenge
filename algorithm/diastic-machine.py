
seed = "seed"

pharagraph = """Mr Emory Barr
Abbey National PLC
Bromley Rd Branch
London
BW1 3AN
Dear Friend,
I am Mr.Emory Barr, Accounts Manager, of Abbey National PLC
Bromley Rd Branch. I have an important business proposition for you.
On December 12th, 2001, a German contractor with the British
Pertroleum co-orporation, United Kingdom ,Mr. Olaf Partetzke made a
numbered time (Fixed) Deposit for twelve calendar months, valued at
US$ 17,350,000.00 (Seventeen Million Three Hundred Hundred and fifty
Thousand Dollars only) in my branch.
Upon maturity,I sent a routine notification to his forwarding address
but got no reply. After a month, we sent a reminder and finally we
discovered from his contract employers, the British Pertroleum
co-orporation that Mr.Olaf Partetzke died from an Automobile accident
further investigation,
I found out that he died without making a WILL,and all attempts to
trace his next of kin was fruitless.
I therefore made further investigation and discovered that Mr. Olaf
Partetzke did not declare any kin or relations in
all his official documents, including his Bank Deposit paperwork in my
Bank. This sum of US$ 17,350,000.00 is still sitting in my Bank and
the interest is being rolled over with the principal sum at the end of
each year. No one will ever come forward to claim it. According to
inheritance Laws of the United Kingdom, at the expiration of 5 (five)
years, the money will revert to the ownership of the Local Government
Authorities here in Wales, United Kingdom, if nobody applies to claim
the fund.
Consequently, my proposal is that I will like you to stand in as the
next of kin to Mr. Olaf Partetzke
so that the fruits of this old man's labor will not get into the hands
of some corrupt government officials.This is simple, I will like you
to provide immediately your full names and address so that the
attorney will prepare the necessary documents and affidavits that will
put you in place as the next of kin. We shall employ the services of
an attorney for drafting and notarization of the WILL and to obtain
the necessary documents and letter of probate/administration in your
favor for the transfer. The money will be paid into your account for
us to share in the ratio of 60% for me and 35% for you and 5% for
Expenses Incurred in the course of the transaction .
There is no risk at all as all the paperwork for this transaction will
be done by the attorney and with my position as the Manager with my
bank will guarantees the successful execution of this transaction. If
you are interested, please reply immediately to my private email
box : emory400@xasamail.com
Upon your response, I shall then provide you with more details and
relevant documents that will help you understand the transaction. You
should observe utmost confidentiality, and rest assured that this
transaction would be most profitable for both of us because I shall
require your assistance to invest my share in your country.
Awaiting your urgent reply.
Thanks and regards.
Emory Barr"""

# algoritma
words = pharagraph.split()
sentence = ""
lastIndex = 0
for n, ch in enumerate(seed):
   for index, word in enumerate(words[lastIndex:]):
       if n < len(word) and word[n] == ch:
           sentence += word
           sentence += " "
           lastIndex = index + 1
           break
print (sentence)
