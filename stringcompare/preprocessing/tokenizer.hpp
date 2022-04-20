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
        
        stringstream ss(sentence);
        string s;
        while(getline(ss, s, this->delim)) {
            py::print(s);
            result.push_back(s);
        }

        return result;
    }
};

class WhitespaceTokenizer: public DelimTokenizer {
public:
    WhitespaceTokenizer(): DelimTokenizer(" ") {

    }
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
            result.push_back(string(cstring, this->n));
            cstring += this->n;
        }

        return result;
    }
};
