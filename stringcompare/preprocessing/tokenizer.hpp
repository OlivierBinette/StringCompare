#pragma once

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <set>
#include <sstream>

namespace py = pybind11;
using namespace std;

class Tokenizer {
public:

    multiset<string> tokenize(const string &sentence){
        multiset<string> result;
        return result;
    }

    multiset<string> operator()(const string &sentence) {
        return this->tokenize(sentence);
    }

    vector<multiset<string>> batch_tokenize(const vector<string> &sentences) {
        vector<multiset<string>> result(sentences.size());
        for (size_t i = 0; i < sentences.size(); i++) {
            result[i] = this->tokenize(sentences[i]);
        }

        return result;
    }

};

class DelimTokenizer: public Tokenizer {
public:

    string delim;

    DelimTokenizer(const string &delim) {
        this->delim = delim;
    }

    multiset<string> tokenize(const string &sentence) {
        multiset<string> result;
        
        stringstream ss(this->delim);
        string s;
        while(ss >> s) {
            result.insert(s);
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

    multiset<string> tokenize(const string &sentence) {
        const char* cstring = sentence.c_str();
        multiset<string> result;

        for (size_t i = 0; i < sentence.size() - this->n; i++) {
            result.insert(string(cstring, this->n));
            cstring += this->n;
        }

        return result;
    }
};
