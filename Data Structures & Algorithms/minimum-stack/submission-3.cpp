class MinStack {
    stack<long> m_stack;
    long min;
public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (m_stack.empty())
        {
            m_stack.push(0);
            min = val;
        }
        else
        {
            m_stack.push(val-min);
            if (val < min) min = val;
        }
    }
    
    void pop() {
        if (m_stack.empty()) return;
        long pop = m_stack.top();
        m_stack.pop();
        if (pop < 0) min = min - pop;
    }
    
    int top() {
        long top = m_stack.top();
        return (top > 0) ? (top + min) : (int)min;
    }
    
    int getMin() {
        return min;
    }
};
