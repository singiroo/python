package day09;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.Graphics2D;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.Color;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Tetris02 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl;
	private JLabel[][] lblArray2d = new JLabel[20][10]; // 전체 게임판
	public Block block = new Block(); 				//블록 객체
	
	public int[][] block2D = new int[20][10];		//내려오는 블록의 배열
	public int[][] stack2D = new int[20][10];		//아래에 쌓여있는 블록의 배열
	public int[][] scrin2D = new int[20][10];		//게임 진행 화면의 배열
	

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Tetris02 frame = new Tetris02();
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
	public Tetris02() {
		addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				myPress(e);				//키보드 이벤트를 메서드로 정의
			}
		});
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 270, 600);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		setBlock2DWithBlock();
		
		
		stack2D[19][0] = 11;
		stack2D[19][1] = 11;
		stack2D[19][2] = 11;
		stack2D[19][3] = 11;
		
		//전체 게임판 생성
		for(int i=0;i<lblArray2d.length;i++) {
			for(int j=0;j<lblArray2d[i].length;j++) {
				lbl = new JLabel("");
				lbl.setOpaque(true);
				lbl.setBackground(Color.DARK_GRAY);
				lbl.setBounds(25*j ,25*i, 24, 24);
				lblArray2d[i][j] = lbl;
				contentPane.add(lblArray2d[i][j]);
			}
		}
		
		System.out.println(block);
		printBlock2D();
		printStack2D();
	}
	
	/**
	 * 방향키 입력시 블록이 움직이는 메서드
	 * @param e		키입력 이벤트
	 */
	public void myPress(KeyEvent e) {
		if(e.getKeyCode() == KeyEvent.VK_LEFT) {
			block.j--;
		}
		if(e.getKeyCode() == KeyEvent.VK_RIGHT) {
			block.j++;
		}
		if(e.getKeyCode() == KeyEvent.VK_DOWN) {
			block.i++;
		}
		if(e.getKeyCode() == KeyEvent.VK_UP) {
		}
		
		setBlock2DWithBlock(); // 블록의 좌표 정보를 이용하여 블록의 위치를 설정
		printBlock2D(); // 내려오는 블록을 화면에 표시함(콘솔)
	}
	
	public void setBlock2DWithBlock() {
		
		for(int i=0;i<block2D.length;i++) {
			for(int j=0;j<block2D[i].length;j++) {
				block2D[i][j] = 0;
			}
		}
		
		block2D[block.i-1][block.j] = block.kind;
		block2D[block.i][block.j] = block.kind;
		block2D[block.i+1][block.j] = block.kind;
		block2D[block.i+1][block.j-1] = block.kind;
		
	}
	
	public void printBlock2D() {
		System.out.println("---------------------------------------block2D");
		for(int i=0;i<block2D.length;i++) {
			for(int j=0;j<block2D[i].length;j++) {
				System.out.print(block2D[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	public void printStack2D() {
		System.out.println("---------------------------------------stack2D");
		for(int i=0;i<stack2D.length;i++) {
			for(int j=0;j<stack2D[i].length;j++) {
				System.out.print(stack2D[i][j]+" ");
			}
			System.out.println();
		}
	}
	
	
	
	
	

}
