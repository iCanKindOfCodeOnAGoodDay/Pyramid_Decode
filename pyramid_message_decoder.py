"""

    Scott Quashen
    Data Annotation - Assessment
    Part 3: The Pyramid Message Decoder Solution
    April 16 2024

    ------
    Description: This program decodes a message from a txt file that is encoding using a pyramid format. A message is hidden inside a text file that contains data in the following format: each line has a number followed by a word. There are many lines in the file. To decode the message from the text data, the data needs to be reorganized into a pyramid-like structure based on the numbers found on each of the lines of data. The last number in each row of the pyramid is the key for each of the hidden words, in order. All other words are ignored.
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
    Description
    -----------
    Main function to decode a message from a text file using a pyramid format.
    
    Note
    -----------
    *update to your file_path
    
    """
    
    file_path = '/Users/scottquashen/Developer/Python Projects/coding_qual_input.txt' # update to your path
    
    print( decode( file_path ) )

# end main func


def decode( message_file ):
    
    """
    
    Description
    -----------
    
        1) Data Preparation: The text file's content is parsed into a dictionary, where each line provides a number and a corresponding word. This forms key-value pairs, crucial for later decoding.
    
        2) Building the Pyramid: To construct the pyramid, we sort the numbers extracted from the dictionary in ascending order. The pyramid is a list of lists, where each subsequent row contains an additional element. Rows are created by sequentially adding numbers from the sorted list until the row has one more element than the previous row. The amount of rows created is however many are needed to contain all of the elements. 
    
        3) Decoding Process: With the pyramid in place, decoding begins. At each row's end, the number is used as a key to look up the corresponding word in the dictionary. The decoded words from the pyramid are collected in a list, forming the "secret" message.
    
        4) Message Reconstruction: To reveal the hidden message, our list of strings are combined into a single string, and returned from the function as the 'secret' message.
    
    Input
    ----------
    message_file < TXT File > : The file containing the encoded message. Each line in the file contains a number followed by a word.
    
    Output
    -------
    secretMessage < String > : The decoded message hidden in the input text file.
        
    """
    
    message_map = {} # contains an entry for each line of data with the number being the key and the value being the word found on the same line 
    try:
        with open( message_file, 'r' ) as file:
            
            for line in file:
                number, word = line.strip().split() # extract number and word from each line of data
                message_map[ int( number ) ] = word # dictionary entry for each line to associate each number (key) to each word (value) 

        numbers = list( message_map.keys() ) # isolate numbers to add to pyramid
        numbers.sort() # so that we can add the numbers to pyramid from lowest to highest

        height = 1 # pyramid height (and width) starts with a single element
        while height * ( height + 1 ) / 2 < len( numbers ): # ensure the pyramid accomodates all elements
            height += 1 

        pyramid = [] # this list will contain a list for each row of the pyramid
        number_index = 0 # used to place the correct element in the correct position into the pyramid
        
        for i in range( 1, height + 1 ): # range from 1 to height, inclusive
            row = []   
            for _ in range( i ): # each row at height i also has i amount of elements (starting with 1)
                if number_index < len( numbers ): # don't add elements that don't exist
                    row.append( numbers[ number_index ] ) # numbers are added to pyramid sequentially 
                    number_index += 1 # prepare to add the next element from the numbers list into the pyramid
            pyramid.append( row )

        decoded_words = [ message_map[ line[ -1 ] ] for line in pyramid ] # the last element of each row of the pyramid is the key (number) used to 'look up' the value (word) in our dictionary 
        secret_message = " ".join( decoded_words ) # take the list of 'hidden' words and combine them into a single string which is now the entire 'secret message'
        return secret_message # string

    except FileNotFoundError:
        print( f"Error: File '{message_file}' not found." ) # make sure to update your path
        
# end decode func


# example calls
if __name__ == "__main__":
    main()
