#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "tokenizer.hpp"

PYBIND11_MODULE(_preprocessing, m) {

    m.attr("__name__") = "stringcompare.preprocessing._preprocessing";
        
    py::class_<Tokenizer>(m, "Tokenizer")
        .def("__call__", &Tokenizer::operator())
        .def("batch_tokenize", &Tokenizer::batch_tokenize);
    
    py::class_<DelimTokenizer, Tokenizer>(m, "DelimTokenizer")
        .def(py::init<string>(), py::arg("delim"))
        .def("tokenize", &DelimTokenizer::tokenize);
    
    py::class_<WhitespaceTokenizer, DelimTokenizer>(m, "WhitespaceTokenizer")
        .def(py::init<>());

    py::class_<NGramTokenizer, Tokenizer>(m, "NGramTokenizer")
        .def(py::init<int>(), py::arg("n"))
        .def("tokenize", &NGramTokenizer::tokenize);

}
