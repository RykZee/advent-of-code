package org.example;
import java.util.HashSet;
import java.util.Set;

public class File {
    private final String name;
    private final FileType fileType;
    private Set<File> children = new HashSet<>();
    private final File parent;
    private final int size;

    public String getName() {
        return name;
    }

    public File(String name, FileType fileType, File parent) {
        this(name, fileType, parent, 0);
    }

    public File(String name, FileType fileType, File parent, int size) {
        this.name = name;
        this.fileType = fileType;
        this.parent = parent;
        this.size = size;
    }

    public FileType getFileType() {
        return fileType;
    }

    public Set<File> getChildren() {
        return children;
    }

    public void addChild(File child) {
        this.children.add(child);
    }

    public File getParent() {
        return parent;
    }

    public int getSize() {
        if (fileType == FileType.FILE) {
            return size;
        }
        int childSize = 0;
        for (File child : children) {
            childSize += child.getSize();
        }
        return childSize;
    }
}
