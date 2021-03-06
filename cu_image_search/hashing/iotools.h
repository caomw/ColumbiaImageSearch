#ifndef HASHIOTOOLS_H
#define HASHIOTOOLS_H

#include <fstream>
#include <math.h>
#include <vector>
#include <iostream>
#include <sstream>

using namespace std;

// This is in header
extern string update_files_list;
extern string update_hash_prefix;
extern string update_feature_prefix;
extern string update_compfeature_prefix;
extern string update_compidx_prefix;

// Compression functions
int compress_onefeat(char * in, char * comp, int fsize);
int decompress_onefeat(char * in, char * comp, int compsize, int fsize);

// File reading functions
std::ifstream::pos_type filesize(std::string filename);
int get_file_pos(int * accum, int nb_files, int query, int & res);

// Getting one features from the binary files
int get_onefeatcomp(int query_ids, size_t read_size, int* accum, vector<ifstream*>& read_in_compfeatures, vector<ifstream*>& read_in_compidx, char* feature_cp);
int get_onesample(int query_ids, size_t read_size, int* accum, vector<ifstream*>& read_in, char* cp);
//int get_onefeat(int query_ids, size_t read_size, int* accum, vector<ifstream*>& read_in_features, char* feature_cp);

void fill_accum(vector<unsigned long long int>& data_nums,int * accum);
unsigned long long int fill_data_nums(vector<string>& update_hash_files, vector<unsigned long long int>& data_nums, int bit_num);
int fill_vector_files(vector<ifstream*>& read_in, vector<string>& update_files);

int get_n_features(string udpate_fn, int* query_ids, int query_num, int norm, int bit_num, size_t read_size, char* feature_cp);
int get_n_hashcodes(string udpate_fn, int* query_ids, int query_num, int norm, int bit_num, size_t read_size, char* hashcode_cp);

// Template functions have to be declared in header
template<class ty>
// L2 normalization of features
void normalize(ty *X, size_t dim)
{
    ty sum = 0;
    for (int i=0;i<dim;i++)
    {
        sum +=X[i]*X[i];
    }
    sum = sqrt(sum);
    ty n = 1 / sum;
    for (int i=0;i<dim;i++)
    {
        X[i] *= n;
    }
}

// because to_string is not available on Mac OS X?
template <typename T>
std::string to_string(T value)
{
  //create an output string stream
  std::ostringstream os ;

  //throw the value into the string stream
  os << value ;

  //convert the string stream into a string and return
  return os.str() ;
}

#endif