package com.example.sebastian;

public class Result2 {

    private final int oxygenGeneratorRating;
    private final int CO2ScrubberRating;

    public Result2(int oxygenGeneratorRating, int CO2ScrubberRating) {
        this.oxygenGeneratorRating = oxygenGeneratorRating;
        this.CO2ScrubberRating = CO2ScrubberRating;
    }

    public int getOxygenGeneratorRating() {
        return oxygenGeneratorRating;
    }

    public int getCO2ScrubberRating() {
        return CO2ScrubberRating;
    }
}
