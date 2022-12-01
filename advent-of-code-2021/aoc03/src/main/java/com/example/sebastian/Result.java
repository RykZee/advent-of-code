package com.example.sebastian;

public class Result {
    private final int gammaRate;
    private final int epsilonRate;

    public Result(int gammaRate, int epsilonRate) {
        this.gammaRate = gammaRate;
        this.epsilonRate = epsilonRate;
    }

    public int getGammaRate() {
        return gammaRate;
    }

    public int getEpsilonRate() {
        return epsilonRate;
    }
}
