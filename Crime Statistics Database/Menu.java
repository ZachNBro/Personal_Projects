/**
* File: TestCrime.java
* Author: Zachary N. Brown
* Date: August 10, 2020
* Purpose: Creates the new Menu object and the 
* necessary code to loop through each user
* selection
*/

import java.util.ArrayList;
import java.util.Scanner;

public class Menu {
	  
	private CrimeData crimeData;

		// Constructor
		public Menu(CrimeData crimeDataParm) {	
		crimeData = crimeDataParm;
		}
		
		// Fields to use for user input
		public String selection;
		public Scanner input;
		
		// Method to be initiated by the test class and display menu to user
		public void menu() {
					
	    	System.out.println("******************** Welcome to The US Crime Statistical Application ********************");
	    	System.out.println("\nEnter the number of the information you would like to know about. Enter 'Q' to quit the program:\n");
	    	System.out.println("1. What were growth percentages in population growth for each consecutive year from 1994 - 2013?");
	    	System.out.println("2. What year was the Murder rate the highest?");
	    	System.out.println("3. What year was the Murder rate the lowest?");
	    	System.out.println("4. What year was the Robbery rate the highest?");
	    	System.out.println("5. What year was the Robbery rate the lowest?");
	    	System.out.println("Q. Quit the program");	
	    	System.out.print("\nEnter your selection: ");
	    		
	    	userSelection();
		}
	    		
		// Method to scan for user input
		public void userSelection() {
	    		
	    	String userInput; 
	    		
	    	input = new Scanner(System.in);
	    		
	    	userInput = input.next().toUpperCase(); 
	    	reportSelection(userInput); 
	    	input.close();
		}
	    	
		// Method to scan for specific user input
		public void optionToQuit() {
	
	    	String userInput;
	
	    	input = new Scanner(System.in);
	    		
	    	System.out.println("\nEnter 'M' for menu or 'Q' to quit");
	    	userInput = input.next().toUpperCase();
	    		
	    	
	    	if(userInput.compareTo("M") == 0) { 
	    	
		menu(); 
	    			
	    	} else if (userInput.compareTo("Q") == 0) { 
	    		reportSelection(userInput);
	    			
	    	} else {
	    		System.out.println("**Invalid selection - Returning to menu**.\n\n\n\n");
	    		menu(); 
	    	}
	    		
	    	input.close();	
		}
		
		// Loop to call methods from the CrimeData class to display applicable data
		public void reportSelection(String selection){
		
		boolean askContinue = false; 
		
			if ("1".equals(selection)) {
				ArrayList<String> growthRateChart = crimeData.popGrowthRate();
					for(String year : growthRateChart)
						System.out.println(year);
						skContinue = true;
			
			} else if ("2".equals(selection)) {
				System.out.println(crimeData.murderRateHigh());
				askContinue = true;
							
			} else if ("3".equals(selection)) {
				System.out.println(crimeData.murderRateLow());
				askContinue = true;
							
			} else if ("4".equals(selection)) {
				System.out.println(crimeData.robberyRateHigh());
				askContinue = true;
							
			} else if ("5".equals(selection)) {
				System.out.println(crimeData.robberyRateLow());
				askContinue = true;
							
			} else if ("Q".equals(selection)) {
				return;
							
			} else if ("M".equals(selection)) {
				menu();
							
			} else {
				System.out.println("\n\n**Invalid Entry. Please re enter your selection**\n");
			menu();	
			}
			    		
			if(askContinue){
		    		optionToQuit(); 
		    		askContinue = false; 
			}
		}			
}
