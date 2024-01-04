class MyQueue {
public:
    #include <stack>
    stack<int> s; 
    stack<int> t; // used for pop storage
    MyQueue() {
        
    }
    
    void push(int x) {
        while (!t.empty()){
            s.push(t.top());
            t.pop();
        }
        s.push(x);
    }
    
    int pop() {
        while (!s.empty()){
            t.push(s.top());
            s.pop();
        }
        int temp = t.top();
        t.pop();
        return temp;
    }
    
    int peek() {
        while (!s.empty()){
            t.push(s.top());
            s.pop();
        }
        return t.top();
    }
    
    bool empty() {
        return s.empty() && t.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */