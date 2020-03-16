#include <iostream>
#include <new>
using namespace std;

// Dynamic integer array class
class IntArray {
  int capacity = 0;
  public:
    int len = 0;
    int *arr;

    IntArray(int);

    void add(int);
    void removeAt(int);
    bool remove(int);

    int size();
    bool isEmpty();

    int get(int);
    void set(int, int);

    void deleteArray();
  };

// Contructor
IntArray::IntArray(int size) {
  capacity = len = size;
  arr = new(nothrow) int[size];
  if (!arr) cout<<"Illegal size: " + size<<endl;
}

// Add an element to this dynamic array
void IntArray::add(int element) {
  if (len + 1 >= capacity) {
    if (capacity == 0) capacity = 1;
    else capacity *= 2; // Double the size
    int * temp = new int[capacity]; // Temporary array of double the size
    for (int i = 0; i < size(); i++) temp[i] = arr[i]; // Assign all values
    arr = temp; // Set temporary array to original array
  }
  arr[len++] = element;
}

// Removes the element at the specified index in this list.
// If possible, avoid calling this method as it take O(n) time
// to remove an element (since you have to reconstruct the array!)
void IntArray::removeAt(int rm_index) {
  int * temp = new int[capacity]; // Temporary array of double the size
  for (int i = 0; i < rm_index; i++) temp[i] = arr[i]; // Assign all values
  for (int i = rm_index + 1; i < size(); i++) temp[i - 1] = arr[i]; // Assign all values
  arr = temp; // Set temporary array to original array
  --len;
  --capacity;
}

// Search and remove an element if it is found in the array
// If possible, avoid calling this method as it take O(n) time
bool IntArray::remove(int elem) {
  for (int i = 0; i < len; i++) {
    if (arr[i] == elem) {
      removeAt(i);
      return true;
    }
  }
  return false;
}

// Returns the size of the array
int IntArray::size() {
  return len;
}

// Returns true/false on whether the array is empty
bool IntArray::isEmpty() {
  return len == 0;
}

// Get method for array
int IntArray::get(int index) {
  return arr[index];
}

// Set method for array
void IntArray::set(int index, int elem) {
  arr[index] = elem;
}

// Deleting array
void IntArray::deleteArray() {
  delete[] arr;
}

int main() {
  IntArray ar(2);

  ar.set(0, 1);
  ar.set(1, 2);

  ar.add(5);
  ar.add(3);
  ar.add(4);

  ar.remove(5);

  // Print dynamic array
  for (int i = 0; i < ar.size(); i++) cout<<ar.get(i)<<" ";
  return 0;
}
