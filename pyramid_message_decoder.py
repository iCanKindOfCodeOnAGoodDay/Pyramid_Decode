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
    
    The `decode()` function decodes a message from a text file encoded in a pyramid format. 
    The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (e.g., 1, 3, and 6).
    The pyramid is contructed by ordering the numbers consecutively, and adding another number to each row, starting with 1 on the top. 
    How many rows to be built is determined by calculating how many rows are needed to accomodate 
    all of the elements. By extracting only the numbers, and sorting them, 
    pyramid rows can be constructed by adding the numbers to each
    row based on the numbers index, with
    each row getting one more number,
    until all of the numbers are 
    added to the pyramid.
    
    Line data from the txt file is extracted. Each line is a dictionary entry, with the number being the key, and the value being 
    the word. By using the  element found at the end of each row of the pyramid, we can look up the corresponding
    value for that element in the dictionary, which is how the hidden message is revealed.
    
    Example Pyramid:
        
        1
        2 3
        4 5 6
            
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
    
    message_dict = {} # This dictionary will hold key value pairs for each line loaded from the text file
    
    try:
    
        with open( message_file, 'r' ) as file:
                    
            for line in file:
                data = line.strip().split() # Isolate the data on each line 
                message_dict[ int( data[ 0 ] ) ] = data[ 1 ] # The number on each line is the dictionary key, and the word is the value
         
            numbers = list( message_dict.keys() ) # Isolate the numbers so they can be sorted and added into a pyramid
            numbers.sort() 
            amount_of_pyramid_layers = 1 
            
            while amount_of_pyramid_layers * ( amount_of_pyramid_layers + 1 ) / 2 < len( numbers ): # By using this calculation, it is ensured that there are enough rows to accommodate all of the elements in the pyramid (determine total row count)
                amount_of_pyramid_layers += 1
                        
            pyramid = [] # Stores rows of numbers in consecutive order, with each row having one more number than the previous
            index = 0 # Variable used to identify which number is added to each spot of the pyramid
            
            for i in range( 1, amount_of_pyramid_layers + 1 ): # Adding 1 ensures loop iterates over all necessasry rows for the pyramid because the Python range does not include stop value
                row = []
                for j in range( i ): # The inner loop fills each row with i amount of the correct numbers based on index
                    if index < len( numbers ):                   
                        row.append( numbers[ index ] )
                        index += 1 
                        
                pyramid.append( row ) # Row is filled
            
            decoded_words = []
            
            for line in pyramid:
                lastDigitInEachLine = line[ len( line ) - 1 ]
                decoded_words.append( message_dict[ lastDigitInEachLine ] ) # Use the disovered key to look up the value in the dict
                    
            secretMessage = " ".join( [ str(i) for i in decoded_words ] ) # Combine the list of strings into a single string

            return secretMessage
        
    except FileNotFoundError:
        print( f"Error: File '{message_file}' not found.")

        
# end


# calls

if __name__ == "__main__":
    
    main()
    
    
    
    
