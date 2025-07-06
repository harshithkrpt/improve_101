package com.harshith;

import com.harshith.api.GameEngine;
import com.harshith.game.Board;
import com.harshith.game.Cell;
import com.harshith.game.Move;
import com.harshith.user.Player;

import java.util.Scanner;

public class Main {
    public static void main(String [] args) {
        GameEngine gameEngine = new GameEngine();
        Board board = gameEngine.start(GameEngine.TicTacToe);
        Scanner scanner = new Scanner(System.in);
        while(gameEngine.isComplete(board).isOver()) {
            System.out.println("Make your Move : ");
            Player computer = new Player("O");
            Player opponent = new Player("X");
            int row = scanner.nextInt();
            int col = scanner.nextInt();
            Move oppMove = new Move(new Cell(row, col));
            gameEngine.move(board, opponent, oppMove);
            if(!gameEngine.isComplete(board).isOver()) {
                Move computerMove = gameEngine.suggestMove(computer, board);
                gameEngine.move(board, computer, computerMove);
            }
        }
    }
}
