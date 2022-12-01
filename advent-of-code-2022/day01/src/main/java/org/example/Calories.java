package org.example;

import java.util.*;

public class Calories {

    public int getMaxNrOfCalories(List<String> input) {
        int max = 0;
        int current = 0;
        for (String s : input) {
            if ("".equals(s)) {
                current = 0;
                continue;
            }

            current += Integer.parseInt(s);
            if (current > max) {
                max = current;
            }
        }
        return max;
    }
}
