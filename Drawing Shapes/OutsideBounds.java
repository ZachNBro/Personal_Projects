/**
* File: OutsideBounds.java
* Author: Zachary N. Brown
* Date: June 01, 2022
* Purpose: This class provides an outside bounds message if the
* user inputs a shape outside of the preferred dimensions
* 
*/

import javax.swing.JOptionPane;

public class OutsideBounds extends Exception {
  
	public OutsideBounds (String errorMessage) {
		super(errorMessage);
		
	}	
}
