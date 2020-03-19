#include <iostream>
#include <new>
using namespace std;

// Stack
template <typename T>
class Stack {
  public:
    class Node;
  private:
    int size = 0;
    Node *head = NULL;
    Node *tail = NULL;
  public:
    // Node class
    class Node {
      public:
        T data;
        Node *next;
        // Constructor
        Node(T data = NULL, Node *next = NULL) {
          this->data = data;
          this->next = next;
        }
    };

    // Push an element to this Stack, O(1)
    void push(T elem) {
      if (size == 0) {
        head = tail = new Node(elem);
      } else {
        Node *temp = new Node(elem, head);
        head = temp;
      }
      size++;
    }

    // Pop an element from this Stack. O(1)
    void pop() {
      Node *temp = head;
      head = head->next;
      delete temp;
      size--;
    }

    // Check the value of the first node if it exists, O(1)
    T peekFirst() {
      try {if (size == 0) throw 101;} catch(...) {cout<<"Empty list";}
      return head.data;
    }

    // Find the index of a particular value in the linked list, O(n)
    int indexOf(T value) {
      int index = 0;
      Node *trav = head;
      for (; trav != NULL; trav = trav->next, index++) {
        if (value == trav->data) {
          return index;
        }
      }
      return -1;
    }

    // Check is a value is contained within the linked list
    bool contains(T value) {
      return indexOf(value) != -1;
    }

    // Print values in linked list
    void print() {
      Node *trav = head;
      while (trav != NULL) {
        cout<<trav->data<<" ";
        trav = trav->next;
      }
    }
};

int main()
{
  Stack<int> A;
  A.push(4);
  A.push(3);
  A.push(2);
  A.push(1);
  A.push(0);
  A.push(-1);
  A.pop();
  A.pop();
  A.print();
  return 0;
}
