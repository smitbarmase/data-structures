#include <iostream>
#include <new>
using namespace std;

// Singly linked list class
template <typename T>
class SinglyLinkedList {
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

    // Add a node to the tail of the linked list, O(1)
    void add(T elem) {
      Node *temp = new Node(elem);
      if (size == 0) {
        head = tail = temp;
      } else {
        tail->next = temp;
        tail = tail->next;
      }
      size++;
    }

    // Add an element to the beginning of this linked list, O(1)
    void addFirst(T elem) {
      if (size == 0) {
        head = tail = new Node(elem);
      } else {
        Node *temp = new Node(elem, head);
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

    // Remove a node at a particular index, O(n)
    void removeAt(int index) {
      // Make sure the index provided is valid
      try {
        if (index < 0 || index >= size) {
          throw 101;
        }
      } catch(...) {
        cout<<"Invalid index";
      }

      Node *temp = head;
      if (index == 0) {
        head = head->next;
        delete temp;
      }
      else
      {
        // Search from the front of the list
        for (int i = 1; i != index; i++) {
          temp = temp->next;
        }
        Node *toDelete = temp->next;
        temp->next = toDelete->next;
        delete toDelete;
      }
      size--;
    }

    // Remove a particular value in the linked list, O(n)
    bool remove(T value) {
      Node *temp = head;
      if (head->data == value) {
        head = head->next;
        delete temp;
        size--;
        return true;
      }
      else
      {
        // Search for value
        for (; temp->next != NULL; temp = temp->next) {
          if (value == temp->next->data) {
            Node *nextNode = temp->next->next;
            delete temp->next;
            temp->next = nextNode;
            size--;
            return true;
          }
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
    }
};

int main()
{
  SinglyLinkedList<int> A;
  A.add(1);
  A.add(2);
  A.add(3);
  A.add(4);
  A.add(5);
  A.add(6);
  A.removeAt(0);
  A.removeAt(1);
  A.remove(5);
  A.print();
  return 0;
}
