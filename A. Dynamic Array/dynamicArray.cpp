#include <iostream>
using namespace std;

template <typename T>

// Dynamic array class
class DynamicArray {
  public:
    int len = 0;
    T *arr;

    DynamicArray(int); // Size

    // Methods
    void add(T); // Element
    void removeAt(int); // Index
    bool remove(T); // Element

    int size();
    bool isEmpty();

    T get(int); // Index
    void set(int, T); // Index, Element

    void deleteArray();
  };

// Contructor
template <typename T>
DynamicArray<T>::DynamicArray(int size) {
  len = size;
  // Using malloc() function from <stdlib.h>
  arr = (T*) malloc(size * sizeof(T));
  if (!arr) cout<<"Illegal size: " + size<<endl;
}

// Add an element to this dynamic array
template <typename T>
void DynamicArray<T>::add(T element) {
  // Using realloc() function from <stdlib.h>
  arr = (T*) realloc(arr, (len + 1) * sizeof(T));
  arr[len] = element;
  len++;
}

// Removes the element at the specified index in this list.
// If possible, avoid calling this method as it take O(n) time
// to remove an element (since you have to reconstruct the array!)
template <typename T>
void DynamicArray<T>::removeAt(int rm_index) {
  T * temp = (T*) malloc(len * sizeof(T));
  for (int i = 0; i < rm_index; i++) temp[i] = arr[i];
  for (int i = rm_index + 1; i < size(); i++) temp[i - 1] = arr[i];
  arr = (T*) realloc(temp, (len - 1) * sizeof(T));
  --len;
}

// Search and remove an element if it is found in the array
// If possible, avoid calling this method as it take O(n) time
template <typename T>
bool DynamicArray<T>::remove(T elem) {
  for (int i = 0; i < len; i++) {
    if (arr[i] == elem) {
      removeAt(i);
      return true;
    }
  }
  return false;
}

// Returns the size of the array
template <typename T>
int DynamicArray<T>::size() {
  return len;
}

// Returns true/false on whether the array is empty
template <typename T>
bool DynamicArray<T>::isEmpty() {
  return len == 0;
}

// Get method for array
template <typename T>
T DynamicArray<T>::get(int index) {
  return arr[index];
}

// Set method for array
template <typename T>
void DynamicArray<T>::set(int index, T elem) {
  arr[index] = elem;
}

// Deleting array
template <typename T>
void DynamicArray<T>::deleteArray() {
  free(arr);
}

int main() {
  DynamicArray<int> ar(2);

  ar.set(1, 2);

  ar.add(3);
  ar.add(4);
  ar.add(5);

  ar.remove(4);

  // Print dynamic array
  for (int i = 0; i < ar.size(); i++) cout<<ar.get(i)<<" ";
  return 0;
}
