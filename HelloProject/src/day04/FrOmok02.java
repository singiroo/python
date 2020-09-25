package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
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
	private int cnt = 0;

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
		int2d[1][1] =1;
		int2d[2][2] =2;
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
						System.out.println(up_cnt);
						turn = !turn;
					}
				});
			}
		}
		
		showInt2d();
		myRender();
		
	}
	
	public int getUp(int x, int y, int cnt_stone) {
		int cnt = 0;
		//����
		while(true) {
			if(int2d[x][++y] == cnt_stone) {
				cnt++;
			}else {
				cnt = 0;
				break;
			}
		}
		return cnt;
		
	}
}