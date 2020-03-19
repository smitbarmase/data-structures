#include <iostream>
#include <new>
using namespace std;

// Queue class
template <typename T>
class Queue {
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

    // Enqueue an element in queue. Adding element to the tail. O(1)
    void enqueue(T elem) {
      if (size == 0) {
        head = tail = new Node(elem);
      } else {
        Node *temp = new Node(elem);
        tail->next = temp;
        tail = temp;
      }
      size++;
    }

    // Dequeue an element in queue. Removing head. O(1)
    void dequeue() {
      Node *temp = head;
      head = head->next;
      delete temp;
      size--;
    }

    // Check the value of the last node if it exists, O(1)
    T peekLast() {
      try {if (size == 0) throw 101;} catch(...) {cout<<"Empty list";}
      return tail.data;
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
  Queue<int> A;
  A.enqueue(-1);
  A.enqueue(0);
  A.enqueue(1);
  A.enqueue(2);
  A.enqueue(3);
  A.enqueue(4);
  A.dequeue();
  A.dequeue();
  A.print();
  return 0;
}
