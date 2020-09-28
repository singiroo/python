package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.ImageIcon;

public class FrOmok02 extends JFrame {

	private JPanel contentPane;
	private JLabel[] arr2D = new JLabel[10];
	private JLabel[][] arr2 = new JLabel[10][10];
	private int[][]	int2d = new int[10][10];
	private ImageIcon iie = new ImageIcon(FrOmok02.class.getResource("/day04/0.jpg"));
	private ImageIcon iiw = new ImageIcon(FrOmok02.class.getResource("/day04/1.jpg"));
	private ImageIcon iib = new ImageIcon(FrOmok02.class.getResource("/day04/2.jpg"));
	private boolean turn = false;
	private boolean flagIng = true;
	private String winner = "";

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrOmok02 frame = new FrOmok02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
				
			}
			
		});
	}
	
	
	public void showInt2d() {
		for(int i=0;i<int2d.length;i++) {
			for(int j=0;j<int2d[i].length;j++) {
				System.out.print("\t"+int2d[i][j]);
			}
			System.out.println();
		}
	}
	
	public void myRender() {
		for(int i=0;i<int2d.length;i++) {
			for(int j=0;j<int2d[i].length;j++) {
				int data = int2d[i][j];
				if(data == 0) {
					arr2[i][j].setIcon(iie);
				}else if(data == 1) {
					arr2[i][j].setIcon(iiw);
				}else {
					arr2[i][j].setIcon(iib);
				}
			}
		}
	}
	
	
	/**
	 * Create the frame.
	 */
	public FrOmok02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 812, 691);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
	
		
		for(int j=0;j<arr2.length;j++) {
			for(int i=0; i<arr2D.length; i++) {
				JLabel lbl = new JLabel("New label");
				lbl.setIcon(iie);
				lbl.setText(j+","+i);
				lbl.setBounds(0+(75*i), 0+(75*j), 75, 75);
				contentPane.add(lbl);
				arr2D[i] = lbl;
				arr2[j][i] = lbl;
				lbl.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						myclick(e);
					}
				});
			}
		}
			
		showInt2d();
		myRender();
		
	}
	
	public void myclick(MouseEvent e) {
		
//		if(!flagIng)) {
//			return;
//		}
		
		JLabel temp = (JLabel)e.getComponent();
		System.out.println(temp.getText());
		String locator = temp.getText();
		String[] location = locator.split(",");
		int x = Integer.parseInt(location[0]);
		int y = Integer.parseInt(location[1]);
		
		if(temp.getIcon() != iie) {
			System.out.println("�ߺ��� ��ġ�Դϴ�!!");
			return;
		}
		// ��� �� (1)
		int cnt_stone = 1;
		
		if(turn) {
			int2d[x][y] = 1;
			cnt_stone = 1;
		}else{
			int2d[x][y] = 2;
			cnt_stone = 2;
		}
		
		myRender();
		
		int up_cnt = getUp(x, y, cnt_stone);
		int dw_cnt = getDown(x, y, cnt_stone);
		int left_cnt = getLeft(x, y, cnt_stone);
		int right_cnt = getRight(x, y, cnt_stone);
		
		int uple_cnt = getUpLe(x, y, cnt_stone);
		int upRi_cnt = getUpRi(x, y, cnt_stone);
		int dwle_cnt = getdwLe(x, y, cnt_stone);
		int dwRi_cnt = getdwRi(x, y, cnt_stone);
		
		
		int[] cnt5p = new int[4];
		
		cnt5p[0] = up_cnt + dw_cnt + 1;
		cnt5p[1] = left_cnt + right_cnt + 1;
		cnt5p[2] = uple_cnt + dwRi_cnt + 1;
		cnt5p[3] = upRi_cnt + dwle_cnt + 1;
		
		for(int cnt : cnt5p) {
			if(cnt == 5) {
			  winner = 	turn == true ? "�鵹" : "�浹";
			  JOptionPane.showMessageDialog(null, winner+"�� �̰���ϴ�.");	
			  flagIng = !flagIng;
//			  System.exit(0);
			}
		}
		
		
		
		System.out.println("up : "+up_cnt);
		System.out.println("down : "+dw_cnt);
		System.out.println("left : "+left_cnt);
		System.out.println("right : "+right_cnt);
		System.out.println("upleft : "+uple_cnt);
		System.out.println("upright : "+upRi_cnt);
		System.out.println("downleft : "+dwle_cnt);
		System.out.println("downright : "+dwRi_cnt);

		turn = !turn;
	}
	
	
	public int getUp(int x, int y, int cnt_stone) {
		int cnt = 0;
		//����
		try {
			while(true) {
				if(int2d[--x][y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;			
	}
	
	public int getDown(int x, int y, int cnt_stone) {
		int cnt = 0; // ���� ���� ����
		
		try {
			while(true) {
				if(int2d[++x][y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	
	public int getLeft(int x, int y, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				if(int2d[x][--y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	
	public int getRight(int x, int y, int cnt_stone) {
		int cnt = 0;
		try {
			while(true) {
				if(int2d[x][++y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	
	public int getUpLe(int x, int y, int cnt_stone) {
		int cnt = 0;
		//����
		try {
			while(true) {
				if(int2d[--x][--y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;			
	}
	
	public int getUpRi(int x, int y, int cnt_stone) {
		int cnt = 0;
		//����
		try {
			while(true) {
				if(int2d[--x][++y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;			
	}
	
	public int getdwLe(int x, int y, int cnt_stone) {
		int cnt = 0; // ���� ���� ����
		
		try {
			while(true) {
				if(int2d[++x][--y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	
	public int getdwRi(int x, int y, int cnt_stone) {
		int cnt = 0; // ���� ���� ����
		
		try {
			while(true) {
				if(int2d[++x][++y] == cnt_stone) {
					cnt++;
				}else {
					break;
				}
			}			
		}catch(IndexOutOfBoundsException e) {
			System.out.println("line out");
		}
		
		return cnt;
	}
	
	
	
	
	
	
	
}
