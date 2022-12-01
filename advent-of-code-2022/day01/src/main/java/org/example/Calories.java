package org.example;

import java.util.*;
import java.util.stream.Collectors;

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

    public List<Integer> getTopThreeMaxNrOfCalories(List<String> input) {
        List<Integer> sums = new ArrayList<>();
        int currentValue = 0;

        for (String s : input) {
            if ("".equals(s)) {
                sums.add(currentValue);
                currentValue = 0;
                continue;
            }

            currentValue += Integer.parseInt(s);
        }
        sums.add(currentValue);

        return sums.stream()
                .sorted(Collections.reverseOrder())
                .collect(Collectors.toList())
                .subList(0,3);
    }
}
