#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

#include "comparator.hpp"
#include "../preprocessing/tokenizer.hpp"

namespace py = pybind11;
using namespace std;

class Jaccard: public StringComparator {
public:

    Tokenizer tokenizer;
    bool normalize;
    bool similarity;

  Jaccard(Tokenizer tokenizer, bool normalize=true, bool similarity=false){
        this->tokenizer = tokenizer;
        this->normalize = normalize;
        this->similarity = similarity;
  }

  double compare(const string &s, const string &t) {
      return 0;
  }
  
};
