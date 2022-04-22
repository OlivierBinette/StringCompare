#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <sstream>

namespace py = pybind11;
using namespace std;

class Tokenizer {
public:

    vector<string> tokenize(const string &sentence){
        vector<string> result;
        return result;
    }

    vector<string> operator()(const string &sentence) {
        return this->tokenize(sentence);
    }

    vector<vector<string>> batch_tokenize(const vector<string> &sentences) {
        vector<vector<string>> result(sentences.size());
        for (size_t i = 0; i < sentences.size(); i++) {
            result[i] = this->tokenize(sentences[i]);
        }

        return result;
    }

};

class DelimTokenizer: public Tokenizer {
public:

    string delim;

    DelimTokenizer(const string delim) {
        this->delim = delim;
    }

    vector<string> tokenize(const string &sentence) {
        vector<string> result;        

        size_t k = this->delim.size();
        size_t pos = 0;
        size_t match = 0;

        while ((match = sentence.find(this->delim, pos)) != string::npos) {
            if (match != pos) {
                result.push_back(sentence.substr(pos, match - pos));
            }
            pos = match + k;
        }
        if (pos < sentence.size()) {
            result.push_back(sentence.substr(pos));
        }

        return result;
    }
};

class WhitespaceTokenizer: public DelimTokenizer {
public:
    WhitespaceTokenizer(): DelimTokenizer(" ") {}
};

class NGramTokenizer: public Tokenizer {
public:

    int n;

    NGramTokenizer(int n) {
        this->n = n;
    }

    vector<string> tokenize(const string &sentence) {
        const char* cstring = sentence.c_str();
        vector<string> result;

        for (size_t i = 0; i < sentence.size() - this->n; i++) {
            result.push_back(sentence.substr(i, this->n));
        }

        return result;
    }
};
