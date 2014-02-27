package graphics;

import java.awt.event.*;
import javax.swing.*;
import javax.swing.border.LineBorder;
import java.awt.*;
import board.BoardLayout;
import javax.swing.JOptionPane;


public class TitleCheckers extends JFrame implements ActionListener  {

	private static JLabel title;
	private static JButton standard, custom;
	private static JPanel panel;
	private static Color bgColor; 
	private static GridBagConstraints gbc = new GridBagConstraints();
	private BoardLayout bl = new BoardLayout();
	

	private TitleCheckers() {

		super("Checkers");
		panel = new JPanel(new GridBagLayout());
		bgColor = Color.decode("#00FF59");

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(700, 500);
		setResizable(false);
	

		
		title = new JLabel("Welcome to Checkers");
		title.setFont(new Font("Tahoma", Font.BOLD, 36));
		title.setForeground(Color.WHITE);
		
		standard = new JButton("Play Standard Game");
		standard.setPreferredSize(new Dimension(200, 25));
		standard.setFont(new Font("Tahoma", Font.BOLD, 12));
		standard.setBackground(new Color(0, 146, 50));
		standard.setOpaque(true);
		standard.setBorderPainted(false);
		standard.setForeground(Color.WHITE);
		
		custom = new JButton("Play Custom Game");
		custom.setPreferredSize(new Dimension(200, 25));
		custom.setFont(new Font("Tahoma", Font.BOLD, 12));
		custom.setBackground(new Color(0, 146, 50));
		custom.setOpaque(true);
		custom.setBorderPainted(false);
		custom.setForeground(Color.WHITE);
		
		panel.setBackground(bgColor);

		gbc.insets = new Insets(15, 0, 0, 0); // spacing
		
		gbc.gridx = 1;
		gbc.gridy = 1;
	
		panel.add(title, gbc);
		
		gbc.gridy = 2;
		panel.add(standard, gbc);
		standard.addActionListener(this);
	
		
		gbc.gridy = 3;
		panel.add(custom, gbc);
		custom.addActionListener(this);
		


		this.setMinimumSize(new Dimension(700, 500));
		this.setContentPane(panel);
		this.setVisible(true);
		
	
	
	}

	public void actionPerformed(ActionEvent e) {

	if (e.getSource() == standard) {
	
		JOptionPane.showMessageDialog (null, "You have chosen a standard game!", "Standard Selected", JOptionPane.INFORMATION_MESSAGE);
		bl.Create_StandardBoard();
		
		
	}
	
	if (e.getSource() == custom) {
		
		JOptionPane.showMessageDialog (null, "You have chosen a custom game!", "Standard Selected", JOptionPane.INFORMATION_MESSAGE);
		bl.Create_CustomBoard();
		
	
	}

	

	}

	//main method 
	public static void main(String[] args) {

		//calls own classes constructor
		new TitleCheckers();
	}
}