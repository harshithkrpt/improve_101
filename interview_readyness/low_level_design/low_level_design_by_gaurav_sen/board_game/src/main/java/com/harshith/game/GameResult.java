package com.harshith.game;

public class GameResult {
    boolean isOver = false;
    String winner;

    public GameResult(boolean isOver, String winner) {
        this.isOver = isOver;
        this.winner = winner;
    }

    public boolean isOver() {
        return isOver;
    }
}
