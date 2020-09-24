package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.SwingConstants;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Myframe02 extends JFrame {

	private JPanel contentPane;
	private JLabel lbl;
	private JButton btnDecrease;
	private int cnt = 1;
	private JButton btnReset;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Myframe02 frame = new Myframe02();
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
	public Myframe02() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		lbl = new JLabel("1");
		lbl.setHorizontalAlignment(SwingConstants.CENTER);
		lbl.setBounds(40, 35, 104, 15);
		contentPane.add(lbl);
		
		JButton btnIncrease = new JButton("Increase by 1");
		btnIncrease.addMouseListener(new MouseAdapter() {
		
			@Override
			public void mouseClicked(MouseEvent e) {
				lbl.setText(String.valueOf((++cnt)));
			}
		});
		btnIncrease.setBounds(247, 31, 133, 23);
		contentPane.add(btnIncrease);
		
		btnDecrease = new JButton("Decrease by 1");
		btnDecrease.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				lbl.setText(String.valueOf((--cnt)));
			}
		});
		btnDecrease.setBounds(247, 71, 133, 23);
		contentPane.add(btnDecrease);
		
		btnReset = new JButton("Reset to 1");
		btnReset.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				cnt = 1;
				lbl.setText(String.valueOf(cnt));
			}
		});
		btnReset.setBounds(247, 112, 133, 23);
		contentPane.add(btnReset);
	}

}
