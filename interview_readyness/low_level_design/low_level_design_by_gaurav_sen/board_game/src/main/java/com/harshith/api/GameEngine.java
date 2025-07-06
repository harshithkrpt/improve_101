package com.harshith.api;

import com.harshith.boards.TicTacToeBoard;
import com.harshith.game.*;
import com.harshith.user.Player;

public class GameEngine {
    public final static String TicTacToe = "TicTacToe";

    public Board start(String type) {
        if(type.equals(GameEngine.TicTacToe)) {
            return new TicTacToeBoard();
        }
        else {
            throw new IllegalArgumentException();
        }
    }

    public void move(Board board, Player player, Move move) {
        if(board instanceof TicTacToeBoard) {
            TicTacToeBoard board1 = (TicTacToeBoard) board;
            board1.setCell(move.getCell(), player.symbol());
        }
        else {
            throw new IllegalArgumentException();
        }
    }

    public GameResult isComplete(Board board) {
        if (board instanceof TicTacToeBoard) {
            boolean rowComplete = false;
            boolean columnComplete = false;
            String firstCharacter = "-";
            TicTacToeBoard board1 = (TicTacToeBoard) board;
            // Row Complete
            for(int i=0;i<3;i++) {
                 rowComplete = board1.getCell(i,0) != null;
                 firstCharacter = board1.getCell(i,0);
                 for (int j=1;j<3;j++) {
                    if(board1.getCell(i,j) == null || !board1.getCell(i,j).equals(firstCharacter)) {
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
                columnComplete = board1.getCell(0,i) != null;
                firstCharacter = board1.getCell(0,i);
                for (int j=1;j<3;j++) {
                    if(board1.getCell(j,i) == null || !board1.getCell(j,i).equals(firstCharacter)) {
                        columnComplete = false;
                        break;
                    }
                }

                if(columnComplete) {
                    return new GameResult(rowComplete, firstCharacter);
                }
            }

            // Diagonal Complete
            boolean diagComplete = board1.getCell(0,0) != null;
            firstCharacter = board1.getCell(0,0);
            for(int i=0;i<3;i++) {
                if(board1.getCell(i,i) == null || !board1.getCell(i,i).equals(firstCharacter)) {
                    diagComplete  = false;
                    break;
                }
            }

            if(diagComplete) {
                return new GameResult(diagComplete, firstCharacter);
            }

            // Reverse Diagnoal Complete
            boolean revDiagonalComplete = board1.getCell(0,2) != null;
            firstCharacter = board1.getCell(0,2);
            for(int i=0;i<3;i++) {
                if(board1.getCell(i,2-i) == null || !board1.getCell(i,2-i).equals(firstCharacter)) {
                    revDiagonalComplete = false;
                    break;
                }
            }

            if(revDiagonalComplete) {
                return new GameResult(revDiagonalComplete, firstCharacter);
            }

            int countOfFilledCells = 0;
            for(int i=0;i<3;i++) {
                for(int j=0;j<3;j++) {
                    if(board1.getCell(i, j) != null) {
                        countOfFilledCells++;
                    }
                }
            }

            if(countOfFilledCells == 9) {
                return new GameResult(true, "-");
            }
            else {
                return new GameResult(false, "-");
            }
        }


        return new GameResult(false, "-");
    }

    public Move suggestMove(Player player, Board board) {
        if(board instanceof TicTacToeBoard) {
            TicTacToeBoard board1 = (TicTacToeBoard) board;
            for(int i=0;i<3;i++) {
                for(int j=0;j<3;j++) {
                    if(board1.getCell(i,j) != null) {
                        return new Move(new Cell(i, j));
                    }
                }
            }

            throw new IllegalStateException();
        }
        else {
            throw new IllegalArgumentException();
        }
    }
}