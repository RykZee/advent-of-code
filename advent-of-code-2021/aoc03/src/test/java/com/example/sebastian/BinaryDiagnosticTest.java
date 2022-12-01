package com.example.sebastian;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * Unit test for simple App.
 */
public class BinaryDiagnosticTest extends TestCase {

    final List<String> EXAMPLE_NUMBERS = Arrays.stream((
            "00100\n" +
            "11110\n" +
            "10110\n" +
            "10111\n" +
            "10101\n" +
            "01111\n" +
            "00111\n" +
            "11100\n" +
            "10000\n" +
            "11001\n" +
            "00010\n" +
            "01010")
            .split("\n"))
            .toList();
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public BinaryDiagnosticTest(String testName) {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite() {
        return new TestSuite(BinaryDiagnosticTest.class);
    }

    public void testPowerConsumptionExample() {
        PowerConsumptionCalculator calculator = new PowerConsumptionCalculator();
        Result result = calculator.calculatePowerConsumption(EXAMPLE_NUMBERS);

        assertEquals(22, result.getGammaRate());
        assertEquals(9, result.getEpsilonRate());
    }

    public void testPowerConsumption() {
        List<String> input = readFile("input");

        PowerConsumptionCalculator calculator = new PowerConsumptionCalculator();
        Result result = calculator.calculatePowerConsumption(input);

        assertEquals(1616, result.getGammaRate());
        assertEquals(2479, result.getEpsilonRate());
        System.out.println("Multiplied " + result.getGammaRate() * result.getEpsilonRate());
    }

    public void testLifeSupportRatingExample() {
        PowerConsumptionCalculator calculator = new PowerConsumptionCalculator();
        Result2 result = calculator.calculateLifeSupportRating(EXAMPLE_NUMBERS);

        assertEquals(23, result.getOxygenGeneratorRating());
        assertEquals(10, result.getCO2ScrubberRating());
    }

    public void testLifeSupportRating() {
        List<String> input = readFile("input");
        PowerConsumptionCalculator calculator = new PowerConsumptionCalculator();
        Result2 result = calculator.calculateLifeSupportRating(input);

        assertEquals(1599, result.getOxygenGeneratorRating());
        assertEquals(3716, result.getCO2ScrubberRating());
        System.out.println("Multiplied: " + result.getOxygenGeneratorRating() * result.getCO2ScrubberRating());
    }

    private List<String> readFile(String filename) {
        List<String> input = new ArrayList<>();
        String path = "src/test/resources/" + filename;

        try (FileInputStream inputStream = new FileInputStream(path)) {
            Scanner scanner = new Scanner(inputStream);
            while (scanner.hasNextLine()) {
                input.add(scanner.nextLine());
            }
        } catch (IOException e) {
            System.err.println("Could not read from file " + path);
            System.exit(1);
        }
        return input;
    }
}
