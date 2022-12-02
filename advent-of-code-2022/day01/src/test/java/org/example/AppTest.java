package org.example;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

/**
 * Unit test for simple App.
 */
public class AppTest 
    extends TestCase
{
    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTest( String testName )
    {
        super( testName );
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite()
    {
        return new TestSuite( AppTest.class );
    }

    /**
     * Rigourous Test :-)
     */
    public void testGetMaxNrOfCaloriesExample() {
        List<String> input = Arrays.stream((
                "1000\n" +
                "2000\n" +
                "3000\n" +
                "\n" +
                "4000\n" +
                "\n" +
                "5000\n" +
                "6000\n" +
                "\n" +
                "7000\n" +
                "8000\n" +
                "9000\n" +
                "\n" +
                "10000").split("\n"))
                .toList();

        Calories calories = new Calories();
         assertEquals(24000, calories.getMaxNrOfCalories(input));
    }

    public void testGetMaxNrOfCaloriesFunctionalExample() {
        List<String> input = Arrays.stream((
                "1000\n" +
                "2000\n" +
                "3000\n" +
                "\n" +
                "4000\n" +
                "\n" +
                "5000\n" +
                "6000\n" +
                "\n" +
                "7000\n" +
                "8000\n" +
                "9000\n" +
                "\n" +
                "10000").split("\n"))
                .toList();

        Calories calories = new Calories();
        assertEquals(24000, calories.getMaxNrOfCaloriesFunctional(input));
    }

    public void testGetMaxNrOfCalories() {
        List<String> input = readFile("input");

        Calories calories = new Calories();
        System.out.println("Max nr of calories: " + calories.getMaxNrOfCalories(input));
    }

    public void testGetTopThreeMaxNrOfCaloriesExample() {
        List<String> input = Arrays.stream((
                "1000\n" +
                "2000\n" +
                "3000\n" +
                "\n" +
                "4000\n" +
                "\n" +
                "5000\n" +
                "6000\n" +
                "\n" +
                "7000\n" +
                "8000\n" +
                "9000\n" +
                "\n" +
                "10000").split("\n"))
                .toList();

        Calories calories = new Calories();
        List<Integer> result = calories.getTopThreeMaxNrOfCalories(input);
        int first, second, third;
        first = result.get(0);
        second = result.get(1);
        third = result.get(2);

        assertEquals(24_000, first);
        assertEquals(11_000, second);
        assertEquals(10_000, third);
    }

    public void testGetTopThreeMaxNrOfCalories() {
        List<String> input = readFile("input");

        Calories calories = new Calories();
        List<Integer> result = calories.getTopThreeMaxNrOfCalories(input);
        int first, second, third;
        first = result.get(0);
        second = result.get(1);
        third = result.get(2);

        assertEquals(70_613, first);
        assertEquals(68_330, second);
        assertEquals(66_862, third);
        assertEquals(205_805, first + second, third);
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
