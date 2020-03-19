#include <iostream>
#include <new>
#include <cmath>
using namespace std;

// Doubly linked list class
template <typename T>
class DoublyLinkedList {
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
        Node *prev;
        Node *next;
        // Constructor
        Node(T data = NULL, Node *prev = NULL, Node *next = NULL) {
          this->data = data;
          this->prev = prev;
          this->next = next;
        }
    };

    // Add a node to the tail of the linked list, O(1)
    void addToTail(T elem) {
      Node *temp = new Node(elem, tail);
      if (size == 0) {
        head = tail = temp;
      } else {
        tail->next = temp;
        tail = temp;
      }
      size++;
    }

    // Add an element to the beginning of this linked list, O(1)
    void addToHead(T elem) {
      Node *temp = new Node(elem, NULL, head);
      if (size == 0) {
        head = tail = temp;
      } else {
        head->prev = temp;
        head = temp;
      }
      size++;
    }

    // Check the value of the first node if it exists, O(1)
    T peekFirst() {
      try {if (size == 0) throw 101;} catch(...) {cout<<"Empty list";}
      return head.data;
    }

    // Check the value of the last node if it exists, O(1)
    T peekLast() {
      try {if (size == 0) throw 101;} catch(...) {cout<<"Empty list";}
      return tail.data;
    }

    // Remove a node at a particular index of doubly linked list, O(n)
    void removeAt(int index) {
      // Make sure the index provided is valid
      try {
        if (index < 0 || index >= size) throw 101;
      } catch(...) {
        cout<<"Invalid index";
      }

      Node *temp;
      if (index < floor(size / 2)) { // To get result faster.
        temp = head;
        for (int i = 0; i != index; i++) { // Search from the front of the list
          temp = temp->next;
        }
      } else {
        temp = tail;
        for (int i = size - 1; i != index; i--) { // Search from the back of the list
          temp = temp->prev;
        }
      }

      temp->prev->next = temp->next;
      temp->next->prev = temp->prev;
      delete temp;
      size--;
    }

    // Remove a particular value in the linked list, O(n)
    bool remove(T value) {
      // Search for value
      for (Node *temp = head; temp != NULL; temp = temp->next) {
        if (value == temp->data) {
          temp->prev->next = temp->next;
          temp->next->prev = temp->prev;
          delete temp;
          return true;
          size--;
        }
      }
      return false;
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
      cout<<endl;
    }
};

int main()
{
  DoublyLinkedList<int> A;

  A.addToTail(2);
  A.print();

  A.addToTail(3);
  A.print();

  A.addToTail(4);
  A.print();

  A.addToTail(5);
  A.print();

  A.addToTail(6);
  A.print();

  A.addToHead(1);
  A.print();

  A.removeAt(3);
  A.print();

  A.remove(5);
  A.print();

  return 0;
}
