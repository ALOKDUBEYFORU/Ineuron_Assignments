import logging
logging.basicConfig(filename = "Assignment_25.log",level=logging.INFO,
                    format='%(filename)s %(asctime)s %(levelname)s %(message)s')
logging.info("defining the function1")


def equal(a,b,c):
    '''
    Create a function that takes three integer arguments (a, b, c) and returns the amount of
    integers which are of equal value.
    :param a:
    :param b:
    :param c:
    :return:
    '''
    logging.info("initiating the function")
    try :
        logging.info("Initiating a variable var1 to zero")
        var1 = 1
        logging.info('checking whether if %s == %s',a,b)
        if a==b:
            logging.info("incrementing the %s by one",var1)
            var1 = var1+1
        logging.info('checking whether if %s == %s',a,c)
        if a==c:
            logging.info("incrementing the %s by one", var1)
            var1 = var1+1
        logging.info('checking whether if %s == %s', b, c)
        if b==c:
            logging.info("incrementing the %s by one", var1)
            var1 = var1 + 1
        logging.info('returning the value %s',var1)
        if var1 == 1 :
            return 0
        else:
            return var1
    except Exception as e:
        logging.error("exception raised ")
    finally:
        logging.info("End of the execution of function1")

logging.info("End of the function1")

logging.info("starting of the main program")
try:
    logging.info('running 3, 4, 3 values to equal function')
    logging.info('equal(3, 4, 3) returns %s',equal(3, 4, 3))
    logging.info('running 1, 1, 1 values to equal function')
    logging.info('equal(1, 1, 1) returns %s',equal(3, 4, 3))
    logging.info('running 3, 4, 1 values to equal function')
    logging.info('equal(3, 4, 1) returns %s',equal(3, 4, 1))
except Exception as e:
    logging.error("Error occured in the running the main program",e)
finally:
    logging.info('Completion of main program')

def dict_to_list(dict1):
    logging.info("Beginning of the dict_to_list function")
    try:
        logging.info("creating an empty list")
        list2 = []
        logging.info("starting of the for loop")
        for i in dict1.items():
            logging.info("adding %s",i)
            list2 = list2 + [i]
        logging.info('returning list2 : %s',list2)
        return list2
    except Exception as e:
        logging.error("error occured in the dict to list function", e)
    finally:
        logging.info("function execution had completed")
logging.info("End of the definition of dict to list function")
logging.info("beginning of the main function of dict to list")
dict1 = {"likes": 2, "dislikes": 3, "followers": 10}
logging.info("beginning of the main function of dict to list")
list1 = dict_to_list(dict1)
logging.info('list1 returned is %s',list1)

logging.info("starting of the function definition mapping")
def mapping(list1):
    '''
    Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
    :param list1:
    :return:
    '''
    logging.info("Beginning of the execution of mapping")
    try:
        logging.info("creating an empty dictionary")
        dict1 = {}
        logging.info('looping through %s',list1)
        for i in list1 :
            logging.info('assigning the value %s to dict1[%s]',i.lower(),i.upper())
            dict1[i.lower()] = i.upper()
        logging.info('returning the dictionary %s',dict1)
        return dict1
    except Exception as e:
        logging.error("error occured in running the mapping function",e)
    finally:
        logging.info("Execution of mapping function completed")

logging.info("running the main function of mapping function")
logging.info(mapping(["p", "s"]))
logging.info(mapping(["a", "b", "c"]) )
logging.info(mapping(["a", "v", "y", "z"]))

logging.info("starting of the vow_replace function definition")
def vow_replace(string1,string2):
    '''
    Write a function, that replaces all vowels in a string with a specified vowel.
    Examples
    vow_replace("apples and bananas", "u") ➞ "upplus und bununus"

    vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"

    vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"

    :param string1: The string which needs to be transformed
    :param string2:The string that will be replacing the vowels in param string1
    :return: transformed string
    '''
    logging.info('starting of the execution of vow_replace function')
    try:
        logging.info("replacing the character 'a' with %s in %s",string2,string1)
        string1 = string1.replace('a',string2)
        logging.info("replacing the character 'e' with %s in %s", string2,string1)
        string1 = string1.replace('e',string2)
        logging.info("replacing the character 'i' with %s in %s", string2,string1)
        string1 = string1.replace('i', string2)
        logging.info("replacing the character 'o' with %s in %s", string2,string1)
        string1 = string1.replace('o', string2)
        logging.info("replacing the character 'u' with %s in %s", string2,string1)
        string1 = string1.replace('u', string2)
        logging.info('returning %s',string1)
        return string1
    except Exception as e:
        logging.error("Error occured in execution of vow_replace function ",e)
    finally:
        logging.info("Completion of execution of vow_replace function")

logging.info("end of the vow_replace function definition")

try :

    logging.info("execution of the main function calling vow_replace function")
    logging.info('passing the values "apples and bananas" and "u" to the vow_replace function')
    result1 = vow_replace("apples and bananas", "u")
    logging.info("recieved '%s' from vow_replace function",result1)
    logging.info('passing the values "apples and bananas" and "u" to the vow_replace function')
    logging.info('passing the values "cheese casserole" and "o" to the vow_replace function')
    result2 = vow_replace("cheese casserole", "o")
    logging.info("recieved '%s' from vow_replace function",result2)
    logging.info('passing the values "stuffed jalapeno poppers" and "e" to the vow_replace function')
    result3 =vow_replace("stuffed jalapeno poppers", "e")
    logging.info("recieved '%s' from vow_replace function",result3)
except Exception as e:
    logging.error("Error occured in the execution of main function calling vow_replace ",e)
finally:
    logging.info("completion of execution of main function")

logging.info('start of asc__capitalize function definition')
def ascii_capitalize(string1):
    '''
    Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
    Examples
    ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"

    ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"

    ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."

    :param string1:
    :return:
    '''
    try:
        logging.info('beginning of the execution of ascii_capitalize function')
        logging.info("initializing an empty string variable 'a'")
        a=''
        logging.info('starting of for loop')
        for i in string1:
            logging.info('finding the ascii value and the reminder of dividing the same with 2 and check whether the remainder is equal to 1')
            if ord(i) %2 == 1:
                logging.info('if the remainder equals to one, convert the value "%s" into lower case and append it to "%s"',i,a)
                a = a+i.lower()
            else:
                logging.info(
                    'if the remainder equals to one, convert the value "%s" into upper case and append it to "%s"', i,
                    a)
                a = a+i.upper()
        logging.info('returning the value "%s"',a)
        return a
    except Exception as e:
        logging.error("Error occured in execution of ascii_capitalize function ",e)
    finally:
        logging.info("execution of ascii_capitalize function got completed")

logging.info('end of asc__capitalize function definition')

try:
    logging.info('starting of the execution of main function calling acii_capitalize function')
    logging.info('passing the value "to be or not to be!" to ascii_capitalize function')
    var1 = ascii_capitalize("to be or not to be!")
    logging.info('result obtained is %s',var1)

    logging.info('passing the value "THE LITTLE MERMAID" to ascii_capitalize function')
    var2 = ascii_capitalize("THE LITTLE MERMAID")
    logging.info('result obtained is %s',var2)

    logging.info('passing the value "Oh what a beautiful morning." to ascii_capitalize function')
    var3 = ascii_capitalize("Oh what a beautiful morning.")
    logging.info('result obtained is %s', var3)
except Exception as e:
    logging.error("Error occured in the execution of calling ascii_capitalize function ",e)
finally:
    logging.info('execution of main function calling ascii_capitalize function completed')