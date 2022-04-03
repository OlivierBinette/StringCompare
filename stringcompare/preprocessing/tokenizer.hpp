#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <vector>

namespace py = pybind11;
using namespace std;

class Tokenizer {
    public:
    virtual string tokenize(const string &sentence) = 0;

    string operator()(const string &sentence) {
        return compare(s);
    }

    vector<string> batch_tokenize(const vector<string> &sentences) {
        vector<string> result(sentences.size());
        
        for (size_t i = 0; i < sentences.size(); i++) {
            result[i] = this->tokenize(sentences[i]);
        }

        return result;
    }
}
