"""

    Scott Quashen
    Data Annotation - Assessment
    Part 3: The Pyramid Message Decoder Solution
    April 12 2024

    ------
    Description: This program decodes a message from a txt file that is encoding using a pyramid format. 
    ------
    
    ------
    Inputs:  Reads data from disk. [ Update to your file path ] *** Interestingly, the message encoded in this file is not a coherent sentence.
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


# definitions


def main():
    
    """
    
    Description
    ----------
    'main()' contains the path to the txt file stored on Scott Quashen's system, and passes that file into the decode function, 
    which decodes the hidden message from the input txt file
    
    Parameters
    ----------
    None.
    
    Outputs
    -------
    Decoded message, or error message

    """
    
    file_path = '/Users/scottquashen/Developer/Python Projects/coding_qual_input.txt'
    decode( file_path )
    
# end
    

def decode( message_file ):
    
    """
    
    Description
    -----------
    
    A message is hidden inside a text file that contains data in the following format: 
    each line has a number followed by a word. 
    There are many lines in the file. 
    To decode the message from the text data, 
    the data needs to be reorganized into a pyramid-like structure based on the numbers 
    found on each of the lines of data. The last number in each row of the pyramid is part of the hidden message, 
    in order. All other words are ignored.
            
    Exception Possiblity 
    ----------
    
    If file can't be opened function could throw exception.
    
    Parameters
    ----------
    
    `message_file` (Txt file): The file containing the encoded message. Each line in the file contains a number followed by a word.
    
    Returns
    -------
    
    `secretMessage` (STRING): The decoded message hidden in the input text file.
        
    """
    
    message_dict = {} # This dictionary will hold key value pairs for each line loaded from the text file: key - number, value - word
    
    try:
    
        with open( message_file, 'r' ) as file:
                    
            for line in file:
                data = line.strip().split() # Isolate line data from text file
                message_dict[ int( data[ 0 ] ) ] = data[ 1 ] # Fill dictionary with key value pairs from every line of text file
         
            numbers = list( message_dict.keys() ) # Isolate the numbers so they can be sorted and added into a pyramid
            numbers.sort() 
            amount_of_pyramid_layers = 1 
            
            while amount_of_pyramid_layers * ( amount_of_pyramid_layers + 1 ) / 2 < len( numbers ): # By using this calculation, it is ensured that there are enough rows to accommodate all of the elements in the pyramid (determine total row count)
                amount_of_pyramid_layers += 1
                        
            pyramid = [] # Stores rows (lists) of numbers in consecutive order, with each row having one more number than the previous
            index = 0 # Used to identify which number is added to each spot of the pyramid
            
            for i in range( 1, amount_of_pyramid_layers + 1 ): # Adding 1 ensures loop iterates over all necessasry rows for the pyramid because the Python range does not include stop value
                row = []
                for j in range( i ): # Fill each row with numbers based on index
                    if index < len( numbers ):                   
                        row.append( numbers[ index ] )
                        index += 1 
                        
                pyramid.append( row ) 
            
            decoded_words = []
            
            for line in pyramid:
                lastDigitInEachLine = line[ len( line ) - 1 ]
                decoded_words.append( message_dict[ lastDigitInEachLine ] ) # Use each key to look up each hidden word from the dictionary
                    
            secretMessage = " ".join( [ str(i) for i in decoded_words ] ) # The words were found in the correct order so we can just create a single string

            return secretMessage
        
    except FileNotFoundError:
        print( f"Error: File '{message_file}' not found.")

        
# end


# calls

if __name__ == "__main__":
    
    main()
    
    
    
    
