package com.example.sebastian;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class PowerConsumptionCalculator {
    public PowerConsumptionCalculator() {
    }

    public Result calculatePowerConsumption(List<String> input) {
        StringBuilder gammaBuilder = new StringBuilder();
        StringBuilder epsilonBuilder = new StringBuilder();

        for (int col = 0; col < input.get(0).length(); col++) {
            OnesAndZeroes onesAndZeroes = findNumberOfOnesAndZeroes(input, col);

            boolean hasMoreOnes = onesAndZeroes.numberOfOnes > onesAndZeroes.numberOfZeroes;
            char gammaValue = hasMoreOnes ? '1' : '0';
            char epsilonValue = !hasMoreOnes ? '1' : '0';
            gammaBuilder.append(gammaValue);
            epsilonBuilder.append(epsilonValue);
        }

        int gammaDecimalValue = Integer.parseInt(gammaBuilder.toString(), 2);
        int epsilonDecimalValue = Integer.parseInt(epsilonBuilder.toString(), 2);

        return new Result(gammaDecimalValue,epsilonDecimalValue);
    }

    public Result2 calculateLifeSupportRating(List<String> input) {
        List<String> remainingOxygenNumbers = new ArrayList<>(input);
        List<String> remainingCO2Numbers = new ArrayList<>(input);
        for (int col = 0; col < input.get(0).length(); col++) {
            OnesAndZeroes onesAndZeroes = findNumberOfOnesAndZeroes(remainingOxygenNumbers, col);
            OnesAndZeroes co2OnesAndZeroes = findNumberOfOnesAndZeroes(remainingCO2Numbers, col);

            int finalCol = col;
            if (remainingOxygenNumbers.size() > 1) {
                remainingOxygenNumbers = remainingOxygenNumbers
                        .stream()
                        .filter(s -> {
                            if (onesAndZeroes.numberOfOnes >= onesAndZeroes.numberOfZeroes) {
                                return s.charAt(finalCol) == '1';
                            } else {
                                return s.charAt(finalCol) == '0';
                            }
                        })
                        .collect(Collectors.toList());
            }
            if (remainingCO2Numbers.size() > 1) {
            remainingCO2Numbers = remainingCO2Numbers
                    .stream()
                    .filter(s -> {
                        if (co2OnesAndZeroes.numberOfZeroes <= co2OnesAndZeroes.numberOfOnes) {
                            return s.charAt(finalCol) == '0';
                        } else {
                            return s.charAt(finalCol) == '1';
                        }
                    })
                    .collect(Collectors.toList());
            }
        }

        int oxygenGeneratorRating;
        if (remainingOxygenNumbers.size() == 2) {
            oxygenGeneratorRating = Integer.parseInt(remainingOxygenNumbers
                    .stream()
                    .filter(s -> s.charAt(s.length() - 1) == '1')
                    .findFirst()
                    .orElseThrow(),2);
        } else {
            oxygenGeneratorRating = Integer.parseInt(remainingOxygenNumbers
                    .stream()
                    .findFirst()
                    .orElseThrow(), 2);
        }

        int CO2ScrubberRating;
        if (remainingOxygenNumbers.size() == 2) {
            CO2ScrubberRating = Integer.parseInt(remainingCO2Numbers
                    .stream()
                    .filter(s -> s.charAt(s.length() - 1) == '0')
                    .findFirst()
                    .orElseThrow(), 2);
        } else {
            CO2ScrubberRating = Integer.parseInt(remainingCO2Numbers
                    .stream()
                    .findFirst()
                    .orElseThrow(), 2);
        }

        return new Result2(oxygenGeneratorRating, CO2ScrubberRating);
    }

    private OnesAndZeroes findNumberOfOnesAndZeroes(List<String> input, int column) {
        int numberOfOnes = 0;
        int numberOfZeroes = 0;
        for (String number : input) {
            if (number.charAt(column) == '1') {
                numberOfOnes++;
            } else if (number.charAt(column) == '0') {
                numberOfZeroes++;
            }
        }
        return new OnesAndZeroes(numberOfOnes, numberOfZeroes);
    }
}
