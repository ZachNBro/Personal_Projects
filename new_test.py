"""
    File name: new_test.py
    Author: Zachary Brown
    Date created: 12/21/21
    Date last modified: 01/09/22
    Python version: 3.9
    Description: Import an original and potentially
    edited file to scan for malicious code by converting
    each file to bytes, constructing two arrays and
    comparing the byte values.
"""

import numpy as np

class Test:

    def __init__(self): # class constructor
        self._data = ""
        self._data_two = ""

    @property # use property decorator to represent the python property() function get argument
    def data(self):
        return self._data

    @property
    def data_two(self):
        return self._data_two

    @data.setter # use setter decorator to represent the python property() function set argument
    def data(self, a):
        self._data = a

    @data_two.setter
    def data_two(self, b):
        self._data_two = b

def main():

    try:
        dt = np.dtype('B')  # 'B' = unsigned byte values from 0 to 255

        # enter file paths
        original_path = input("Enter path of original file:")
        scanned_path = input("Enter path of new file to be scanned:")

        new_test.data = np.fromfile(original_path, dtype=dt)  # set data variable and type
        new_test.data_two = np.fromfile(scanned_path, dtype=dt)  # set data_two variable and type

        original_code = np.array(new_test.data) # get data variables and convert to numpy array
        scanned_code = np.array(new_test.data_two)

        original_length = (len(original_code)) # set original and scanned array length variables for later comparison
        scanned_length = (len(scanned_code))

        ''' The conditional statements below check and resize the arrays if needed for proper comparison.
                    Arrays must be of the same size in order to compare elements '''

        # determine if any code was added or deleted
        if len(original_code) == len(scanned_code): # check if length of each array is the same

            # compare the element values from each array using a map with an iterator function (lambda)
            result = map(lambda x, y: x == y, original_code, scanned_code)
            scan = (np.array(list(result))) # use list for proper display of elements

            position = np.where(scan == False) # if map comparison returns False value, set element position in array

            if False not in scan:
                print("No malicious code detected")

            else:
                print("Code to be examined:")
                # convert element(s) position to bytes then decode to display plain text
                print(bytes(scanned_code[position]).decode('utf-8'))

        elif len(original_code) < len(scanned_code): # check if original code length is less than scanned code

            len(original_code) == [] * scanned_length # set length to greater value

            new_array_two = np.append(original_code, scanned_code) # append to new array for proper comparison
            result_two = map(lambda x, y: x == y, new_array_two, scanned_code) # iterate over new array
            scan_two = (np.array(list(result_two)))

            print("***Potential code addition and/or alteration detected***")
            position = np.where(scan_two == False) # display where element positions equal false

            print("Code to be examined:")
            print(bytes(scanned_code[position]).decode('utf-8'))

        elif len(original_code) > len(scanned_code): # check if original code length is greater than scanned code

            len(scanned_code) == [] * original_length

            new_array_three = np.append(scanned_code, original_code)
            result_three = map(lambda x, y: x == y, new_array_three, original_code)
            scan_three = (np.array(list(result_three)))

            print("***Potential code deletion and/or alteration detected***")
            position = np.where(scan_three == False)

            print("Code to be examined:")
            # change variable to show original code positions and possible code deleted
            print(bytes(original_code[position]).decode('utf-8'))

    except IOError: # throw exception if file(s) do not exist

        print("Error while opening either file" + '\n' +
              "Please ensure path is correct WITH file type")
        main()

if __name__ == '__main__':

    new_test = Test()  # create new instance of class
    main()