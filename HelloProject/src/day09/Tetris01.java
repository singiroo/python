package day09;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.Color;
import javax.swing.JButton;
import java.awt.Label;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

/**
 * 테트리스
 * @author PC-25
 *
 */
public class Tetris01 extends JFrame {

	private JPanel contentPane;
	private final int BLOCK_SPEED = 25;		//블록의 이동하는 속도(이동 정도)
	private JLabel lbl = new JLabel("");

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Tetris01 frame = new Tetris01();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Tetris01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 453, 682);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl.setOpaque(true);			//라벨의 불투명도 설정(true : 불투명)
		lbl.setBackground(Color.ORANGE);
		lbl.setBounds(48, 24, 25, 25);
		contentPane.add(lbl);
		addKeyListener(new KeyAdapter() {		//키 입력 이벤트 설정
			@Override
			public void keyPressed(KeyEvent e) {	// 방향키를 입력하여 해당 방향으로 블록이 움직임.
				if(e.getKeyCode() == KeyEvent.VK_LEFT) {
					lbl.setLocation(lbl.getX()-BLOCK_SPEED, lbl.getY());
				}
				if(e.getKeyCode() == KeyEvent.VK_RIGHT) {
					lbl.setLocation(lbl.getX()+BLOCK_SPEED, lbl.getY());
				}
				if(e.getKeyCode() == KeyEvent.VK_DOWN) {
					lbl.setLocation(lbl.getX(), lbl.getY()+BLOCK_SPEED);
				}
				if(e.getKeyCode() == KeyEvent.VK_UP) {
					lbl.setLocation(lbl.getX(), lbl.getY()-BLOCK_SPEED);
				}
				
			}
		});
	}
}
