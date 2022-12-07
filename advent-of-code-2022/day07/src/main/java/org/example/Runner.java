package org.example;

import java.util.ArrayList;
import java.util.List;

public class Runner {
    public int getSizeOfDirectoriesLessThanLimit(List<String> input) {
        File root = buildFileTree(input);
        return getSizeOfDirectoriesLessThanLimit(root)
                .stream()
                .mapToInt(File::getSize)
                .sum();
    }

    public File getSmallestDirectoryToDelete(List<String> inputs) {
        File root = buildFileTree(inputs);
        int target = 30_000_000 - (70_000_000 - root.getSize());
        return getSmallestDirectoryToDelete(root, target);
    }

    private File buildFileTree(List<String> inputs) {
        File root = null;
        File current = null;
        for (String input : inputs) {
            String[] splitInput = input.split(" ");
            if (splitInput[0].equals("$")) {
                if (splitInput[1].equals("cd")) {
                    if (splitInput[2].equals("/")) {
                        root = new File("/", FileType.DIRECTORY, null);
                        current = root;
                    } else if (splitInput[2].equals("..")) {
                        current = current.getParent();
                    } else {
                        current = current
                                .getChildren()
                                .stream()
                                .filter(f -> f.getName().equals(splitInput[2]))
                                .findFirst()
                                .orElseThrow();
                    }
                }
            } else { // read output from ls
                File file;
                if (splitInput[0].equals("dir")) {
                    file = new File(splitInput[1], FileType.DIRECTORY, current);
                } else {
                    file = new File(splitInput[1], FileType.FILE, current, Integer.parseInt(splitInput[0]));
                }
                current.addChild(file);
            }
        }
        return root;
    }

    private File getSmallestDirectoryToDelete(File node, int target) {
        File smallestDirectoryToDelete = null;
        if (node.getFileType() == FileType.DIRECTORY && node.getSize() >= target) {
            smallestDirectoryToDelete = node;
        }
        for (File child : node.getChildren()) {
            if (child.getFileType() == FileType.DIRECTORY && !child.getChildren().isEmpty()) {
                File found = getSmallestDirectoryToDelete(child, target);
                if (found != null && found.getSize() < smallestDirectoryToDelete.getSize()) {
                    smallestDirectoryToDelete = found;
                }
            }
        }
        return smallestDirectoryToDelete;
    }

    private List<File> getSizeOfDirectoriesLessThanLimit(File root) {
        List<File> allFoundDirectories = new ArrayList<>();
        if (root.getFileType() == FileType.DIRECTORY && root.getSize() <= 100_000) {
            allFoundDirectories.add(root);
        }
        for (File child : root.getChildren()) {
            if (child.getFileType() == FileType.DIRECTORY && !child.getChildren().isEmpty()) {
                List<File> childFound = getSizeOfDirectoriesLessThanLimit(child);
                allFoundDirectories.addAll(childFound);
            }
        }
        return allFoundDirectories;
    }
}
