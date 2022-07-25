import logging
logging.basicConfig(filename='Assignment_24.log',level=logging.INFO,
                    format='%(filename)s %(asctime)s %(levelname)s %(message)s')
logging.info("beginning of the amplify function")
def amplify(number1):
    '''
    Create a function that takes an integer and returns a list from 1 to the given number, where:
    1.	If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
    2.	If the number cannot be divided evenly by 4, simply return the number.
    Examples
    amplify(4) ➞ [1, 2, 3, 40]

    amplify(3) ➞ [1, 2, 3]

    amplify(25) ➞ [1, 2, 3, 40, 5, 6, 7, 80, 9, 10, 11, 120, 13, 14, 15, 160, 17, 18, 19, 200, 21, 22, 23, 240, 25]
    Notes
    •	The given integer will always be equal to or greater than 1.
    •	Include the number (see example above).
    •	To perform this problem with its intended purpose, try doing it with list comprehensions. If that's too difficult, just solve the challenge any way you can.

    :param number1:
    :return:
    '''
    try:
        logging.info("creating list comprehension to generate from 1 to %s",number1)
        list1 = [x for x in range(1,number1+1)]
        logging.info("creating an empty list list2")
        list2 = []
        logging.info('start of the for loop')
        for i in list1:
            logging.info('To check whether the number when divided by 4 leaves zero as reminder')
            if i%4 ==0:
                list2.append(i*10)
            else:
                list2.append(i)
        logging.info('returning the list2 "%s"',list2)
        return list2
    except Exception as e:
        logging.error("Error occured in function amplify ",e)
    finally:
        logging.info("execution of amplify function had been completed")

try:
    logging.info('Calling the main function for amplify')
    logging.info('calling amplify function with a value "%s"',25)
    list1 = amplify(25)
    logging.info("amplify function had returned the value '%s'",list1)
except Exception as e:
    logging.error("Exception raised in calling the amplify function")
finally:
    logging.info("Completion of the execution of the main function of amplify")

logging.info("starting of the definition of unique function")
def unique(list1):
    '''
    Create a function that takes a list of numbers and return the number that's unique.
    Examples
    unique([3, 3, 3, 7, 3, 3]) ➞ 7

    unique([0, 0, 0.77, 0, 0]) ➞ 0.77

    unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0
    Notes
    Test cases will always have exactly one unique number while all others are the same.
    :param list1
    :return:
    '''
    try:
        logging.info('starting of the execution of unique function')
        logging.info('creating a set to list out the unique values from the list %s',list1)
        set1 = set(list1)
        logging.info('Set "%s" had been created. starting the loop in the set1 values',set1)
        for i in set1:
            logging.info('checking the count of occurance of the set value in list1. if it equal to one, then return the value. otherwise continue the loop')
            if list1.count(i) == 1 :
                return i
    except Exception as e:
        logging.error("Error occured in the execution of unique function ",e)
    finally:
        logging.info("End of the execution of the unique function")

logging.info("Ending of the definition of unique function")

try :
    logging.info('calling unique function [3, 3, 3, 7, 3, 3]')
    value1 = unique([3, 3, 3, 7, 3, 3])
    logging.info('returned the value %s',value1)
    logging.info('calling unique function [0, 0, 0.77, 0, 0]')
    value1 = unique([0, 0, 0.77, 0, 0])
    logging.info('returned the value %s', value1)
    logging.info('calling unique function [0, 1, 1, 1, 1, 1, 1, 1]')
    unique([0, 1, 1, 1, 1, 1, 1, 1])
    logging.info('returned the value %s', value1)
except Exception as e:
    logging.error("Error occured in calling the unique function ",e)
finally:
    logging.info("completion of main function calling the unique function")

import math

'''
Your task is to create a Circle constructor that creates a circle 
with a radius provided by an argument. The circles constructed must 
have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which 
give both respective areas and perimeter (circumference).'''

logging.info("starting of the definition of Circle class")
class Circle:
    logging.info("beginning of the execution of Circle class")
    logging.info("declaration of pi variable")
    pi = math.pi
    def __init__(self,radius):
        '''
        This method accepts a single value and assign it to radius
        :param radius:
        '''
        self.radius = radius

    def getArea(self):
        '''
        Calculates the Area of the circle
        :return:
        '''
        logging.info("Beginning of the execution of getArea")
        logging.info("passing the radius as '%s'",self.radius)
        area = Circle.pi*pow(self.radius,2)
        logging.info("Area had been calculated as '%s' and is being returned",area)
        return area

    def getPerimeter(self):
        '''
        method to calulcate the permiter of a circle
        :return:
        '''
        try :

            logging.info("calculating the perimeter of a circle with radius '%s'",peri)
            peri = 2*Circle.pi*self.radius
            logging.info("Permiter is calculated as '%s' and is being returned",peri)
            return peri
        except Exception as e:
            logging.error("Error occured in Cicle",e)
        finally:
            logging.info("perimeter calculation had been done")
logging.info("End of the definition of Circle class")

Circle_obj1 = Circle(5)
logging.info(Circle_obj1.getArea())

def sort_by_length(list1):
    try:

        dict1 = {}
        list2 = []
        for i in list1:
            list2.append(len(i))
        dict1 = dict(zip(list2,list1))
        list3 = []
        for i in sorted(dict1):
            list3.append(dict1[i])
        return (list3)
    except Exception as e:
        logging.Error('Error occured in sort by legth function ',e)
    finally:
        logging.info("completion of soft by length function")

list1=['apple','Microsoft','google']
list1 = sort_by_length(list1)
logging.info(list1)

def is_triplet(num1,num2,num3):
    try:
        logging.info('Beginning of execution of is_triplet(%s,%s,%s)',num1,num2,num3)
        list1 = [num1,num2,num3]
        list1.sort()
        return pow(list1[0],2)+pow(list1[1],2) == pow(list1[2],2)

    except Exception as e:
        logging.error("exception raised in is_triplet function ",e)
    finally:
        logging.info("End of execution if is_triplet function")

logging.info(is_triplet(5, 4, 3) )
logging.info(is_triplet(13, 5, 12) )
logging.info(is_triplet(1, 2, 3))