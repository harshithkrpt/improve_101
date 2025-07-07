package com.harshith.boards;

import com.harshith.game.Board;
import com.harshith.game.Cell;
public class TicTacToeBoard extends Board {
    String cells[][] = new String[3][3];


    public String getCell(int row, int column) {
        return this.cells[row][column];
    }

    public void setCell(Cell cell, String symbol) {
        cells[cell.getRow()][cell.getCol()] = symbol;
    }

    @Override
    public String toString() {
        String res = "";
        for(int i=0;i<3;i++) {
            for(int j=0;j<3;j++) {
                if(cells[i][j] != null) {
                    res += cells[i][j] + " ";
                }
                else {
                    res += "- ";
                }
            }
            res += "\n";
        }

        return res;
    }
}
