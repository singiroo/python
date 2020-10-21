package com.digiburo.backprop1b.demo3;

import java.io.File;

import java.awt.event.*;

import java.awt.GridLayout;
import java.awt.GridBagLayout;
import java.awt.GridBagConstraints;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;

import javax.swing.border.BevelBorder;
import javax.swing.border.TitledBorder;

import com.digiburo.backprop1b.network.Pattern;
import com.digiburo.backprop1b.network.PatternList;

/**
 * GUI for BdDemo3.  Divided into four panels.
 * Left to right: selection, edit, result.
 * Bottom: apply button.
 *
 * <P>
 * Selection panel as ten buttons, one for each digit.  This permits
 * selection of any training digit.  When the button is pressed,
 * the original pixels as presented in the edit panel.
 *
 * <P>
 * Edit panel allows a pixel to be toggled as set/cleared.  This
 * allows one to distort the original pattern.
 *
 * <P>
 * Result panel shows the answer from the neural network.  
 *
 * <P>
 * Apply button submits the pattern contained in the edit panel
 * to the neural network and updates the result panel w/the answer.
 *
 * @author G.S. Cole (gsc@digiburo.com)
 * @version $Id: BpDigitTestGui.java,v 1.3 2002/02/03 20:31:41 gsc Exp $
 */

/*
 * Development Environment:
 *   Linux 2.2.12-20 (Red Hat 6.1)
 *   Java Developers Kit 1.2.2-RC2-K
 *
 * Legalise:  
 *   Copyright (C) 2002 Digital Burro, INC.
 *
 * Maintenance History:
 *   $Log: BpDigitTestGui.java,v $
 *   Revision 1.3  2002/02/03 20:31:41  gsc
 *   Format tweaks
 *
 *   Revision 1.2  2002/02/03 18:51:08  gsc
 *   Format tweaks
 *
 *   Revision 1.1  2002/02/03 04:24:05  gsc
 *   Initial Check In
 */

public class BpDigitTestGui extends JFrame {
 
	public static final String TRAIN_FILENAME = "demo3.trn";    
    public static final String NETWORK_FILENAME = "demo3.serial";

    public static final double ONE = 0.9999999999;
    public static final double ZERO = 0.0000000001;

    private final PanelNnResult panelnnresult;
    private final PanelPatternEdit panelpatternedit;
    private final GridBagConstraints gridbagconstraints;

	/**
     *
     */
	public BpDigitTestGui(String frame_title, final BpDemo3 bpdemo3, final PatternList training) {
		super(frame_title);

		//
		// Specify layout hints
		//
		gridbagconstraints = new GridBagConstraints();
		gridbagconstraints.fill = GridBagConstraints.BOTH;
		gridbagconstraints.anchor = GridBagConstraints.CENTER;
		gridbagconstraints.weightx = 100;
		gridbagconstraints.weighty = 100;

		getContentPane().setLayout(new GridBagLayout());

		panelpatternedit = new PanelPatternEdit(bpdemo3, training);
		PanelPatternSelect panelpatternselect = new PanelPatternSelect(panelpatternedit);
		panelnnresult = new PanelNnResult();
		JButton apply_button = new JButton("Apply Pattern");

		gridbagconstraints.gridx = 0;
		gridbagconstraints.gridy = 0;
		gridbagconstraints.gridwidth = 1;
		gridbagconstraints.gridheight = 1;
		getContentPane().add(panelpatternselect, gridbagconstraints);

		gridbagconstraints.gridx = 1;
		gridbagconstraints.gridy = 0;
		gridbagconstraints.gridwidth = 1;
		gridbagconstraints.gridheight = 1;
		getContentPane().add(panelpatternedit, gridbagconstraints);

		gridbagconstraints.gridx = 2;
		gridbagconstraints.gridy = 0;
		gridbagconstraints.gridwidth = 1;
		gridbagconstraints.gridheight = 1;
		getContentPane().add(panelnnresult, gridbagconstraints);

		gridbagconstraints.gridx = 0;
		gridbagconstraints.gridy = 1;
		gridbagconstraints.gridwidth = 3;
		gridbagconstraints.gridheight = 1;
		gridbagconstraints.weighty = 20;
		getContentPane().add(apply_button, gridbagconstraints);

		apply_button.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent event) {
				panelnnresult.setAnswer(bpdemo3.runNetwork(panelpatternedit.getPattern()));
			}
		});
	}

	/**
	 * driver
	 */
	public static void main(String args[]) throws Exception {
		System.out.println("begin");

		BpDemo3 bd3 = null;
		PatternList training = null;

		training = new PatternList();
		training.reader(new File(TRAIN_FILENAME));

		if (args.length == 0) {
			bd3 = new BpDemo3(new File(NETWORK_FILENAME));
		} else {
			bd3 = new BpDemo3(new File(args[0]));
		}

		BpDigitTestGui bdtg = new BpDigitTestGui("BP Demo 3", bd3, training);

		bdtg.setBackground(java.awt.Color.white);
		bdtg.setSize(500, 350);
		bdtg.setVisible(true);

		System.out.println("end");
	}   
	
	/**
	 * eclipse generated 
	 */
	private static final long serialVersionUID = -7071344260848058959L;
}

/**
 * Select a digit to display.
 */
class PanelPatternSelect extends JPanel {

	/**
	 * @param pep
	 */
	public PanelPatternSelect(final PanelPatternEdit pep) {
		setLayout(new GridLayout(5, 2));

		JButton selections[] = new JButton[10];
		for (int ii = 0; ii < 10; ii++) {
			selections[ii] = new JButton(Integer.toString(ii));
			add(selections[ii]);

			selections[ii].addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent event) {
					pep.setPattern(Integer.parseInt(event.getActionCommand()));
				}
			});
		}

		BevelBorder bevel_border = new BevelBorder(BevelBorder.RAISED);
		this.setBorder(new TitledBorder(bevel_border, "Select Pattern"));
	}
	
	/**
	 * eclipse generated
	 */
	private static final long serialVersionUID = -5698181693665181035L;
}

/**
 * Show the responses from BackProp
 */
class PanelNnResult extends JPanel {

	private JButton[] results;

	/**
     *
     */
	public PanelNnResult() {
		setLayout(new GridLayout(5, 2));

		results = new JButton[10];
		for (int ii = 0; ii < 10; ii++) {
			results[ii] = new JButton(Integer.toString(ii));
			add(results[ii]);
		}

		BevelBorder bevel_border = new BevelBorder(BevelBorder.RAISED);
		this.setBorder(new TitledBorder(bevel_border, "Answer"));

		double temp[] = new double[10];
		setAnswer(temp);
	}

	/**
     *
     */
	public void setAnswer(double[] answers) {
		for (int ii = 0; ii < answers.length; ii++) {
			if (answers[ii] > 0.75) {
				results[ii].setBackground(java.awt.Color.red);
				results[ii].setForeground(java.awt.Color.black);
			} else {
				results[ii].setBackground(java.awt.Color.black);
				results[ii].setForeground(java.awt.Color.red);
			}
		}
	}	
	
	/**
	 * eclipse generated 
	 */
	private static final long serialVersionUID = -4356291377159597583L;
}

/**
 * Interactive 5x5 edit panel
 */
class PanelPatternEdit extends JPanel {

	private PatternList training;

	private JButton[] pixels;
	private double[] pattern;

	/**
     *
     */
	public PanelPatternEdit(BpDemo3 bd3, PatternList training) {
		this.training = training;

		pattern = new double[25];

		setLayout(new GridLayout(5, 5));

		pixels = new JButton[25];
		for (int ii = 0; ii < 25; ii++) {
			pattern[ii] = 0.0;
			pixels[ii] = new JButton(Integer.toString(ii));
			pixels[ii].setBackground(java.awt.Color.black);
			add(pixels[ii]);

			pixels[ii].addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent event) {
					int ndx = Integer.parseInt(event.getActionCommand());

					if (pattern[ndx] < 0.5) {
						pattern[ndx] = BpDigitTestGui.ONE;
						pixels[ndx].setBackground(java.awt.Color.red);
					} else {
						pattern[ndx] = BpDigitTestGui.ZERO;
						pixels[ndx].setBackground(java.awt.Color.black);
					}
				}
			});
		}

		BevelBorder bevel_border = new BevelBorder(BevelBorder.RAISED);
		this.setBorder(new TitledBorder(bevel_border, "Pattern Edit"));
	}

	/**
	 * Show the pattern used for training
	 * 
	 * @param ndx
	 *            index into PatternList
	 */
	public void setPattern(int ndx) {
		// System.out.println("set pattern " + ndx);

		Pattern pp = training.get(ndx);

		double[] original = pp.getInput();

		for (int ii = 0; ii < original.length; ii++) {
			pattern[ii] = original[ii];

			// System.out.println(ii + " " + original[ii]);

			if (original[ii] < 0.5) {
				pixels[ii].setBackground(java.awt.Color.black);
			} else {
				pixels[ii].setBackground(java.awt.Color.red);
			}
		}
	}

    /**
     *
     */
    public double[] getPattern() {
    	return(pattern);
    }	
    
    /**
	 * eclipse generated 
	 */
	private static final long serialVersionUID = 7143340791046661355L;

}
