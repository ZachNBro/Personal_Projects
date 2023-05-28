/**
* File: Rectangular.java
* Author: Zachary N. Brown
* Date: June 01, 2022
* Purpose: This subclass is for the Rectangular shape and contains the
* draw method to draw the object on the graphics object
* 
*/

import java.awt.Graphics;
import java.awt.Rectangle;

public class Rectangular extends Shape {
	
	public Rectangular(Rectangle rect, String Color, String fillType) {
		super(rect, Color, fillType);	
	}
	
	@Override
	public void draw(Graphics g) {
		
		Shape.setColor(g);
			
		if (getSolid().equalsIgnoreCase("Hollow")) {
			g.drawRect(x, y, width, height);
		} else {
			g.fillRect(x, y, width, height);
		}	
	}
}
