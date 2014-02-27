package board;

import interfaces.BoardLayoutInterface;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.border.LineBorder;
import java.awt.*;

public class BoardLayout extends JFrame implements BoardLayoutInterface,
		ActionListener {

	private String board[][] = new String[8][8];
	private JButton[] blackButtons = new JButton[32];
	private JButton[] whiteButtons = new JButton[32];
	private JPanel customPanel;
	private int x, y = 0;

	private static void main(String[] args) {

		BoardLayout hey = new BoardLayout();
		hey.Create_StandardBoard();

	}

	public void Create_CustomBoard() {

		for (int i = 0; i < blackButtons.length; i++) {
			blackButtons[i] = new JButton("B");
			blackButtons[i].setBackground(Color.BLACK);
		}
		for (int i = 0; i < whiteButtons.length; i++) {
			whiteButtons[i] = new JButton("W");
			whiteButtons[i].setBackground(Color.WHITE);
		}

		customPanel = new JPanel();
		customPanel.setLayout(new GridLayout(8, 8));
		customPanel.setSize(600, 600);

		for (int i = 0; i < 8; i++) {
			if (i % 2 == 0) {
				for (int j = 0; j < 4; j++) {
					customPanel.add(blackButtons[4 * i + j]);
					customPanel.add(whiteButtons[4 * i + j]);
				}
			} else {
				for (int j = 0; j < 4; j++) {
					customPanel.add(whiteButtons[4 * i + j]);
					customPanel.add(blackButtons[4 * i + j]);
				}
			}
		}

	}

	public void Create_StandardBoard() {

		for (int row = 0; row < 2; row++) {
			for (int col = 0; col < board.length; col++) {

				if (x % 2 == 0) {
					board[row][col] = "W";
				}

				x++;

			}
		}
		for (int row = 5; row < board.length; row++) {
			for (int col = 0; col < board.length; col++) {

				if (y % 2 != 0) {
					board[row][col] = "B";
				}

				y++;

			}
		}

	}

	
	
	public void Finish_CustomBoard() {
		// TODO Auto-generated method stub

	}

	public void actionPerformed(ActionEvent e) {

	}

}
