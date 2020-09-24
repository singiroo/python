package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.SwingConstants;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class Myframe03 extends JFrame {

	private JPanel contentPane;
	private JTextField nInput1;
	private JTextField nInput2;
	private JTextField nResult;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Myframe03 frame = new Myframe03();
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
	public Myframe03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		nInput1 = new JTextField();
		nInput1.setHorizontalAlignment(SwingConstants.CENTER);
		nInput1.setBounds(9, 40, 89, 21);
		contentPane.add(nInput1);
		nInput1.setColumns(10);
		
		nInput2 = new JTextField();
		nInput2.setHorizontalAlignment(SwingConstants.CENTER);
		nInput2.setBounds(145, 40, 89, 21);
		contentPane.add(nInput2);
		nInput2.setColumns(10);
		
		JLabel lblAdder = new JLabel("+");
		lblAdder.setHorizontalAlignment(SwingConstants.CENTER);
		lblAdder.setBounds(107, 43, 29, 15);
		contentPane.add(lblAdder);
		
		JButton btnGetResult = new JButton("=");
		btnGetResult.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
			}
		});
		btnGetResult.setBounds(243, 39, 52, 23);
		contentPane.add(btnGetResult);
		
		nResult = new JTextField();
		nResult.setHorizontalAlignment(SwingConstants.CENTER);
		nResult.setBounds(304, 40, 116, 21);
		contentPane.add(nResult);
		nResult.setColumns(10);
		btnGetResult.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				nResult.setText(
						String.valueOf(Integer.parseInt(nInput1.getText()) 
								+ Integer.parseInt(nInput2.getText())));	
			}
		});
	}
}
