package day10;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.Graphics2D;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import day09.Block;

import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Color;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.awt.Font;

public class Tetris03 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl;
	private JLabel lblRow;
	private JLabel lblDisp;
	private JLabel[][] lblArray2d = new JLabel[20][10]; // 전체 게임판
	public Block block = new Block(); 				//블록 객체
	
	public int[][] block2D = new int[20][10];		//내려오는 블록의 배열
	public int[][] stack2D = new int[20][10];		//아래에 쌓여있는 블록의 배열
	public int[][] scrin2D = new int[20][10];		//게임 진행 화면의 배열
	public boolean flagIng = true;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Tetris03 frame = new Tetris03();
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
	public Tetris03() {
		
		
		
		
		
		addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				myPress(e);				//키보드 이벤트를 메서드로 정의
			}
		});
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 564, 697);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lblDisp = new JLabel("\uBAA9\uD45C : ");
		lblDisp.setFont(new Font("굴림", Font.PLAIN, 15));
		lblDisp.setBounds(283, 31, 57, 15);
		contentPane.add(lblDisp);
		
		lblRow = new JLabel("1");
		lblRow.setFont(new Font("굴림", Font.PLAIN, 15));
		lblRow.setBounds(341, 31, 57, 15);
		contentPane.add(lblRow);
		
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
				lbl.setBounds(25*j ,25*i, 24, 24);
				lbl.setBackground(Color.DARK_GRAY);					
				lblArray2d[i][j] = lbl;
				contentPane.add(lblArray2d[i][j]);
			}
		}
		
		

		System.out.println(block);
		print2D(block2D);
		print2D(stack2D);
		
		new Thread() {
			@Override
			public void run() {
				try {
					while(flagIng) {
						Thread.sleep(1000);
						realPress(KeyEvent.VK_DOWN);						
					}
				} catch (InterruptedException e) {
				}
			}
		}.start();
	}
	
	public void myRender() {
		for(int i=0;i<scrin2D.length;i++) {
			for(int j=0;j<scrin2D[i].length;j++) {				
				if(scrin2D[i][j] == 0) {
					lblArray2d[i][j].setBackground(Color.DARK_GRAY);
				}
				if(scrin2D[i][j] == 1) {
					lblArray2d[i][j].setBackground(Color.RED);
				}
				if(scrin2D[i][j] == 2) {
					lblArray2d[i][j].setBackground(Color.ORANGE);
				}
				if(scrin2D[i][j] == 3) {
					lblArray2d[i][j].setBackground(Color.YELLOW);
				}
				if(scrin2D[i][j] == 4) {
					lblArray2d[i][j].setBackground(Color.GREEN);
				}
				if(scrin2D[i][j] == 5) {
					lblArray2d[i][j].setBackground(Color.BLUE);
				}
				if(scrin2D[i][j] == 6) {
					lblArray2d[i][j].setBackground(Color.WHITE);
				}
				if(scrin2D[i][j] == 7) {
					lblArray2d[i][j].setBackground(Color.CYAN);
				}
				if(scrin2D[i][j] == 11) {
					lblArray2d[i][j].setBackground(Color.magenta);
				}
				if(scrin2D[i][j] == 12) {
					lblArray2d[i][j].setBackground(Color.magenta);
				}
				if(scrin2D[i][j] == 13) {
					lblArray2d[i][j].setBackground(Color.magenta);
				}
				if(scrin2D[i][j] == 14) {
					lblArray2d[i][j].setBackground(Color.magenta);
				}
				if(scrin2D[i][j] == 15) {
					lblArray2d[i][j].setBackground(Color.magenta);
				}
				if(scrin2D[i][j] == 16) {
					lblArray2d[i][j].setBackground(Color.magenta);
				}
				if(scrin2D[i][j] == 17) {
					lblArray2d[i][j].setBackground(Color.magenta);
				}
				
			}
		}
	}
	
	public void myPress(KeyEvent e) {
		realPress(e.getKeyCode());
	}
	

	/**
	 * 방향키 입력시 블록이 움직이는 메서드
	 * @param e		키입력 이벤트
	 */
	public void realPress(int keyCode) {
		boolean flag_col_bound = false;
		boolean flag_down = false;
		int pre_status = block.status;
		int pre_i = block.i;
		int pre_j = block.j;
		
		if(!flagIng) {
			return;
		}
		
		
		if(keyCode == KeyEvent.VK_LEFT) {
			block.j--;
		}
		if(keyCode == KeyEvent.VK_RIGHT) {
			block.j++;
		}
		if(keyCode == KeyEvent.VK_DOWN) {
			block.i++;
			flag_down = true;
		}
		if(keyCode == KeyEvent.VK_UP ) {
			changeBlockStatus();
		}
		System.out.println(block);
		
		
		try {			
			setBlock2DWithBlock(); // 블록의 좌표 정보를 이용하여 블록의 위치를 설정
		}catch(Exception ex) {
			flag_col_bound = true;
		}
		
		
		moveStackBlockToScrin();
		
		boolean flag_collision = isCollision();
		if(flag_collision || flag_col_bound) {
			block.status = pre_status;
			block.i = pre_i;
			block.j = pre_j;
			setBlock2DWithBlock();
			moveStackBlockToScrin();
			if(flag_down) {
				
				moveBlockToStack();
				
				ArrayList<String> notFullStack = getNotFullStack(); //지워지지 않는 줄의 정보
				int cnt10 = 20 - notFullStack.size(); // 지워지는 줄의 수
				if(cnt10 > 0) {
					lblRow.setText(String.valueOf(Integer.parseInt(lblRow.getText())-cnt10));					
				}
				
				if(Integer.parseInt(lblRow.getText()) <= 0) {
					JOptionPane.showMessageDialog(null, "이김.");
					flagIng = false;
					return;
				}
				
				for(int i=0; i<stack2D[4].length; i++) {
					if(stack2D[4][i] > 0) {
						JOptionPane.showMessageDialog(null, "졌음");
						flagIng = false;
						return;
					}
				}
				
				
//				int cnt10 = getCnt10();
				
				System.out.println("cnt10 :" + cnt10);
				
				for(int i=0; i<cnt10; i++) {
					notFullStack.add(0,"0,0,0,0,0,0,0,0,0,0"); // 지워지는 줄의 수만큼 위쪽의 줄을 더해줌
				}
				
				for(int i=0; i<notFullStack.size(); i++ ) {
					String line = notFullStack.get(i);
					String[] data = line.split(",");
					stack2D[i][0] = Integer.parseInt(data[0]);
					stack2D[i][1] = Integer.parseInt(data[1]);
					stack2D[i][2] = Integer.parseInt(data[2]);
					stack2D[i][3] = Integer.parseInt(data[3]);
					stack2D[i][4] = Integer.parseInt(data[4]);
					stack2D[i][5] = Integer.parseInt(data[5]);
					stack2D[i][6] = Integer.parseInt(data[6]);
					stack2D[i][7] = Integer.parseInt(data[7]);
					stack2D[i][8] = Integer.parseInt(data[8]);
					stack2D[i][9] = Integer.parseInt(data[9]);
				}
				
				
				
				
				block.init();
				setBlock2DWithBlock();
				moveStackBlockToScrin();
			
			}
		}
		
		
		System.out.println("flag_collision : " + flag_collision);
		System.out.println("flag_col_bound : " + flag_col_bound);
		
		myRender();
		
		print2D(scrin2D); // 내려오는 블록을 화면에 표시함(콘솔)
	}
	
	public ArrayList<String> getNotFullStack() {
		ArrayList<String> stack_temp = new ArrayList<>();
		
		for(int i=0; i<stack2D.length;i++) {
			int[] tmp = stack2D[i];
			if(					// 블록이 지워지는 조건
				tmp[0] > 0 &&
				tmp[1] > 0 &&
				tmp[2] > 0 &&
				tmp[3] > 0 &&
				tmp[4] > 0 &&
				tmp[5] > 0 &&
				tmp[6] > 0 &&
				tmp[7] > 0 &&
				tmp[8] > 0 &&
				tmp[9] > 0
			  ) {
			}else {
				String str_line = tmp[0]+","+tmp[1]+","+tmp[2]+","+tmp[3]+","+tmp[4]+","+tmp[5]+","+tmp[6]+","+tmp[7]+","+tmp[8]+","+tmp[9]; // 다 채워지지 않은 블록
				stack_temp.add(str_line);
			}
		}
		return stack_temp;
	}
	
	public int getCnt10() {
		int cnt = 0;
		for(int i=0; i<stack2D.length;i++) {
			for(int j = 0; j<stack2D[i].length;j++) {
				if(stack2D[i][j] == 0) {
					break;
				}else if(j == stack2D[i].length -1) {
					cnt++;
				}
			}
		}
		
		return cnt;
	}
	
	
	
	public void moveBlockToStack() {
		for(int i=0;i<block2D.length;i++) {
			for(int j=0;j<block2D[i].length;j++) {
				if(block2D[i][j] > 0) {
					stack2D[i][j] = block2D[i][j]+10;
				}
			}
		}
	}
	
	
	
	
	
	public boolean isCollision() {
		
		boolean ret = false;
		 for(int i= 0;i<scrin2D.length;i++) {
			 for(int j=0;j<scrin2D[i].length;j++) {
				 if(block2D[i][j] > 0 && stack2D[i][j] > 0) {
					 ret = true;
				 }
			 }
		 }
		
		return ret;
	}
	
	public void changeBlockStatus() {
		if(block.kind == 1) {
			block.status = 1;
		}
		if(block.kind == 2 || block.kind == 3 || block.kind == 4) {
			if(block.status == 1) {
				block.status = 2;
			}else if(block.status ==2) {
				block.status = 1;
			}
		}
		if(block.kind == 5 || block.kind == 6 || block.kind == 7) {
			if(block.status == 1) {
				block.status = 2;
			}else if(block.status == 2) {
				block.status = 3;
			}else if (block.status == 3) {
				block.status = 4;
			}else if(block.status == 4) {
				block.status = 1;
			}
			
		}
		
	}
	
	public void moveStackBlockToScrin() {
		
		for(int i=0;i<scrin2D.length;i++) {
			for(int j=0;j<scrin2D[i].length;j++) {
				scrin2D[i][j] = block2D[i][j] + stack2D[i][j];
			}
		}
	}
	
	public void setBlock2DWithBlock() {
		
		for(int i=0;i<block2D.length;i++) {
			for(int j=0;j<block2D[i].length;j++) {
				block2D[i][j] = 0;
			}
		}
		
		
		if(block.kind == 1) {
			block2D[block.i][block.j] = block.kind;
			block2D[block.i+1][block.j] = block.kind;
			block2D[block.i+1][block.j+1] = block.kind;
			block2D[block.i][block.j+1] = block.kind;
		}
		
		if(block.kind == 2) {
			if(block.status == 1) {
				block2D[block.i-1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i+1][block.j] = block.kind;
				block2D[block.i+2][block.j] = block.kind;
			}
			if(block.status == 2) {
				block2D[block.i][block.j-2] = block.kind;
				block2D[block.i][block.j-1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j+1] = block.kind;
				
			}
		}
		
		if(block.kind == 3) {
			if(block.status == 1) {
				block2D[block.i][block.j-1]=block.kind;
				block2D[block.i][block.j]=block.kind;
				block2D[block.i+1][block.j]=block.kind;
				block2D[block.i+1][block.j+1]=block.kind;
			}
			if(block.status == 2) {
				block2D[block.i-1][block.j]=block.kind;
				block2D[block.i][block.j]=block.kind;
				block2D[block.i][block.j-1]=block.kind;
				block2D[block.i+1][block.j-1]=block.kind;
			}
		}
		
		if(block.kind == 4) {
			if(block.status == 1) {
				block2D[block.i][block.j+1]=block.kind;
				block2D[block.i][block.j]=block.kind;
				block2D[block.i+1][block.j]=block.kind;
				block2D[block.i+1][block.j-1]=block.kind;
			}
			if(block.status == 2) {
				block2D[block.i-1][block.j-1]=block.kind;
				block2D[block.i][block.j-1]=block.kind;
				block2D[block.i][block.j]=block.kind;
				block2D[block.i+1][block.j]=block.kind;
			}
		}
		
		if(block.kind == 5) {
			if(block.status == 1) {
				block2D[block.i][block.j-1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i-1][block.j] = block.kind;
				block2D[block.i][block.j+1] = block.kind;
			}
			if(block.status == 2) {
				block2D[block.i-1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i+1][block.j] = block.kind;
				block2D[block.i][block.j+1] = block.kind;
			}
			if(block.status == 3) {
				block2D[block.i][block.j-1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j+1] = block.kind;
				block2D[block.i+1][block.j] = block.kind;
			}
			if(block.status == 4) {
				block2D[block.i-1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i+1][block.j] = block.kind;
				block2D[block.i][block.j-1] = block.kind;
			}
		}
		
		if(block.kind == 6) {
			if(block.status == 1) {
				block2D[block.i-1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i+1][block.j] = block.kind;
				block2D[block.i-1][block.j-1] = block.kind;
			}
			if(block.status == 2) {
				block2D[block.i][block.j-1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j+1] = block.kind;
				block2D[block.i-1][block.j+1] = block.kind;
			}
			if(block.status == 3) {
				block2D[block.i-1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i+1][block.j] = block.kind;
				block2D[block.i+1][block.j+1] = block.kind;
			}
			if(block.status == 4) {
				block2D[block.i][block.j-1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j+1] = block.kind;
				block2D[block.i+1][block.j-1] = block.kind;
			}
		}
		
		if(block.kind == 7) {
			if(block.status == 1) {
				block2D[block.i-1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i+1][block.j] = block.kind;
				block2D[block.i+1][block.j-1] = block.kind;				
			}
			if(block.status == 2) {
				block2D[block.i-1][block.j-1] = block.kind;
				block2D[block.i][block.j-1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j+1] = block.kind;
			}
			if(block.status == 3) {
				block2D[block.i-1][block.j+1] = block.kind;
				block2D[block.i-1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i+1][block.j] = block.kind;
				
			}
			if(block.status == 4) {
				block2D[block.i][block.j-1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j+1] = block.kind;
				block2D[block.i+1][block.j+1] = block.kind;	
			}
			
		}
		
		
	}
	
	public void print2D(int[][] arr2D) {
		System.out.println("---------------------------------------");
		for(int i=0;i<arr2D.length;i++) {
			for(int j=0;j<arr2D[i].length;j++) {
				System.out.print(arr2D[i][j]+" ");
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
