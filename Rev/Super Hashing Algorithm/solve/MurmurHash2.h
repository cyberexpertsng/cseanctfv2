#ifndef MURMUR_PLATFORM_H
#define MURMUR_PLATFORM_H

  void SetAffinity ( int cpu );
  #include <stdint.h>
  #include <strings.h>

  #define	FORCE_INLINE __attribute__((always_inline))
  #define BIG_CONSTANT(x) (x##LLU)
  #define _stricmp strcasecmp

#endif 
/* MURMUR_PLATFORM_H */

#ifdef __cplusplus
  extern "C" {
#endif

uint64_t MurmurHash64A      ( const void * key, int len, uint64_t seed );

#ifdef __cplusplus
  }
#endif