/**
* File: Drawing.java
* Author: Zachary N. Brown
* Date: June 01, 2022
* Purpose: This class saves the created shape object in the GUI 
* to be passed to the paint component method and drawn on the panel
* 
*/

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.util.Objects;
import javax.swing.JPanel;

public class Drawing extends JPanel {
	
		public Shape currentShape = null;
		
		@Override
		public void paintComponent (Graphics g) {
			
			super.paintComponent(g);
			// Draw the created shape
			if (!Objects.isNull(currentShape)) {	
				currentShape.draw(g);
				
				// Count number of shapes
				g.setColor(Color.BLACK);
				g.drawString(String.valueOf(Shape.getNoOfShapes()), 10, 10);
			}
		}
	
		@Override
		public Dimension getPreferredSize () {
			
			return new Dimension(200, 200);		
		}
	
		public void drawShape(Shape createdShape) {
			// Save shape for access by paintComponent
			currentShape = createdShape;

			// Clear the pane and draw the new shape
			repaint();
		}	
}
		

		

	

		

		

		
