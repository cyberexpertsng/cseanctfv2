#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
#include <cstring>
#include "MurmurHash2.h"

uint64_t MurmurHash64A ( const void * key, int len, uint64_t seed )
{
    const uint64_t m = BIG_CONSTANT(0xc6a4a7935bd1e995);
    const int r = 47;

    uint64_t h = seed ^ (len * m);

    const uint64_t * data = (const uint64_t *)key;
    const uint64_t * end = data + (len/8);

    while(data != end)
    {
        uint64_t k = *data++;

        k *= m; 
        k ^= k >> r; 
        k *= m; 
        
        h ^= k;
        h *= m; 
    }

    const unsigned char * data2 = (const unsigned char*)data;

    switch(len & 7)
    {
    case 7: h ^= ((uint64_t) data2[6]) << 48;
    case 6: h ^= ((uint64_t) data2[5]) << 40;
    case 5: h ^= ((uint64_t) data2[4]) << 32;
    case 4: h ^= ((uint64_t) data2[3]) << 24;
    case 3: h ^= ((uint64_t) data2[2]) << 16;
    case 2: h ^= ((uint64_t) data2[1]) << 8;
    case 1: h ^= ((uint64_t) data2[0]);
            h *= m;
    };
    
    h ^= h >> r;
    h *= m;
    h ^= h >> r;

    return h;
} 

const std::vector<uint64_t> hash_values = {
    0x911ee1d25da755aa,
    0x678a6473e4a9044a,
    0xb44f230e4f5d9c47,
    0x70260e10b014d067,
    0x9b0ef6f4684f9915,
    0x1a1378a8b78e9a55,
    0x911ee1d25da755aa,
    0x1ff01ebc0c7408cb,
    0x26a3abbdccb22431,
    0xc22268ab7cbf7104,
    0x701e6962bf9b2556,
    0x9b0ef6f4684f9915,
    0xb44f230e4f5d9c47,
    0xf9dfa617052dfd5e,
    0x188cf31a079d66fc,
    0xdf10f650f01e63ae,
    0xbf4208c9b9e129a7,
    0xf9dfa617052dfd5e,
    0xd58e3ba2fbef9d8c,
    0xdf10f650f01e63ae,
    0x678a6473e4a9044a,
    0xd58e3ba2fbef9d8c,
    0xf9dfa617052dfd5e,
    0x26a3abbdccb22431,
    0x3eb8b6a6f0753e49,
    0x9b0ef6f4684f9915,
    0x911ee1d25da755aa,
    0x1ff01ebc0c7408cb,
    0xa12c8af2572dfa48,
    0x701e6962bf9b2556,
    0x9b0ef6f4684f9915,
    0x678a6473e4a9044a,
    0xf9dfa617052dfd5e,
    0xe2a06e4b6bf05d6, 
    0x701e6962bf9b2556,
    0xb44f230e4f5d9c47,
    0x678a6473e4a9044a,
    0xf9dfa617052dfd5e,
    0xa54b50d4b5707b62,
    0x827aee59df4bcce8,
    0x827aee59df4bcce8,
    0x827aee59df4bcce8,
    0xb1300fe8129bca46 
};

std::string findFlag(const std::string& charset) {
    std::string known_flag(hash_values.size(), '?'); 

    for (size_t i = 0; i < hash_values.size(); ++i) {
        bool found = false;
        for (char c : charset) {
            uint64_t hash = MurmurHash64A(&c, sizeof(c), 0x1337);
            if (hash == hash_values[i]) {
                known_flag[i] = c;
                found = true;
                break;
            }
        }
        if (!found) {
            std::cerr << "Character not found for index " << i << std::endl;
            break; 
        }
    }
    return known_flag;
}


int main() {
    std::string charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{_}-";
    std::string flag = findFlag(charset);
    
    std::cout << "Flag: " << flag << std::endl;
    return 0;
}
