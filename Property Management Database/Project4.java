/**
* File: Project4.java
* Author: Zachary N. Brown
* Date: October 13, 2022
* Purpose: This class contains the GUI to input the
* required values for each new property and call the
* methods of the Property class
*/

import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import java.awt.Font;
import javax.swing.JButton;
import javax.swing.JComboBox;
import java.util.Objects;
import java.util.TreeMap;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Project4 {
	
	// TreeMap object creation specified by an Integer (transaction ID) key and Property value
	private TreeMap<Integer, Property> propertyDB = new TreeMap <Integer, Property>();
	
	private JFrame frmRealEstateDatabase;
	private JTextField transactionNumberField;
	private JTextField addressField;
	private JTextField bedroomsField;
	private JTextField squareFootageField;
	private JTextField priceField;
		
	public Project4() {		
		initialize();
	}

		public void initialize() {
			
			frmRealEstateDatabase = new JFrame();
			frmRealEstateDatabase.setTitle("Real Estate Database");
			frmRealEstateDatabase.setBounds(100, 100, 294, 270);
			frmRealEstateDatabase.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
			frmRealEstateDatabase.getContentPane().setLayout(null);
			
			transactionNumberField = new JTextField();
			transactionNumberField.setBounds(134, 9, 136, 20);
			frmRealEstateDatabase.getContentPane().add(transactionNumberField);
			transactionNumberField.setColumns(10);
			
			addressField = new JTextField();
			addressField.setBounds(134, 40, 136, 20);
			frmRealEstateDatabase.getContentPane().add(addressField);
			addressField.setColumns(10);
			
			bedroomsField = new JTextField();
			bedroomsField.setBounds(134, 71, 136, 20);
			frmRealEstateDatabase.getContentPane().add(bedroomsField);
			bedroomsField.setColumns(10);
			
			squareFootageField = new JTextField();
			squareFootageField.setBounds(134, 102, 136, 20);
			frmRealEstateDatabase.getContentPane().add(squareFootageField);
			squareFootageField.setColumns(10);
			
			priceField = new JTextField();
			priceField.setBounds(134, 133, 136, 20);
			frmRealEstateDatabase.getContentPane().add(priceField);
			priceField.setColumns(10);
			
			JLabel transactionNumberLabel = new JLabel("Transaction No:");
			transactionNumberLabel.setFont(new Font("Tahoma", Font.BOLD, 12));
			transactionNumberLabel.setBounds(10, 11, 114, 14);
			frmRealEstateDatabase.getContentPane().add(transactionNumberLabel);
			
			JLabel addressLabel = new JLabel("Address:");
			addressLabel.setFont(new Font("Tahoma", Font.BOLD, 12));
			addressLabel.setBounds(10, 42, 93, 14);
			frmRealEstateDatabase.getContentPane().add(addressLabel);
			
			JLabel bedroomsLabel = new JLabel("Bedrooms:");
			bedroomsLabel.setFont(new Font("Tahoma", Font.BOLD, 12));
			bedroomsLabel.setBounds(10, 73, 86, 14);
			frmRealEstateDatabase.getContentPane().add(bedroomsLabel);
			
			JLabel squareFootageLabel = new JLabel("Square Footage:");
			squareFootageLabel.setFont(new Font("Tahoma", Font.BOLD, 12));
			squareFootageLabel.setBounds(10, 104, 114, 14);
			frmRealEstateDatabase.getContentPane().add(squareFootageLabel);
			
			JLabel priceLabel = new JLabel("Price:");
			priceLabel.setFont(new Font("Tahoma", Font.BOLD, 12));
			priceLabel.setBounds(10, 135, 46, 14);
			frmRealEstateDatabase.getContentPane().add(priceLabel);
			
			JComboBox<String> actionBox = new JComboBox<String>();
			actionBox.setBounds(134, 167, 136, 20);
			actionBox.addItem("Insert");
			actionBox.addItem("Delete");
			actionBox.addItem("Find");
			frmRealEstateDatabase.getContentPane().add(actionBox);
			
			JButton processButton = new JButton("Process");
			
			processButton.addActionListener(new ActionListener() {
			
				// Functions to perform the process function of the program
				public void actionPerformed(ActionEvent arg0) {
					
					try {
						int transactionID = Integer.parseInt(transactionNumberField.getText());
			
						String selection = actionBox.getSelectedItem().toString();
						
						if (selection == "Insert") {
							
							String propertyAddress = addressField.getText().toString();
							int bedrooms = Integer.parseInt(bedroomsField.getText());
							int squareFootage = Integer.parseInt(squareFootageField.getText());
							int price = Integer.parseInt(priceField.getText());
							Status status = Status.FOR_SALE;
							
							Property current = propertyDB.get(transactionID);
							
							// Checks whether the property already exists in the database and displays a message
							if (!Objects.isNull(current)) {
								JOptionPane.showMessageDialog(null, "A property associated with transaction ID: " + transactionID  + " already exists in the database");
								
							} else {
								Property newProperty = new Property(propertyAddress, bedrooms, squareFootage, price, status);
								
								// Construct new Property object and add to TreeMap
								propertyDB.put(transactionID, newProperty);
								
								JOptionPane.showMessageDialog(null, "Transaction ID: " + transactionID + "\n" + newProperty.toString());
							}		
								} else if (selection == "Delete") {
									
									Property currentProperty = propertyDB.remove(transactionID);
									
									// Checks whether the property does not exist in the database and displays a message
									if (Objects.isNull(currentProperty)) {
										JOptionPane.showMessageDialog(null, "Property does not exist in the database");
										
									} else {
										JOptionPane.showMessageDialog(null, "Property associated with the transaction ID: " + transactionID  + " has been deleted");
									}
						
								} else {	
									Property currentProperty = propertyDB.get(transactionID);
											
										if (Objects.isNull(currentProperty)) {
											JOptionPane.showMessageDialog(null, "Property does not exist in the database");
												
										} else {	
											JOptionPane.showMessageDialog(null, "Transaction ID: " + transactionID + "\n" + currentProperty.toString());
										}						
								}  
						
							// Catch block to throw exception if integers are not input into applicable fields
							} catch (NumberFormatException n) { 
									JOptionPane.showMessageDialog(null, "Transaction ID, bedrooms, square footage and price must be integers");
							}
				}
			});
			processButton.setBounds(0, 164, 132, 23);
			frmRealEstateDatabase.getContentPane().add(processButton);
			
			JComboBox<String> statusBox = new JComboBox<String>();
			statusBox.setBounds(134, 198, 136, 20);
			statusBox.addItem("FOR_SALE");
			statusBox.addItem("UNDER_CONTRACT");
			statusBox.addItem("SOLD");
			frmRealEstateDatabase.getContentPane().add(statusBox);
			
			JButton changeStatusButton = new JButton("Change Status");
			changeStatusButton.addActionListener(new ActionListener() {
			
				// Action to change the property status by calling the changeState method and utilizing the bounded generic type parameter
				public void actionPerformed(ActionEvent arg0) {
					
					int transactionID = Integer.parseInt(transactionNumberField.getText());
					Property currentProperty = propertyDB.get(transactionID);
					
					String selection = statusBox.getSelectedItem().toString();
					
					currentProperty.changeState(Status.valueOf(selection));
					
					JOptionPane.showMessageDialog(null, "Status of property changed to: " + selection);
				}
				
			});
			changeStatusButton.setBounds(0, 198, 132, 23);
			frmRealEstateDatabase.getContentPane().add(changeStatusButton);		
		}

	public static void main(String[] args) {
		Project4 window = new Project4();
		window.frmRealEstateDatabase.setVisible(true);
	}
}
