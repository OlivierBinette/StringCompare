#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>

namespace py = pybind11;
using namespace std;

class Tokenizer {
    public:
    virtual double tokenize(const string &s) = 0;

    virtual double batch_tokenize(const vector<string> &sentences) = 0;

    double operator()(const string &s) {
        return tokenize(s, t);
    }

}

