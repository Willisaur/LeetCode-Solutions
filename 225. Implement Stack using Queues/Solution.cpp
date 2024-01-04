class MyStack {
public:
    queue<int> s; 

    MyStack() {}
    
    void push(int x) {
        s.push(x);
    }
    
    int pop() {
        for (int i = s.size()-1; i>0; --i){ // rotate the queue until element to-be-popped is at the front
            s.push(s.front());
            s.pop();
        }
        int temp = s.front();
        s.pop();
        return temp;
    }
    
    int top() {
        for (int i = s.size()-1; i>0; --i){ // rotate the queue until element to-be-peeked is at the front
            s.push(s.front());
            s.pop();
        }
        int temp = s.front();
        s.pop();
        s.push(temp); // put it back in the queue
        return temp;
    }
    
    bool empty() {
        return s.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */