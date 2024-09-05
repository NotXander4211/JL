package helper;

import java.util.ArrayList;

public class Stack {
    private int pt = 0;
    private ArrayList<Integer> buf = new ArrayList<>();
    public Stack(int size){
        for (int i = 0;i < size;i++){
            buf.add(0);
        }
    }

    public void push(int value){
        pt++;
        buf.add(pt, value);
    }

    public int pop(){
        int number = buf.get(pt);
        pt--;
        return number;
    }

    public int top(){
        return buf.get(pt);
    }
}
