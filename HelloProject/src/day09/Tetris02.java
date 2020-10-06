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
	private JLabel[][] lblArray2d = new JLabel[20][10]; // ��ü ������
	public Block block = new Block(); 				//���� ��ü
	
	public int[][] block2D = new int[20][10];		//�������� ������ �迭
	public int[][] stack2D = new int[20][10];		//�Ʒ��� �׿��ִ� ������ �迭
	public int[][] scrin2D = new int[20][10];		//���� ���� ȭ���� �迭
	

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
				myPress(e);				//Ű���� �̺�Ʈ�� �޼���� ����
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
		
		//��ü ������ ����
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
	 * ����Ű �Է½� ������ �����̴� �޼���
	 * @param e		Ű�Է� �̺�Ʈ
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
		
		setBlock2DWithBlock(); // ������ ��ǥ ������ �̿��Ͽ� ������ ��ġ�� ����
		printBlock2D(); // �������� ������ ȭ�鿡 ǥ����(�ܼ�)
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