package board;

import interfaces.BoardLayoutInterface;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.border.LineBorder;
import java.awt.*;


public class BoardLayout implements BoardLayoutInterface, ActionListener{
	
	private String board[][] = new String[8][8];
	

	
	
		private static void main(String[] args) {
		
		BoardLayout hey = new BoardLayout();
		hey.Create_StandardBoard();
		
	}
	
	
	public void Create_CustomBoard() {
		
	
	}

	public void Create_StandardBoard() {
		
		int x = 0;
		
		for (int col = 0; col < board.length; col++) {
			for (int row = 0; row < board.length; row++) {
				
			if (x % 2 != 0){
				board[row][col] = "B"; 
			}
			
			x++;
				
			
			}
		}
		
		
		 
		
		
		
		

	}

	public void Finish_CustomBoard() {
		// TODO Auto-generated method stub

	}
	
	public void actionPerformed(ActionEvent e) {

		

		

		}
	
	
	

}
