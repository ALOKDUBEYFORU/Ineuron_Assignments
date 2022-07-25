import logging
logging.basicConfig(filename='Assignment_23.log' ,level=logging.INFO,
                    format='%(filename)s %(asctime)s %(levelname)s %(message)s')
logging.info('starting of logging')
def is_symmetrical(num1):
    '''
    This function that takes a number as an argument and returns True or False depending on whether the number is
    symmetrical or not. A number is symmetrical when it is the same as its reverse.
    :param num1:
    :return:
    '''
    try:
        logging.info('Beginning of the execution of is_symmetrical function, being passed "%s"',num1)
        str1 = str(num1)
        str2 = str1[::-1]
        return str1 == str2
    except Exception as e:
        logging.error("error occured in is_symmetrical function ",e)
    finally:
        logging.info("End of execution of is_symmetrical function")

try:

    is_bool1 = is_symmetrical(7227)
    logging.info('is_symmetrical(7227) returns %s',is_bool1)
    is_bool1 = is_symmetrical(12567)
    logging.info('is_symmetrical(12567) returns %s',is_bool1 )
    is_bool1 = is_symmetrical(44444444)
    logging.info('is_symmetrical(44444444) returns %s', is_bool1)
    is_bool1 = is_symmetrical(9939)
    logging.info('is_symmetrical(9939) returns %s', is_bool1)
    is_bool1 = is_symmetrical(1112111)
    logging.info('is_symmetrical(1112111) returns %s', is_bool1)
except Exception as e:
    logging.error('Error occured in calling the is_bool1 function ',e)
finally:
    logging.info("completion of calling of is_bool1 function")

def multiply_nums(str1):
    '''
    This function takes a string of numbers separated by a comma and space, return the product of the numbers.
    :param str1:
    :return:
    '''
    try:
        logging.info("Starting of the execution of multiply_nums method. This is called using %s",str1)
        list1 = []
        substr1 = ""
        for i in str1:
            if i not in (',',' '):
                substr1 = substr1+i
            elif i == ',':
                list1.append(int(substr1))
            elif i == " ":
                substr1 = ""
        list1.append(int(substr1))
        mult = 1
        for i in list1:
            mult = mult*i
        return mult
    except Exception as e:
        logging.error("Error occured in multiply_nums method ",e)
    finally:
        logging.info("Execution of multiply_nums method completed.")

try:
    logging.info('calling multiply_nums with the value %s',"2, 3")
    num1 = multiply_nums("2, 3")
    logging.info("result is %s",num1)
    logging.info('calling multiply_nums with the value %s', "1, 2, 3, 4")
    num1 = multiply_nums("1, 2, 3, 4")
    logging.info("result is %s",num1)
    logging.info('calling multiply_nums with the value %s', "54, 75, 453, 0")
    num1 = multiply_nums("54, 75, 453, 0")
    logging.info("result is %s", num1)
    logging.info('calling multiply_nums with the value %s', "10, -2")
    num1 = multiply_nums("10, -2")
    logging.info("result is %s",num1)
except Exception as e:
    logging.error("Erroc occured in calling multiply_nums method ",e)
finally:
    logging.info("calling of multiply_nums method had been completed")

def square_digits(num1):
    '''
    This function squares every digit of a number
    :param num1:
    :return:
    '''
    try:
        logging.info('starting of the execution of square_digits function with parameter %s',num1)
        str1 = str(num1)
        str2 = ""
        for i in str1:
            str2 = str2+str(int(i)*int(i))
        return int(str2)
    except Exception as e:
        logging.error("Error occured in square_digits ",e)
    finally:
        logging.info("execution of square_digits function completed")

try:
    logging.info("calling square_digits method using the value %s",9119)
    num1 = square_digits(9119)
    logging.info('result is %s',num1)
    logging.info("calling square_digits method using the value %s", 2483)
    num1 = square_digits(2483)
    logging.info('result is %s',num1)
    logging.info("calling square_digits method using the value %s", 3212)
    num1 = square_digits(3212)
    logging.info('result is %s',num1)
except Exception as e:
    logging.error("Error occured in calling the square_digits method ",e)
finally:
    logging.info("calling of square_digits method completed")

def setify(list1):
    '''
    This function sorts a list and removes all duplicate items from it.
    :param list1:
    :return:
    '''
    try:
        logging.info("Beginning of the execution of setify method with the list %s",list1)
        set1 = set(list1)
        list2 = list(set1)
        list2.sort()
        return list2
    except Exception as e:
        logging.error("Error occured in executing the setify method ",e)
    finally:
        logging.info("execution of setify method is completed")

try:
    logging.info('passing the list [%s] to setify method',[1, 3, 3, 5, 5])
    result1 = setify([1, 3, 3, 5, 5])
    logging.info("result is %s",result1)
    logging.info('passing the list [%s] to setify method',[4, 4, 4, 4])
    result1 = setify([4, 4, 4, 4])
    logging.info("result is %s", result1)
    logging.info('passing the list [%s] to setify method', [5, 7, 8, 9, 10, 15])
    result1 = setify([5, 7, 8, 9, 10, 15])
    logging.info("result is %s", result1)
    logging.info('passing the list [%s] to setify method', [3, 3, 3, 2, 1])
    result1 = setify([3, 3, 3, 2, 1])
    logging.info("result is %s",result1)
except Exception as e:
    logging.error("Error occured in calling setify method ",e)
finally:
    logging.info('execution of setify method completed')

def mean(num1):
    '''
    This function that returns the mean of all digits.
    :param num1:
    :return:
    '''
    try:
        str1 = str(num1)
        num2 = 0
        for i in str1:
            num2 = num2+int(i)
        return num2 / len(str1)
    except Exception as e:
        logging.error("Error occured in mean function ",e)
    finally:
        logging.info("execution of mean function completed")

try:
    logging.info('passing %s to mean function',42)
    result = mean(42)
    logging.info('result is %s',result)
    logging.info('passing %s to mean function', 12345)
    result = mean(12345)
    logging.info('result is %s', result)
    logging.info('passing %s to mean function', 666)
    mean(666)
    logging.info('result is %s',result)
except Exception as e:
    logging.error("error occured in calling mean function ",e)
finally:
    logging.info("calling of mean function had completed")
