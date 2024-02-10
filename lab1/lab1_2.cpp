#include <iostream>

char* reverse_char_ord(const char* word, size_t len)
{
    auto code = new char[len];
    
    for(size_t i = 0; i < len; i++)
    {
        code[i] = ((size_t)'z'-((size_t)word[i]-(size_t)'a'));
    }
    return code;
}

void main()
{
    std::cout << reverse_char_ord("abcd", 4);
}