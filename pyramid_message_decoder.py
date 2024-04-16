"""

    Scott Quashen
    Data Annotation - Assessment
    Part 3: The Pyramid Message Decoder Solution
    April 15 2024

    ------
    Description: This program decodes a message from a txt file that is encoding using a pyramid format. A message is hidden inside a text file that contains data in the following format: each line has a number followed by a word. There are many lines in the file. To decode the message from the text data, the data needs to be reorganized into a pyramid-like structure based on the numbers found on each of the lines of data. The last number in each row of the pyramid is part of the hidden message, in order. All other words are ignored.
    ------
    
    ------
    Inputs: Reads data from disk. [ Update to your file path ] *** Interestingly, the message encoded in this file is not a coherent sentence.
    ------
    
    ------
    Outputs: Decoded message, or File not found error
    ------
    
    ------
    Dependencies: None.
    ------

    ------
    Assumptions: Developed and tested using Spyder 5.15.7, Python version 3.11.5 on macOS 14.4.1
    ------
    
"""

def main():
    
    """
    
    Main function to decode a message from a text file using a pyramid format.
    
    """
    
    file_path = '/Users/scottquashen/Developer/Python Projects/coding_qual_input.txt'
    
    print( decode( file_path ) )

# end main func


def decode( message_file ):
    
    """
    
    Description
    -----------
        
    1) Data Preparation: The text file's content is parsed into a dictionary, where each line provides a number and a corresponding word. This forms key-value pairs, crucial for later decoding.

    2) Building the Pyramid: To construct the pyramid, we sort the numbers extracted from the dictionary in ascending order. The pyramid is a list of lists, where each sequential row contains an additional element. Rows are created by adding numbers based on their sorted index until the row has one more element than the previous row. The amount of rows created is however many are needed to contain all of the elements. 

    3) Decoding Process: With the pyramid in place, decoding begins. At each row's end, the number is used as a key to look up the corresponding word in the dictionary. These words are appended to a list, forming the "secret" message.

    4) Message Reconstruction: The extracted words are stored in a list of strings, representing the decoded message in the correct order. To reveal the hidden message, the strings are combined into a single string.
    
    Parameters
    ----------
    message_file (Txt file): The file containing the encoded message. Each line in the file contains a number followed by a word.
    
    Returns
    -------
    secretMessage (STRING): The decoded message hidden in the input text file.
        
    """
    
    message_map = {}
    try:
        with open( message_file, 'r' ) as file:
            for line in file:
                number, word = line.strip().split()
                message_map[ int( number ) ] = word # dictionary entries to associate number (key) to word (value)

        numbers = list( message_map.keys() )
        numbers.sort()

        height = 1 # if height were initialized to 0 the condition below would immediately be false
        while height * ( height + 1 ) / 2 < len( numbers ): # ensure there are enough rows to accomodate all elements
            height += 1 

        pyramid = []
        index = 0
        
        for i in range( 1, height + 1 ): # range from 1 to height, inclusive
            row = [] 
            
            for _ in range( i ): # it just so happens that i represents both the row itself and the total amount of elements inside the row
                if index < len( numbers ): # don't add elements that don't exist
                    
                    row.append( numbers[ index ] ) # numbers are added sequentially 
                    index += 1
                    
            pyramid.append( row )

        decoded_words = [ message_map[ line[ -1 ] ] for line in pyramid ] # the last element of each row 
        secret_message = " ".join( decoded_words )

        return secret_message

    except FileNotFoundError:
        print( f"Error: File '{message_file}' not found." )
        
# end decode func


# example calls
if __name__ == "__main__":
    main()
