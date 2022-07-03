# Defining isogram encode code wiht defalut values of inputs
def isogram_encode(input=0, key=0):

    while True:
        try:

            # Checking if our inputs aren't empty
            if input == None:
                raise ValueError
                if key == None:
                    raise ValueError

            # Making sure that inputs and key are an string and key is all UPPER
            key = str(key)
            key = key.upper()
            input = str(input)

            # Checking if Input can be intiger 
            input = int(input)

            # Prepering lists that we will work on
            input = str(input)
            list1 = [x for x in key]
            list2 = [x for x in input]
            list3 = []

            # Checking if elements in list1 aren't the same
            b = len(list1)
            for i in range(b):
                for j in range(i + 1, b):
                    if list1[i] == list1[j]:
                        raise ValueError

            # Creating list3 with corresponding letters to numbers
            # Checking if Key length is 10
            if( len(key) == 10):

                # Assigning corresponding letters to numbers and adding them to the empty listy
                for x in list2:
                    if x != 0:
                       list3.append(list1[int(x)-1]) 
                    else:
                       list3.append(list1[9])
            else:
                raise ValueError

            # creating string from list
            c = ''.join(list3)
            return c

        # Returning Error msg
        except:
            c = 'Incorrect key or input!'
            return c
            break

# Defining isogram decode code with defalut values of inputs
def isogram_decode(input=0, key=0):

    while True:
        try:
            # Checking if our inputs aren't empty
            if input == None:
                raise ValueError
                if key == None:
                    raise ValueError

            # Making sure that inputs and kay are an string and key is all UPPER
            key = str(key)
            key = key.upper()
            input = str(input)
            input = input.upper()

            # Prepering lists that we will work on
            list1 = [x for x in key]
            list2 = [x for x in input]
            list3 = []

            # Checking if elements in list1 aren't the same
            b = len(list1)
            for i in range(b):
                for j in range(i + 1, b):
                    if list1[i] == list1[j]:
                        raise ValueError

            # Creating list3 with corresponding letters to numbers
            # Checking if Key length is 10
            if( len(key) == 10):
                # Assigning corresponding letters to numbers and adding them to the empty listy
                o = len(list2)
                for x in range(o):
                    for y in range(b):
                        if list2[x] == list1[y]:
                            y = y+1
                            if y == 10:
                                y = 0
                                list3.append(str(y))
                            else:
                                list3.append(str(y))

            else:
                raise ValueError

            # Checking if our new list isn't empty
            if len(list3) < len(list2):
                raise ValueError 
            
            if list3[0] == 0:
                raise ValueError

            # Creating string from list
            c = ''.join(list3)
            c = int(c)
            c = str(c)
            return c

        # Returning Error msg
        except:
            c = 'Incorrect key or input!'
            return c
            break