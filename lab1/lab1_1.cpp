#include <iostream>
#include <optional>


struct str
{
    char* symbols = nullptr;
    size_t len = 0;
};

struct CeasarCode
{
    str key;
    size_t position = 0;
    
    str encode(str line)
    {
        str code{new char[line.len+1], line.len};
        
        for(size_t i = 0; i < line.len; i++)
        {
            if((size_t)(line.symbols[i]) < this->position || (size_t)(line.symbols[i]) >= this->position+key.len)
            {
                code.symbols[i] = line.symbols[i];
                continue;
            }
            code.symbols[i] = key.symbols[(size_t)line.symbols[i]-this->position];
        }
        return code;
    }
};

void main()
{
	CeasarCode cc;
	str exmpl;
	str code;
	
	cc.key.symbols = "QWERTY";
	cc.key.len = 6;
	cc.position = (size_t)'a'+4;
	
	exmpl.symbols = "abcdefghijklmnopqrstuvwxyz";
	exmpl.len = 26;
	
	code = cc.encode(exmpl);
	
	std::cout << code.symbols;
}