package com.harshith.game;

public class Cell {
    private int row, col;

    public Cell(int row, int col) {
        this.col = col;
        this.row = row;
    }

    public int getRow() {
        return this.row;
    }

    public int getCol() {
        return this.col;
    }
}
