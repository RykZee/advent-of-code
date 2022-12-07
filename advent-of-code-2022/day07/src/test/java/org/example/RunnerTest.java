package org.example;

import junit.framework.TestCase;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class RunnerTest extends TestCase {
    private final List<String> EXAMPLE = Arrays.stream((
                    """
                    $ cd /
                    $ ls
                    dir a
                    14848514 b.txt
                    8504156 c.dat
                    dir d
                    $ cd a
                    $ ls
                    dir e
                    29116 f
                    2557 g
                    62596 h.lst
                    $ cd e
                    $ ls
                    584 i
                    $ cd ..
                    $ cd ..
                    $ cd d
                    $ ls
                    4060174 j
                    8033020 d.log
                    5626152 d.ext
                    7214296 k""")
                    .split("\n"))
            .toList();

    public void testGetSizeOfDirectoriesLessThanLimitExample() {
        int result = new Runner().getSizeOfDirectoriesLessThanLimit(EXAMPLE);
        assertEquals(95_437, result);
    }

    public void testGetSizeOfDirectoriesLessThanLimit() {
        List<String> input = readFile("input");
        int result = new Runner().getSizeOfDirectoriesLessThanLimit(input);
        assertEquals(1_334_506, result);
    }

    public void testGetSmallestDirectoryToDeleteExample() {
        Runner runner = new Runner();
        File result = runner.getSmallestDirectoryToDelete(EXAMPLE);
        assertEquals(24_933_642, result.getSize());
    }

    public void testgetSmallestDirectoryToDelete() {
        List<String> input = readFile("input");
        Runner runner = new Runner();
        File result = runner.getSmallestDirectoryToDelete(input);
        assertEquals(7_421_137, (int) result.getSize());
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
