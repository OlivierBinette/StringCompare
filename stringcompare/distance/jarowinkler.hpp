#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

#include "jaro.hpp"

namespace py = pybind11;
using namespace std;

class JaroWinkler: public StringComparator {
public:

  bool similarity;

  JaroWinkler(bool similarity=false){
    this->similarity = similarity;
  }

  double jarowinkler(const string &s, const string &t, double p=0.1) {
      int ell = 0;
      for (size_t i = 0; i < min({s.size(), t.size(), size_t(4)}); i++) {
          if (s[i] == t[i]){
              ell += 1;
          } else {
              break;
          }
      }

      double sim = Jaro::jaro(s, t);

      return sim + ell * p * (1-sim);
  }

  double compare(const string &s, const string &t) {
      if (this->similarity == true) {
          return jarowinkler(s, t);
      } else { 
          return 1.0 - jarowinkler(s, t);
      } 
  }
  
};
