import pickle
from flask import Flask , render_template , request

app = Flask(__name__)


@app.route('/' , methods=['GET'])
def hello_world():
    
    return render_template('index.html')


 # Python3 program to print a given number in words.
# The program handles till 9 digits numbers and
# can be easily extended to 20 digit number
 
# strings at index 0 is not used, it
# is to make array indexing simple
one = [ "", "one ", "two ", "three ", "four ",
        "five ", "six ", "seven ", "eight ",
        "nine ", "ten ", "eleven ", "twelve ",
        "thirteen ", "fourteen ", "fifteen ",
        "sixteen ", "seventeen ", "eighteen ",
        "nineteen "];
 
# strings at index 0 and 1 are not used,
# they is to make array indexing simple
ten = [ "", "", "twenty ", "thirty ", "forty ",
        "fifty ", "sixty ", "seventy ", "eighty ",
        "ninety "];
 
# n is 1- or 2-digit number
def numToWords(n, s):
 
    str = "";
     
    # if n is more than 19, divide it
    if (n > 19):
        str += ten[n // 10] + one[n % 10];
    else:
        str += one[n];
        # if n is non-zero
    if (n):
        str += s;
 
    return str;
 
# Function to print a given number in words
def convertToWords(n):
 
    # stores word representation of given
    # number n
    out = "";
 
    # handles digits at ten millions and
    # hundred millions places (if any)
    out += numToWords((n // 10000000),
                            "crore ");
 
    # handles digits at hundred thousands
    # and one millions places (if any)
    out += numToWords(((n // 100000) % 100),
                                   "lakh ");
 
    # handles digits at thousands and tens
    # thousands places (if any)
    out += numToWords(((n // 1000) % 100),
                             "thousand ");
 
    # handles digit at hundreds places (if any)
    out += numToWords(((n // 100) % 10),
                      "hundred ");
 
    if (n > 100 and n % 100):
        out += "and ";
 
    # handles digits at ones and tens
    # places (if any)
    out += numToWords((n % 100), "");
 
    return out;
 
# Driver code
 
# long handles upto 9 digit no
# change to unsigned long long
# int to handle more digit number
n = 438237764;
 
# convert given number in words
print(convertToWords(n));

# This code is contributed by mits   

def parse_int(textnum, numwords={}):
    # create our default word-lists
    if not numwords:

      # singles
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      # tens
      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      # larger scales
      scales = ["hundred", "thousand","lakh", "core", "billion", "trillion"]

      # divisors
      numwords["and"] = (1, 0)

      # perform our loops and start the swap
      for idx, word in enumerate(units):    numwords[word] = (1, idx) 
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] =  (10 ** ( idx * 2 + 1 or 2), 0)

    # primary loop
    current = result = 0
    # loop while splitting to break into individual words
    for word in textnum.replace("-"," ").split():
        # if problem then fail-safe
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        # use the index by the multiplier
        scale, increment = numwords[word]
        current = current * scale + increment
        
        # if larger than 100 then push for a round 2
        if scale > 100:
            result += current
            current = 0

    # return the result plus the current
    return result + current  




chaine='one thousand twenty thousand'
chiffre=120000
def correction(chaine,chiffre):
    l='lakh'
    t='thousand'
    c='crore'
    l1=0
    t1=0
    c1=0
    mylist=chaine.split(' ')
    for i in range(len(mylist)):
        if mylist[i]=='lakh':
            l1=l1+1
        if mylist[i]=='thousand':
            t1=t1+1
        if mylist[i]=='crore':
            c1=c1+1
    if(l1>1 or t1>1 or h1>1 or c1>1):
        amount=(convertToWords(chiffre))
        print('the check is not valid : the letter amount is incorrect \n ====> Here is the autocorrection :')
        print('the real amount is : ',amount,chiffre)
        
            
    else:
        if (parse_int(chaine)==chiffre):
            print('the check is valid');
            print('the real amount is :',chiffre,chaine)
                
        else:
            amount=(parse_int(chaine))
            print('the check is not valid : the number amount is incorrect \n ====> Here is the autocorrection :')
            print('the real amount is : ',chaine,amount)
            
                
                
    return('The check is not valid : the number amount is incorrect ,Here is the autocorrection : the real amount is : ',chaine , str(chiffre))



@app.route('/',methods=['GET','POST'])
def predict():
    imagefile= request.files['imagefile']
    image_path =  "./static/" + imagefile.filename
    imagefile.save(image_path)
    v=correction(chaine,chiffre)
    return render_template('index.html',prediction=v)


if __name__ == '__main__':
    app.run(port=3000, debug=True)