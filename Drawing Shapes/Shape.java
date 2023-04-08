/**
* File: Shape.java
* Author: Zachary N. Brown
* Date: June 01, 2022
* Purpose: This abstract class provides the base constructor
* for each shape and methods for specifying unique attributes
* 
*/

import java.awt.Rectangle;
import java.awt.Color;
import java.awt.Graphics;

public abstract class Shape extends Rectangle {

		private static String color;
		private String solidHollow;
		private static int numOfShapes = 0;
		  
		public Shape(Rectangle rect, String Color, String fillType) {
			super(rect); // Pass geometry to the base rectangle
			color = Color;
			solidHollow = fillType;
			numOfShapes++;
		}
	
		public static void setColor(Graphics g) {
			
			if(color.equalsIgnoreCase("black"))
				g.setColor(Color.BLACK);
			else if(color.equalsIgnoreCase("red"))
				g.setColor(Color.RED);
			else if(color.equalsIgnoreCase("orange"))
				g.setColor(Color.ORANGE);
			else if(color.equalsIgnoreCase("yellow"))
				g.setColor(Color.YELLOW);
			else if(color.equalsIgnoreCase("green"))
				g.setColor(Color.GREEN);
			else if(color.equalsIgnoreCase("blue"))
				g.setColor(Color.BLUE);
			else if(color.equalsIgnoreCase("magenta"))
				g.setColor(Color.MAGENTA);
		}
		
		public String getSolid() {
			return solidHollow;
		}
		
		public static int getNoOfShapes() {
			return numOfShapes;
		}
			  
		public abstract void draw(Graphics g);
}