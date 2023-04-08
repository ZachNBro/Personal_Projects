/**
* File: Project3.java
* Author: Zachary N. Brown
* Date: June 01, 2022
* Purpose: This class contains the GUI and the necessary options
* to create unique shapes
* 
*/

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.Box;
import javax.swing.border.TitledBorder;
import javax.swing.UIManager;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Rectangle;
import javax.swing.JComboBox;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Project3 extends JFrame {

	private JPanel contentPane;
	private JTextField widthField;
	private JTextField heightField;
	private JTextField xCoordField;
	private JTextField yCoordField;

	public Project3() {
		
		setTitle("Geometric Drawing");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 437, 305);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		widthField = new JTextField();
		widthField.setBounds(117, 89, 86, 20);
		contentPane.add(widthField);
		widthField.setColumns(10);
		
		heightField = new JTextField();
		heightField.setBounds(117, 120, 86, 20);
		contentPane.add(heightField);
		heightField.setColumns(10);
		
		xCoordField = new JTextField();
		xCoordField.setBounds(117, 182, 86, 20);
		contentPane.add(xCoordField);
		xCoordField.setColumns(10);
		
		yCoordField = new JTextField();
		yCoordField.setBounds(117, 151, 86, 20);
		contentPane.add(yCoordField);
		yCoordField.setColumns(10);
		
		JLabel shapeLabel = new JLabel("Shape Type");
		shapeLabel.setBounds(25, 10, 86, 14);
		contentPane.add(shapeLabel);
		
		JLabel fillLabel = new JLabel("Fill Type");
		fillLabel.setBounds(25, 37, 46, 14);
		contentPane.add(fillLabel);
		
		JLabel colorLabel = new JLabel("Color");
		colorLabel.setBounds(25, 63, 46, 14);
		contentPane.add(colorLabel);
		
		JLabel widthLabel = new JLabel("Width");
		widthLabel.setBounds(25, 92, 46, 14);
		contentPane.add(widthLabel);
		
		JLabel heightLabel = new JLabel("Height");
		heightLabel.setBounds(25, 123, 46, 14);
		contentPane.add(heightLabel);
		
		JLabel xCoordLabel = new JLabel("x coordinate");
		xCoordLabel.setBounds(25, 154, 82, 14);
		contentPane.add(xCoordLabel);
		
		JLabel yCoordLabel = new JLabel("y coordinate");
		yCoordLabel.setBounds(25, 185, 82, 14);
		contentPane.add(yCoordLabel);
		
		Box horizontalBox = Box.createHorizontalBox();
		horizontalBox.setBorder(new TitledBorder(new TitledBorder(UIManager.getBorder("TitledBorder.border"), "Drawing", 
				TitledBorder.LEADING, TitledBorder.TOP, null, new Color(0, 0, 0)), "Shape Drawing", 
				TitledBorder.LEADING, TitledBorder.TOP, null, Color.BLACK));
		
		horizontalBox.setBounds(213, 10, 199, 192);
		contentPane.add(horizontalBox);
		
		JComboBox<String> shapeTypeBox = new JComboBox<String>();
		shapeTypeBox.setBounds(117, 11, 86, 20);
		shapeTypeBox.addItem("Rectangle");
		shapeTypeBox.addItem("Oval"); 
		contentPane.add(shapeTypeBox);
	  
		
		JComboBox<String> fillTypeBox = new JComboBox<String>();
		fillTypeBox.setBounds(117, 37, 86, 20);
		fillTypeBox.addItem("Hollow");
		fillTypeBox.addItem("Solid");
		contentPane.add(fillTypeBox);
		
		JComboBox<String> colorTypeBox = new JComboBox<String>();
		colorTypeBox.setBounds(117, 63, 86, 20);
		colorTypeBox.addItem("Black");
		colorTypeBox.addItem("Red");
		colorTypeBox.addItem("Orange");
		colorTypeBox.addItem("Yellow");
		colorTypeBox.addItem("Green");
		colorTypeBox.addItem("Blue");
		colorTypeBox.addItem("Magenta");
		contentPane.add(colorTypeBox);
		
		// Panel for adding the created shape object
		Drawing drawPanel = new Drawing();
		drawPanel.getPreferredSize();
		horizontalBox.add(drawPanel);
		
		// Draw button
		JButton drawButton = new JButton("Draw");
		drawButton.addActionListener(new ActionListener() {
			
			public void actionPerformed(ActionEvent e) {
				
				try {
					// Extract shape parameters from the entry boxes
					String shapeType = shapeTypeBox.getSelectedItem().toString();
					String fillType = fillTypeBox.getSelectedItem().toString();
					String color = colorTypeBox.getSelectedItem().toString();
				
					// Extract geometry information
					int height = Integer.parseInt(heightField.getText());
					int width = Integer.parseInt(widthField.getText());
					int originX = Integer.parseInt(xCoordField.getText());
					int originY = Integer.parseInt(yCoordField.getText());
					
					// Geometry info communicated using a base rectangle
					Rectangle rect = new Rectangle(originX, originY, width, height);
				
					// Create the requested shape
					Shape createdShape;
					
					if (shapeType == "Rectangle") {   
						createdShape = new Rectangular(rect, color, fillType);
					} else {
						createdShape = new Oval(rect, color, fillType);
					} 
				
					// Draw the shape created
					drawPanel.drawShape(createdShape);
				
					// Throw checked exception if dimensions do not fit inside panel
					if ((width + originX > 200 || height + originY > 200))
					throw new OutsideBounds("Dimensions are outside the panel boundary, please re-enter");
						} catch (OutsideBounds o) {
							JOptionPane.showMessageDialog(null, o.getMessage());
							return;
				
						} catch (NumberFormatException n) { // Error message if a non-integer value is entered
							JOptionPane.showMessageDialog(null, "Height, Width, X and Y Coordinates must be integers.");
							return;			
					} 
			}
		});

		drawButton.setBounds(167, 216, 89, 23);
		contentPane.add(drawButton);
	}	
	
	public static void main(String[] args) {
		
		Project3 frame = new Project3();
				 frame.setVisible(true);
	}	
}