#ifndef INCLUDE_CUT_H
#define INCLUDE_CUT_H
#include <vector>

typedef bool (*CutFunction)(double *, std::vector<int>&);

class Cut{
    public:
        Cut(){};
        Cut(std::vector<int>,CutFunction);
        ~Cut(){};
        bool operator()(double *);
    private:
        std::vector<int> _array_ids;
        CutFunction _cut_function;
};
#endif // INCLUDE_CUT_H
