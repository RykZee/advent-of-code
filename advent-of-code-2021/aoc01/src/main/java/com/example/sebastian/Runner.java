package com.example.sebastian;

import java.util.ArrayList;
import java.util.List;

public class Runner {
    private List<Integer> integers;

    public Runner(List<Integer> integers) {
        this.integers = integers;
    }

    public List<String> run() {
        List<String> result = new ArrayList<>();
        result.add("N/A - no previous measurement");
        for (int i = 1; i < integers.size(); i++) {
            int current = integers.get(i);
            int previous = integers.get(i-1);
            if(current > previous) {
                result.add("increased");
            } else if(current < previous) {
                result.add("decreased");
            } else {
                result.add("no change");
            }
        }
        return result;
    }

    public List<String> runSliding() {
        List<String> result = new ArrayList<>();
        result.add("N/A - no previous measurement");
        int previous = 0;
        for (int i = 0; i < integers.size(); i++) {
            if(i + 3 >= integers.size()) {
                break;
            }
            int current = integers.get(i) + integers.get(i+1) + integers.get(i+2);
            if(current > previous) {
                result.add("increased");
            } else if(current < previous) {
                result.add("decreased");
            } else {
                result.add("no change");
            }
            previous = current;
        }
        return result;
    }
}
