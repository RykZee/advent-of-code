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

    public int getMaxNrOfCaloriesFunctional(List<String> input) {
        List<Integer> sums = new ArrayList<>();

        while (true) {
            if (input.isEmpty()) {
                break;
            } else if (input.size() == 1) {
                sums.add(Integer.parseInt(input.get(0)));
                break;
            }
            List<String> toSumUp = input
                    .stream()
                    .takeWhile(s -> !"".equals(s))
                    .toList();

            input = input.subList(toSumUp.size()+1, input.size());

            int sum = toSumUp
                    .stream()
                    .mapToInt(Integer::parseInt)
                    .sum();
            sums.add(sum);
        }
        return Collections.max(sums);
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
