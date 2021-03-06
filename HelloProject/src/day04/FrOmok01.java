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

public class FrOmok01 extends JFrame {

	private JPanel contentPane;
	private JLabel[] arr2D = new JLabel[10];
	private JLabel[][] arr2 = new JLabel[10][10];
	private ImageIcon iie = new ImageIcon(FrOmok01.class.getResource("/day04/0.jpg"));
	private ImageIcon iiw = new ImageIcon(FrOmok01.class.getResource("/day04/1.jpg"));
	private ImageIcon iib = new ImageIcon(FrOmok01.class.getResource("/day04/2.jpg"));
	private boolean turn = false;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrOmok01 frame = new FrOmok01();
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
	public FrOmok01() {
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
						
						
						
						
//						if(turn) {
//							lbl.setIcon(iiw);							
//						}else {
//							lbl.setIcon(iib);
//						}
//						turn = !turn;
					}
				});
			}
		}
		
	}
}
