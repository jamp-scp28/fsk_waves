class Byte_Utility:
    def convertByteToString(string):
        binary_int = int(string, 2);
 
        # Getting the byte number
        byte_number = binary_int.bit_length() + 7 // 8
        
        # Getting an array of bytes
        binary_array = binary_int.to_bytes(byte_number, "big")
        
        # Converting the array into ASCII text
        ascii_text = binary_array.decode()
        
        # Getting the ASCII value
        return ascii_text