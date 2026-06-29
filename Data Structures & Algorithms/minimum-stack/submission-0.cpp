class MinStack {
    stack<int> m_stack;
    stack<int> minStack;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        m_stack.push(val);
        val = min(val, minStack.empty() ? val : minStack.top());
        minStack.push(val);
    }
    
    void pop() {
        m_stack.pop();
        minStack.pop();
    }
    
    int top() {
        return m_stack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
