#include <iostream>
#include <map>



std::map<char, size_t> index(const char* word, size_t len)
{
    std::map<char, size_t> index_table;
    
    for(size_t i = 0; i < len; i++)
    {
        index_table[word[i]] = i;
    }
    return index_table;
}



char* route_encode(const char* message, const size_t len, const char* key, size_t rows, size_t cols)
{
    const auto digits = index(key, cols);
    char copy[len+(len%cols)];
    char* code = new char[len+(len%cols)];
    
    for(size_t row = 0; row < rows; row++)
    {
        for(size_t i = 0; i < cols; i++)
        {
            size_t ind = row*cols + i;
            
            if(ind > len)
            {
                copy[ind] = ' ';
                continue;
            }
            copy[ind] = message[ind];
        }
        
        size_t i = 0;
        for(const auto& digit: digits)
        {
            size_t ind = row*cols;
            code[ind + i] = copy[ind+digit.second];
            i++;
        }
    }
    return code;
}



void main()
{
	std::cout << route_encode("abcdefghigklmnopqrstuvwxyz", 26, "nope", 26, 4);
}