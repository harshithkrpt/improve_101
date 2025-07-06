package com.harshith;

public class Main {
    public static void main(String[] args) {

    }

    public Board start() {
        return new Board();
    }

    public void move(Board board, Player player, Move move) {

    }

    public GameResult isComplete(Board board) {
        if (board instanceof TicTacToeBoard) {
            boolean rowComplete = false;
            boolean columnComplete = false;
            String firstCharacter = "-";
            TicTacToeBoard board1 = (TicTacToeBoard) board;
            // Row Complete
            for(int i=0;i<3;i++) {
                 rowComplete = board1.cells[i][0] != null;
                 firstCharacter = board1.cells[i][0];
                for (int j=1;j<3;j++) {
                    if(board1.cells[i][j] == null || !board1.cells[i][j].equals(firstCharacter)) {
                        rowComplete = false;
                        break;
                    }
                }

                if(rowComplete) {
                    return new GameResult(rowComplete, firstCharacter);
                }
            }

            // Column Complete
            for(int i=0;i<3;i++) {
                columnComplete = board1.cells[0][i] != null;
                firstCharacter = board1.cells[0][i];
                for (int j=1;j<3;j++) {
                    if(board1.cells[j][i] == null || !board1.cells[j][i].equals(firstCharacter)) {
                        columnComplete = false;
                        break;
                    }
                }

                if(columnComplete) {
                    return new GameResult(rowComplete, firstCharacter);
                }
            }

            // Diagonal Complete
            boolean diagComplete = board1.cells[0][0] != null;
            firstCharacter = board1.cells[0][0];
            for(int i=0;i<3;i++) {
                if(board1.cells[i][i] == null || !board1.cells[i][i].equals(firstCharacter)) {
                    diagComplete  = false;
                    break;
                }
            }

            if(diagComplete) {
                return new GameResult(diagComplete, firstCharacter);
            }

            // Reverse Diagnoal Complete
            boolean revDiagonalComplete = board1.cells[0][2] != null;
            firstCharacter = board1.cells[0][2];
            for(int i=0;i<3;i++) {
                if(board1.cells[i][2-i] == null || !board1.cells[i][2-i].equals(firstCharacter)) {
                    revDiagonalComplete = false;
                    break;
                }
            }

            if(revDiagonalComplete) {
                return new GameResult(revDiagonalComplete, firstCharacter);
            }
        }


        return new GameResult(false, "-");
    }
}