

# definitions

def main():
    
    message_file = '/Users/scottquashen/Developer/Python Projects/coding_qual_input.txt'
    
    theMessage = decode( message_file )
    
    #print( theMessage )
    


def decode( message_file ):
    
    # declare empty dictionary
    
    message_dict = {}

    
    # load txt file
    
    with open( message_file, 'r' ) as file:
        

        
        # loop over the file line by line
        
        for line in file:
        
		    # remove leading and trailing whitespace from line and split the line to get the number and word in data list
       
            data = line.strip().split()
		
            # insert the number as key and word as value
       
            message_dict[ int( data[ 0 ] ) ] = data[ 1 ]
            

        
        print( message_dict )
         
     	# get the list of keys of the dictionary in numbers list
         
        numbers = list( message_dict.keys() )
         
         # sort the numbers list in ascending order
         
        numbers.sort() 
        
        print( numbers )
        
        # now that we have our map, we can build the pyramid
        
        n = 1
        
        while n * ( n + 1 ) / 2 < len( numbers ):
            
            n += 1
        
        pyramid = []
        
        num_index = 0
        
        for i in range( 1, n + 1 ):
            
            row = []
            
            for j in range( i ):
                
                if num_index < len( numbers ):
                    
                    row.append( numbers[ num_index ] )
                    
                    num_index += 1
                    
            pyramid.append(row)
            
        print( pyramid[ 3 ] )

        # now we have built the pyramid of numbers, we can extract the value of the last digit
        # then, we can look up the corresponding value
        # then construct the hidden message into a string of the values
        # then return the hidden message string
        
        decoded_keys = []
        
        decoded_words = []
        
        for line in pyramid:
            
            lastDigitInEachLine = line[ len( line ) - 1 ]
            
            print( lastDigitInEachLine )
            
            decoded_keys.append( lastDigitInEachLine )
            
            # now that we have extracted the last digit in each line, we can look up the value in our map

            
            decoded_words.append( message_dict[ lastDigitInEachLine ] )
            
        
        print( decoded_keys )
        
        print( decoded_words )
        
        # take the list of words and combine them into a single string
        
        secretMessage = " ".join( [ str(i) for i in decoded_words ] )
        
        print( secretMessage )
        
        # return the secret ( decoded ) message
        
        return secretMessage
        
            
        
        
        
            
        
    
    
    


            
            
        
    
        
        

            




# calls

if __name__ == "__main__":
    
    main()