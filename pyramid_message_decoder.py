"""

    Scott Quashen
    Data Annotation - Assessment
    Part 3: The Pyramid Message Decoder Solution
    April 10 2024

    ------
    Description: This program decodes a message from a txt file that is encoding using a pyramid format. 
    ------
    
    ------
    Inputs:  Reads data from disk. [ Update to your file path ] *** Interestingly, the message encoded in this file is not a coherent sentence.
    ------
    
    ------
    Outputs: Decoded message
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
    'main()' contains the path to the txt file stored on Scott Quashen's system, and passes that file into the decode function, which decodes the hidden message from the input txt file
    
    Outputs
    -------
    Decoded message, or error message

    """
    
    file_path = '/Users/scottquashen/Developer/Python Projects/coding_qual_input.txt'
    
    try:
        
        the_message = decode( file_path )
        
        print( the_message )
        
    except FileNotFoundError:
        
        print( f"Error: File '{file_path}' not found." )
        
    except Exception as e:
        
        print( f"An error occurred: {e}" )
    
    
# end
    

def decode( message_file ):
    
    """
    
    Description
    -----------
    
    The `decode()` function decodes a message from a text file encoded in a pyramid format. The key to decoding the message is to use the words corresponding to the numbers at the end of each pyramid line (e.g., 1, 3, and 6).
    
    To reveal the hidden message, the script extracts line data from the text file and creates key-value pairs for each line with the line's number being the key and the line's word being the value for a dictionary called message_dict. From there, the script builds the pyramid by first creating a list of only the numbers, then sorts that list of numbers, then determines how many rows is needed to accomodate all of the elements, then iterates each row filling them with correct elements (the numbers). The pyramid is now built. 
    
    In the inner most loop (where the pyramid is filled with number data), a list of the words is appended with each 'secret word' by using the last number in each row (the key of the message_dict) to look up the corresponding word (value) in the dictionary. Now that we have the hidden message as Strings within a list, finally, the list of decoded words is converted into a single string, which is the final decoded message returned by the function. Problem solved.
    
    
    Parameters
    ----------
    
    `message_file` (Txt file): The file containing the encoded message. Each line in the file contains a number followed by a word.
    
    Returns
    -------
    
    `secretMessage` (STRING): The decoded message hidden in the input text file.
        
    """
    
    # This dictionary will hold key value pairs for each line loaded from the text file
        
    message_dict = {}
    
    # Load file
    
    try:
    
        with open( message_file, 'r' ) as file:
                    
            for line in file:
            
    		    # Isolate the data on each line 
                
                data = line.strip().split()
    		
                # Insert the number as key and word as value
           
                message_dict[ int( data[ 0 ] ) ] = data[ 1 ]
    
            
            # Isolate the numbers
            
            numbers = list( message_dict.keys() )
    
            numbers.sort() 
            
            # Create rows for each 'layer' of the pyramid
    
            amount_of_rows = 1
            
            # By using this calculation, it is ensured that there are enough rows to accommodate all of the elements in the pyramid (determine total row count)
        
            while amount_of_rows * ( amount_of_rows + 1 ) / 2 < len( numbers ):
                
                # add a row
                
                amount_of_rows += 1
            
            # Initialize empty pyramid
            
            pyramid = []
            
            # Initialize variable outside of the below loops
            
            current_number_index = 0
            
            # The outer loop iterates each row
            
            for i in range( 1, amount_of_rows + 1 ):
                
                row = []
                
                # The inner loop fills each row with numbers
                
                for j in range( i ):
                        
                    if current_number_index < len( numbers ):
                        
                        # Add i amount of elements from list of numbers according to the current_number_index
                        
                        row.append( numbers[ current_number_index ] )
                        
                        # Increment number index so that each iteration fills each row with the proper data
                        
                        current_number_index += 1
                        
                # The row is filled, add it to the pyramid        
                        
                pyramid.append( row )
                
            # Now that we have built the pyramid of numbers, we extract the last number from each row,
            # which serves as the key to look up the corresponding word in the dictionary.
            
            # Using these keys, we construct a list of the decoded words,
            # which will form the hidden message once combined into a single string.
            
            # Finally, we return the hidden message string.
            
            decoded_keys = []
            
            decoded_words = []
            
            for line in pyramid:
                
                lastDigitInEachLine = line[ len( line ) - 1 ]
                            
                decoded_keys.append( lastDigitInEachLine )
                
                # Now that the last digit in each line has been extracted, each key is identified.
                # Each key is used to look up the corresponding value in the message_dict.

                
                decoded_words.append( message_dict[ lastDigitInEachLine ] )
                    
            # Combine them decoded_words into a single string
            
            secretMessage = " ".join( [ str(i) for i in decoded_words ] )
                    
            # Return the secret ( decoded ) message
                        
            return secretMessage
        
    except Exception as e:
        
        raise e
    
# end
        
            

# calls

if __name__ == "__main__":
    
    main()