/**
* File: Oval.java
* Author: Zachary N. Brown
* Date: June 01, 2022
* Purpose: This subclass is for the Oval shape and contains the
* draw method to draw the object on the graphics object
* 
*/

import java.awt.Graphics;
import java.awt.Rectangle;

public class Oval extends Shape {
	
	public Oval(Rectangle rect, String Color, String fillType) {
		super(rect, Color, fillType);	
	}

	@Override
	public void draw(Graphics g) {
		
			Shape.setColor(g);	
			
			if (getSolid().equalsIgnoreCase("Hollow")) {
				g.drawOval(x, y, width, height);
			} else {
				g.fillOval(x, y, width, height);
			}
	}
}
